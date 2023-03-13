from copy import copy


def get_power_dispatch(data):
    data = dict(data)
    powerplants = copy(data["powerplants"])
    fuels = copy(data["fuels"])
    load = copy(data["load"])

    # Get the corresponding cost for each power plant
    plant_cost = {
        'gasfired': fuels['gas(euro/MWh)'],
        'turbojet': fuels['kerosine(euro/MWh)'],
        'windturbine': fuels['wind(%)']
    }
    plants = []

    # Sort the powerplants by merit order
    for powerplant in powerplants:
        plant = copy(powerplant)
        if 'wind' in plant['name']:
            plant['pmax'] *= plant_cost[plant['type']]/100
            plant['variable_cost'] = 0
        else:
            plant['variable_cost'] = plant_cost[plant['type']] / \
                max(plant['efficiency'], 0) + 1
        plants.append(plant)

    # Sort first by variable cost then by power range
    sorted_plants = sorted(plants, key=lambda x: (
        x['variable_cost'], max(x['pmin'], 0)/(max(x['pmax'], 0) + 1)))
    dispached_power = dict([(plant['name'],  0) for plant in sorted_plants])

    remaining_load = copy(load)
    for plant in sorted_plants:

        capacity = round(min(plant['pmax'], remaining_load), 1)  # round to 0.1

        if capacity >= plant['pmin'] or \
                (remaining_load - plant['pmin']) < 0:
            dispached_power[plant['name']] = capacity
            remaining_load -= capacity

        else:
            dispached_power[plant['name']] = plant['pmin']
            remaining_load -= plant['pmin']

        if remaining_load <= 0:
            break

    return [{'name': plant_name, 'p': power}
            for plant_name, power in dispached_power.items()]
