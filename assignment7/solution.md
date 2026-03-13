# Assignment 7

## Exercise 1
a) A case primarily consists of a specific problem description and its corresponding solution. In many advanced systems, a case also includes the evaluation outcome and an explanation or justification of exactly how that solution was reached.


b) The main processes are Retrieve, Reuse, Revise and Retain. In Retrieve, the system looks for the most similar cases. During Reuse, the retrieved case is adjusted to suggest a solution. In Revise, the proposed solution is evaluated. Finally, in Retain, the new experience is saved for future use.

## Exercise 2
a) An application could be a meal planning assistant. The task of the system is to recommend a cooking recipe based on the ingredients a user currently has in their kitchen.

b) The case representation includes the main ingredient, secondary ingredients, dietary restrictions, cooking time, and the specific recipe provided as the solution.

c) A similarity function for the main ingredient attribute yields 1 for an exact match, 0.5 for an ingredient in the same food group, and 0 for completely different foods.

## Exercise 3
|  | Vocabulary | Case Base | Similarity | Adaptation |
| :--- | :--- | :--- | :--- | :--- |
| **Retrieve** | Specifies the language used to represent the problem. | Acts as the repository searched for similar past cases. | Guides the retrieval of experiences most similar to the target problem. | Not primarily used in this step. |
| **Reuse** | Specifies the language used to represent the proposed solution. | Provides the retrieved cases to be utilized. | Not primarily used in this step. | Modifies the retrieved solution to address the new target problem. |
| **Revise** | Represents the evaluation and repaired knowledge. | Provides the original proposed solution for domain expert review. | Not primarily used in this step. | Explains and repairs failures in the proposed solution. |
| **Retain** | Can be revised as the system learns and evolves. | Retains the new case if it is deemed useful. | Can be updated as knowledge shifts during system evolution. | Can be updated as knowledge shifts during system evolution. |