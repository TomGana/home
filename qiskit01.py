import qiskit as q

circuit = q.QuantumCircuit(2,2) #(qbits, bits)
#(0,0)
circuit.x(0) #(1,0)
circuit.cx(0,1) #cnot, flips 2nd qbit if first qbit is a 1
#(1,1)
circuit.measure([0,1], [0,1]) #map to bit

circuit.draw()

#circuit.draw(output='mpl')

from qiskit import IBMQ

#IBMQ.save_account("b3bb883ac33e8faef5af38947e19a659b7ec8a265cba863a3c1a667c72d8826b34d19b3ec3d312109b0ed7edbe416bb5fb069b979db02b45e7d04fc0fb919941")
IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')
for backend in provider.backends():
    try:
        qubit_count = len(backend.properties().qubits)
    except:
        qubit_count = "simulated"

    print(f"{backend.name()} has {backend.status().pending_jobs} queued and {qubit_count} qubits")
