# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 20:21:30 2024

@author: Dustin Miller
"""

from Queue_for_ALGO import Queue
import random
from tabulate import tabulate

CHECKOUT_CONSTANT = 45
SEC_PER_ITEM = 4

class Register:
    def __init__(self):
        self.queue = Queue()
        self.items = []
        self.checkoutTimeRemaining = 0
        self.current_customer = None
        self.customers_served = 0
        self.items_checked_out = 0
        self.idle_time = 0
        self.waiting_time = 0
        
    def add_customer(self, customer):
        self.current_customer = customer
        self.items.append(1)
        self.queue.enqueue(customer)
        self.customers_served += 1
        self.items_checked_out += customer.getItems()
        self.checkoutTimeRemaining = CHECKOUT_CONSTANT + customer.getItems()*SEC_PER_ITEM
    
    def return_queue(self):
        return self.queue
        
    def tick(self) :
        if not(self.idle()):
            self.waiting_time += 1
            self.checkoutTimeRemaining -= 1
            if self.checkoutTimeRemaining <= 0:
                self.current_customer = None
                self.queue.dequeue()
                self.items.remove(1)
        if self.idle() == True:
                self.idle_time += 1
        
    def idle(self):
        return (self.current_customer == None) 
    
    def display(self, time, reg_name):
        print(f'For {reg_name} at {time} seconds:')
        print(f'Customers served = {self.customers_served}')
        print(f'Items checked out = {self.items_checked_out} items')
        print(f'Idle Time = {self.idle_time/60: .2f} minutes')
        print(f'Waiting Time = {self.waiting_time} seconds')
        print()
        

class Customer:
    def __init__(self, items) :
        self.items = items
        self.checkoutTimeRemaining = self.checkout_time()
    
    def getItems(self) :
        return self.items
    
    def checkout_time(self) : 
        self.checkout_time = CHECKOUT_CONSTANT + self.items*SEC_PER_ITEM
        
def simulation(simLength=7200):
    register_one = Register()
    register_two = Register()
    register_three = Register()
    register_four = Register()
    register_express = Register()
    list_registers = [register_one,register_two,register_three,register_four,register_express]
    
    for second in range(simLength):
        for register in list_registers:
            if second % 30 == 0: 
                customer = Customer(random.randint(6,21))
                customer_register = choose_register(customer, register_one,register_two,register_three,register_four,register_express)
                customer_register.add_customer(customer)
            if second % 50 == 0:
                if register == register_one:
                    reg_name = 'Register One'
                if register == register_two:
                    reg_name = 'Register Two'
                if register == register_three:
                    reg_name = 'Register Three'
                if register == register_four:
                    reg_name = 'Register Four'
                if register == register_express:
                    reg_name = 'Express Register'
                register.display(second, reg_name)  
            register.tick()
            
    if second == 7200:
        tabulate_final(register_one,register_two,register_three,register_four,register_express)
    
def choose_register(customer, register_one,register_two,register_three,register_four,register_express):
    if int(customer.getItems()) < 10:
        if register_express.idle == True:
            return register_express
        else:
            return random.choice(shortest_line([register_one,register_two,register_three,register_four,register_express]))
    else:
        return random.choice(shortest_line([register_one,register_two,register_three,register_four]))
        
def shortest_line(list_registers):
    shortest_queues = []
    min_length = 100
    for register in list_registers:
        queue = register.return_queue()
        length = queue.size()
        if length < min_length:
            min_length = length
            shortest_queues = [register]
        elif length == min_length:
            shortest_queues.append(register)
    if shortest_queues == []:
        return [list_registers[0],list_registers[1],list_registers[2], list_registers[3]]
    return shortest_queues

def tabulate_final(register_one,register_two,register_three,register_four,register_express):
    headers = ["Register","Total Customers","Total Items","Total Idle Time(Min)","Avg. Wait Time(Sec)"]
    sum_customers = register_one.customers_served + register_two.customers_served + register_three.customers_served + register_four.customers_served + register_express.customers_served
    sum_items = register_one.items_checked_out + register_two.items_checked_out + register_three.items_checked_out + register_four.items_checked_out + register_express.items_checked_out
    sum_idle = round(register_one.idle_time/60,2) + round(register_two.idle_time/60,2) + round(register_three.idle_time/60,2) + round(register_four.idle_time/60,2) + round(register_express.idle_time/60,2)
    sum_wait = round((round(register_one.waiting_time/register_one.customers_served)+round(register_two.waiting_time/register_two.customers_served)+round(register_three.waiting_time/register_three.customers_served)+round(register_four.waiting_time/register_four.customers_served)+round(register_express.waiting_time/register_express.customers_served))/5)
    data = [['One',register_one.customers_served,register_one.items_checked_out,round(register_one.idle_time/60,2),round(register_one.waiting_time/register_one.customers_served)],
            ['Two',register_two.customers_served,register_two.items_checked_out,round(register_two.idle_time/60,2),round(register_two.waiting_time/register_two.customers_served)],
            ['Three',register_three.customers_served,register_three.items_checked_out,round(register_three.idle_time/60,2),round(register_three.waiting_time/register_three.customers_served)],
            ['Four',register_four.customers_served,register_four.items_checked_out,round(register_four.idle_time/60,2),round(register_four.waiting_time/register_four.customers_served)],
            ['Express',register_express.customers_served,register_express.items_checked_out,round(register_express.idle_time/60,2),round(register_express.waiting_time/register_express.customers_served)],
            ['TOTAL',sum_customers, sum_items, sum_idle, sum_wait]]
    table = tabulate(data, headers, tablefmt="grid")
    print(table)
    
def main():
    for i in range(12):
        simulation()
        
main()