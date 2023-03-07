# Part A - Proof Assignment

## Question 1 - Complex Number Proofs

**(a)**
Prove the following identities. These are required proofs for this course.  
Let $z_1 = a + bi = r_1(\cos\theta + i\sin\theta)$
and $z_2 = c + di = r_2(\cos\phi   +  i\sin\phi )$.  
Note: you may wish to write both $z_1$ and $z_2$ in exponential form.

**(a.i)** $|z_1 z_2| = |z_1||z_2|$

In exponential form:  
$z_1 = r_1e^{i\theta}               $  
$z_2 = r_2e^{i\phi}                 $  
$LHS = |r_1e^{i\theta}r_2e^{i\phi}| $  
$= |r_1r_2e^{i(\theta+\phi)}|       $  
$= r_1r_2                           $  
$= |z_1||z_2|                       $  
$= RHS                              $  

**(a.ii)** $\arg(z_1z_2) = \arg z_1 \arg z_2$

**(a.iii)** $|\dfrac{z_1}{z_2}| = \dfrac{|z_1|}{|z_2|}$

**(a.iv)** $\arg(\dfrac{z_1}{z_2}) = \arg z_1-\arg z_2$

**(a.v)** $|z^n_1| = |z_1|^n$

**(a.vi)** $\arg(z^n_1) = n\arg z_1$

**(a.vii)** $\overline{z_1} + \overline{z_2} = \overline{z_1+z_2}$

**(a.viii)** $\overline{z_1} * \overline{z_2} = \overline{z_1z_2}$

**(a.ix)** $z_1\overline{z_1} = |z_1|^2$

**(a.x)** $z_1 + \overline{z_1} = 2Re(z)$

**(b)**
Prove Euler's formula, that is, $\cos x+i\sin x=e^{ix}$ 
and hence evalulate $e^{i\pi}$ (known as Euler's identity).

## Question 2 - Proof Techniques
Using any of the proof techniques we hav ecovered, prove the following statements.  
Clearly state which method you are using.

**(a)** The product of two consecutive even counting numbers is a multiple of 4.

**(b)** $\forall a,b\in \mathbb{Z}, a^2 = b^2,$ then $a = b$.

**(c)** There exists a number which is half the sum of its positive factors.

**(d)** The number $\sqrt{5}$ is irrational.

**(e)** Within any group of $n\geq 2$ people, there are at least two people who have met with the same number of people.

## Question 3 - The Triangle Inequality

**(a)** State the triangle inequality both in words and using mathematical symbols.

**(b)** Prove the triangle inequality using two different methods. You are encouraged to research this.
Include references to any sources you used.

**(c)** Summarise each of the proofs from **(b)** and highlight the similarities and differences between the two proofs.

**(d)** Which method do you prefer, and why?

## Question 4 - Quadrilateral and Polygon Properties

**(a.i)** Prove that the axis of a kite is the perpendicular bisector of the other diagonal.

**(a.ii)** Demonstrate this using Geogebra or similar technology.

**(b.i)** Prove, by mathematical induction, 
that the interior angle sum of an *n*-gon is equal to $(n-2) \times 180$ degrees for all integers, $n \geq 3$.

**(b.ii)** Hence prove that the exterior angle sum of an *n*-gon is $360\degree$.

**(c)**
Suppose we draw on a plane *n* lines in 'general position', i.e. with no three concurrent and no two parallel.  
Let $S_n$ be the number of regions into which these lines divide the plane, for example $S_3=7$ in the following diagram:

![3 lines, 7 section graph](s_3.svg)

**(c.i)** By drawing diagrams, find $S_1, S_2, S_3, S_4$ and $S_5$.

![S_1 graph](s_1.svg)

**(c.ii)** From these results, make a conjecture about a formula for $S_n$.

**(c.iii)** Prove this formula by mathematical induction.