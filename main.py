from pydantic import BaseModel
from typing import Dict, List

import json

if __name__ == '__main__':
    parameters = Parameters()
    manager = Manager(parameters)

    for apartment in manager.apartments.values():
        print(apartment.key, apartment.name, apartment.location, apartment.area_m2)
        for room in apartment.rooms.values():
            print('  ', room.name, room.area_m2)
        
        for bill in manager.bills:
            if bill.apartment == apartment.key:
                print('  ', bill.amount_pln, bill.date_due, bill.settlement_year, bill.settlement_month, bill.type)
#zmianione
    for tenant in manager.tenants.values():
        print(tenant.name, tenant.apartment, tenant.room, tenant.rent_pln, tenant.deposit_pln, tenant.date_agreement_from, tenant.date_agreement_to)
        for transfer in manager.transfers:
            if transfer.tenant == tenant.name:
                print('  ', transfer.amount_pln, transfer.date, transfer.settlement_year, transfer.settlement_month)