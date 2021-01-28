using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Console_App
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter a number: ");
            double num1 = Convert.ToDouble(Console.ReadLine());

            Console.Write("Enter Operator: ");
            string op = Console.ReadLine();

            Console.Write("Enter another number: ");
            double num2 = Convert.ToDouble(Console.ReadLine());

            if (op == "+")
            {
                double answer = num1 + num2;
                Console.WriteLine($"Answer: {answer}");
            }

            else if (op == "-")
            {
                double answer = num1 - num2;
                Console.WriteLine($"Answer: {answer}");
            }

            else if (op == "*")
            {
                double answer = num1 * num2;
                Console.WriteLine($"Answer: {answer}");
            }

            else if (op == "/")
            {
                if (num2 == 0.0) 
                {
                    Console.WriteLine("ERROR: Zero Division Error");
                }

                else 
                {
                    double answer = num1 / num2;
                Console.WriteLine($"Answer: {answer}");
                }
            }

            else
            {
                Console.WriteLine("ERROR: Invalid Operator");
            }

            Console.ReadLine();
        }
    }
}
