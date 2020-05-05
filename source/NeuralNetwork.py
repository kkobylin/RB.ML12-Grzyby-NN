import numpy as np
import source.Neuron as Neuron


class NeuralNetwork:
    def __init__(self, inputs, size, outputs):
        self.sizes = size  # for set_weights_one()
        self.input = np.zeros((inputs, 1))
        self.neurons = []
        self.hidden_layers = len(size)
        self.output = np.zeros((outputs, 1))
        self.weights = []
        if self.hidden_layers == 0:
            self.weights.append(np.random.rand(outputs, inputs))
        else:
            self.weights.append(np.random.rand(size[0], inputs))
            for i in range(1, self.hidden_layers):
                self.weights.append(np.random.rand(size[i], size[i - 1]))
            self.weights.append(np.random.rand(outputs, size[self.hidden_layers-1]))

    def calculate_output(self, vec):
        self.neurons = []
        self.fill_input(vec)
        layers_neuron = NeuralNetwork.calculate_layer(self.weights[0], self.input)
        self.neurons.append(layers_neuron)
        for i in range(self.hidden_layers):
            layers_neuron = NeuralNetwork.calculate_layer(self.weights[i+1], self.neurons[i])
            self.neurons.append(layers_neuron)
        self.output = self.neurons[self.hidden_layers]
        return self.output

    def fill_input(self, vec):
        for i in range(len(vec)):
            self.input[i] = vec[i]

    @staticmethod
    def calculate_layer(layer, weights):
        layer_values = np.dot(layer, weights)
        layer_output = Neuron.Neuron.calculate_value(layer_values)
        return layer_output

    def set_weights_one(self):
        self.weights = []
        if self.hidden_layers == 0:
            self.weights.append(np.ones((self.output.size, self.input.size)))
        else:
            self.weights.append(np.ones((self.sizes[0], self.input.size)))
            for i in range(1, self.hidden_layers):
                self.weights.append(np.ones((self.sizes[i], self.sizes[i - 1])))
            self.weights.append(np.ones((self.output.size, self.sizes[self.hidden_layers - 1])))