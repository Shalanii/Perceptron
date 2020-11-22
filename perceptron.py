def train_model():
    inputs =  [[5.12522945, 4.97589132],
 [5.14752398, 5.42175877],
 [5.2513868,  5.08566492],
 [4.57122775, 4.86186423],
 [4.98125856, 5.10089702],
 [6.26065265, 6.80349543],
 [6.79955078, 6.32344424],
 [6.92706257, 6.76088356],
 [6.89584227, 6.54362606],
 [6.51892616, 6.5735943 ]]
    
    weights = [0,0]
    targets = [0, 0, 0, 0, 0, 1, 1, 1, 1,  1]
    bias = 0
    alpha = 0.1
    predicted_output = 0
    desired_output = 0
    output_list = []
    if(len(inputs)!=len(targets)):
        print("Error : Number of outputs does not match with the number of inputs.")

    else:
        for i in range(0,len(targets)):
            for j in range(0,len(targets)):
                list1 = []
                hx = vector_multiplication(inputs[j],weights)+bias

                if hx<0:
                    predicted_output = 0
                else:
                    predicted_output = 1
               
                if predicted_output==0 and targets[j]==1:
                    bias = bias+alpha
                    for i in range(0,len(inputs[0])):
                        list1.append(weights[i]+(alpha*inputs[j][i]))
                    weights = list1
                elif predicted_output==1 and targets[j]==0:
                    bias = bias-alpha
                    for i in range(0,len(inputs[0])):
                        list1.append(weights[i]-(alpha*inputs[j][i]))
                    weights = list1
                
                    
        print("== Trained Model ==\nBIAS  " + str(bias) +"  Weights  " + str(weights))
        output_list = [bias,weights]
        return output_list

def test_model(test_outputs):
    print("== Testing Model ==")
    vector_size = len(test_outputs[1])
    inputs = []
    for i in range(0,vector_size):
        v1 = float (input("Enter test input value "+str(i+1)+":  " ))
        inputs.append(v1)
    bias = test_outputs[0]
    hx = vector_multiplication(inputs,test_outputs[1])+bias
    if hx<0:
        output_value = 0
    else:
        output_value = 1
    print("Output is "+str(output_value))
    return output_value

def vector_multiplication(vector1,vector2):
    summ = 0
    if(len(vector1)!=len(vector2)):
        print("ERROR : Given vectors cannot be multiplied!")

    else:
        for i in range(len(vector1)):
            summ = summ + vector1[i]*vector2[i]
    return summ
        
if __name__ == "__main__":
    outputs = train_model()
    test_model(outputs)
    

