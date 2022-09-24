from openvino.inference_engine import IECore

xml = 'model/saved_model.xml'
bin = 'model/saved_model.bin'
ie = IECore()
network = ie.read_network(xml, bin)