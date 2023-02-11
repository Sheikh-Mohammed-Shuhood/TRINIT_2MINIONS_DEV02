def energy_per_visit(new_visitors_data, returning_visitors_data):
    new_visitors_energy = new_visitors_data * 0.81 * 0.75
    returning_visitors_energy = returning_visitors_data * 0.81 * 0.25 * 0.02
    return new_visitors_energy + returning_visitors_energy
