using System;
using System.CodeDom.Compiler;
using System.Collections;
using System.Collections.Generic;
using System.Security.AccessControl;

public class Neuron{
	
    List<Node> nodes;
    double[] targets;
    double w1;
    double w2;
    double threshold=0.5;
    public Neuron(){
        this.nodes=createTrainNodes();
        this.targets=new double[] {1,1,-1,-1,1,1,-1,-1};
        this.w1 = -0.4;
        this.w2 = 0.2;
    }
    public double function(double x1,double x2,double w1,double w2){
        double result;
        if((x1*w1 + x2*w2)<threshold){
            result=-1;
        }
        else{
            result=1;
        }
        return result;
			
    }

    public double optimizeWeight(double t, double o,double  w,double x)
    {
        double lambda = 0.05;
        return w + (lambda * (t - o) * x);
    }

    public double trainModel(int epoch){
        int ep=epoch;
        double[] results = new double[8];
        for(int i=0;i<ep;i++){
            int targetIndex=0;
            foreach(Node var in nodes)
            {
                
                double output = function(var.x1, var.x2, w1, w2);
                if(output!=targets[targetIndex]){
                    /*Console.WriteLine(w1);
                    Console.WriteLine(var.x1);
                    Console.WriteLine(output);
                    Console.WriteLine(targets[targetIndex]);
                    Console.WriteLine("-----------");*/
                    w1=optimizeWeight(targets[targetIndex],output,w1,var.x1);
                    w2=optimizeWeight(targets[targetIndex],output,w2,var.x2);
                   
                }
                results[targetIndex] = output;
                targetIndex++;
            }
        }

        int trueRes = 0;
        int index = 0;
        foreach (int i in results){

            if (i == targets[index])
            {
                trueRes++;
            }

            index++;
        }
        Console.WriteLine(w1);
        Console.WriteLine(w2);
        
        return Convert.ToDouble(trueRes) / 8;
    }
    public List<Node> createTrainNodes(){
        List<Node> nodes = new List<Node>();
        int[,] trainValsBefore={{6,5},{2,4},{-3,-5},{-1,-1},{1,1},{-2,7},{-4,-2},{-6,3}};
        for(int i=0;i<8;i++)
        {
       
            nodes.Add(new Node(Convert.ToDouble(trainValsBefore[i,0])/10, Convert.ToDouble(trainValsBefore[i,1])/10));
        }

      
        return nodes;
		
    }

   
    static public void Main(String[] args)
    {

        Neuron n = new Neuron();
        Console.WriteLine("Accuracy for epoch 5:");
        Console.WriteLine(n.trainModel(5));
        Console.WriteLine("-------------");
        Console.WriteLine("Accuracy for epoch 10:");
        Console.WriteLine(n.trainModel(10));
        Console.WriteLine("-------------");
        Console.WriteLine("Accuracy for epoch 100:");
        Console.WriteLine(n.trainModel(100));
        Console.WriteLine("-------------");
        //----------TEST-------------
        n.nodes=new List<Node>{new Node(1, 2),new Node(-2, -3),new Node(-2, 4),new Node(-4, 3),new Node(4, 1)}
        ;
        n.targets = new double[] {1, -1, 1, -1, 1};
        int trueRess = 0;
        int i = 0;
        foreach (Node nn in n.nodes)
        {
            double result=n.function(nn.x1, nn.x2, n.w1, n.w2);
            if (result == n.targets[i])
            {
                trueRess++;
                i++;
            }
        }
        Console.Write("Test Accuracy:");
        Console.WriteLine(Convert.ToDouble(trueRess)/5);
    }
    /*double randfrom(double min, double max) 
    {
        double range = (max - min); 
        double div = RAND_MAX / range;
        return min + (rand() / div);
    }*/
}
public class Node{
    public double x1;
    public double x2;
    public Node(double x1,double x2){
        this.x1=x1;
        this.x2=x2;
    }
}
