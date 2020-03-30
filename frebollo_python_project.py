
import numpy as np
import time as timer
from sys import argv

#PROSPECTIVE PATHWAYS FOR THE FUTURE ENERGY TRANSITION

#1. electric market study
#2 types of energy generation:
    #wind offshore: 4176MWh/year
    #PV: 1500 MWh/year
#total amount hours per year = 8760h
#demand =100Mwh


class RenewableEnergyMix(object):
    def __init__(self):
        # Mix monitoring
        self.initial_time = timer.perf_counter()
        self.time = time

    def Run (self):
        self.Initialize()
        self.Solve()
        self.Finalize()

    def Initialize(self):
        d = 100 #demand =100Mwh
        demand = np.linspace(d,d,8760) #start, final, steps
        pv_1MW_generation = np.load ("pv_data.csv")
        w_1MW_generation = np.load("w_data.csv")
        
        demand_opex_maint = 1 #1 euro/MWh

        pv_capex = 0.8 #MEur/MW
        pv_opex_inst = 12000 #12000 e/MW
        pv_opex_maint = 1 #1 euro/MWh
        w_capex = 1.2 #MEur/MW
        w_opex_inst = 20000 #12000 e/MW
        w_opex_maint = 1 #1 euro/MWh

        pump_capex = 0.4 #Meur/MW
        pump_opex_inst = 10000 #Eur/MW
        pump_opex_maint = 1 #Eur/MWh
        turbine_capex = 0.6 #Meur/MW
        turbine_opex_inst = 10000 #Eur/MW
        turbine_opex_maint = 1 #Eur/MWh

        storage_time_capacity = 12 # variable between 0 to 24h
        storage_capex = 0.011 #MEur/MWh
        time_amortiguation = 25 #variable between 20 to 30 years
        electricity_grid_cost = 130 #Eur/MWh variable between 60 to 200
        electricity_grid_sell = 45 #Eur/MWh variable between 35 to 55
        rate_discount = 0.045 #% between 3,5 to 5,5
        
        p_eff = 0.9  #pump_efficiency
        t_eff = 0.9 #turbine efficiency

        #x is an unknown (x= pv_installed_power)
        #y is an unknown (y = w_installed_power)
        # p= pump_power is an unknown <= max(demand - (pv_1MW_generation * x) - (w_1MW_generation * y))
        # t = turbine power is an unknown <= (Max(demand - (pv_1MW_generation * x) - (w_1MW_generation * y)))/t_eff

        storage = np.array.arrange(100)
        grid = 

        a=np.zeros(10)





        for i in range(1,self.demand.size)
            if p <= max(demand - (pv_1MW_generation * x) - (w_1MW_generation * y)))

        s_cap = p_eff * t_eff * storage_time_capacity * p # storage_capacity en MWh

        i = np.array(:,600)
        j= np.array (:,500)

       

        for x in i:
            for y in j
        
        a = 
        b = 
        c =
        d =


                demand_cover = demand - (pv_1MW_generation * x) - (w_1MW_generation * y) - storage - grid
        if demand_cover != 0:
            x = 
        #if its positive turbining, 
        #if its negatibe pumping

    def Solve(self):

    def Main():

if __name__== '__main__':
    Main()


