import numpy as np
from qiskit import (IBMQ, QuantumCircuit, circuit, execute, Aer)

IBM_TOKEN = "ede8866d65d89e2f9d58aa2f77bae0ddcf1697ca47e3642a607391858bcf96e7dd8d5df68589de250c8294142e88c1089d4eef80afcf64ca58c2f2394c6ac3c9"

IBMQ.save_account(IBM_TOKEN, overwrite=True)

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)

# Add a H gate on qubit 0
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)

# Map the quantum measurement to the classical bits
circuit.measure([0, 1], [0, 1])

# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:", counts)

# Draw the circuit
circuit.draw()
