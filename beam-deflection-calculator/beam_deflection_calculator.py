# beam_deflection_calculator.py

def point_load_deflection(P, a, L, E, I):
    return (P * a**2 * (3 * L - a)) / (6 * E * I)

def distributed_load_deflection(w, L, E, I):
    return (5 * w * L**4) / (384 * E * I)

if __name__ == "__main__":
    print("This is a simple beam deflection calculator.")
