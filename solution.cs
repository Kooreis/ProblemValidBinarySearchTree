```C#
using System;

public class Node
{
    public int Value;
    public Node Left;
    public Node Right;

    public Node(int value, Node left = null, Node right = null)
    {
        Value = value;
        Left = left;
        Right = right;
    }
}

public class Program
{
    public static void Main()
    {
        Node root = new Node(10);
        root.Left = new Node(5);
        root.Right = new Node(15);
        root.Right.Left = new Node(12);
        root.Right.Right = new Node(20);

        Console.WriteLine(IsBinarySearchTree(root));
    }

    public static bool IsBinarySearchTree(Node root, int min = int.MinValue, int max = int.MaxValue)
    {
        if (root == null)
        {
            return true;
        }

        if (root.Value < min || root.Value > max)
        {
            return false;
        }

        return IsBinarySearchTree(root.Left, min, root.Value - 1) && IsBinarySearchTree(root.Right, root.Value + 1, max);
    }
}
```