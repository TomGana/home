import qiskit as q

circuit = q.QuantumCircuit(2,2) #(qbits, bits)
#(0,0)
circuit.x(0) #(1,0)
circuit.cx(0,1) #cnot, flips 2nd qbit if first qbit is a 1
#(1,1)
circuit.measure([0,1], [0,1]) #map to bit

circuit.draw()
