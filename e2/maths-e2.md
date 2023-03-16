# Part A - Proof Assignment

## Question 1 - Complex Number Proofs

**(a)**
Prove the following identities. These are required proofs for this course.  
Let $z_1 = a + bi = r_1(\cos\theta + i\sin\theta)$
and $z_2 = c + di = r_2(\cos\phi   +  i\sin\phi )$.  
Note: you may wish to write both $z_1$ and $z_2$ in exponential form.

In exponential form:  
$z_1 = r_1e^{i\theta} $  
$z_2 = r_2e^{i\phi}   $

**(a.i)**  $|z_1 z_2| = |z_1||z_2|  $  
$LHS = |r_1e^{i\theta}r_2e^{i\phi}| $  
$= |r_1r_2e^{i(\theta+\phi)}|       $  
$= r_1r_2                           $  
$= |z_1||z_2|                       $  
$= RHS                              $

**(a.ii)** $\arg(z_1z_2) = \arg z_1+\arg z_2$  
$LHS = \arg(r_1e^{i\theta}r_2e^{i\phi})     $  
$= \theta+\phi                              $  
$= RHS                                      $  


**(a.iii)** $\left|\dfrac{z_1}{z_2}\right| = \dfrac{|z_1|}{|z_2|}$  
$LHS = \left|\dfrac{r_1e^{i\theta}}{r_2e^{i\phi}} \right|   $  
$= \left|\dfrac{r_1}{r_2}e^{i(\theta-\phi)} \right|         $  
$= \dfrac{r_1}{r_2}                                         $  
$= RHS                                                      $

**(a.iv)** $\arg\left(\dfrac{z_1}{z_2}\right) = \arg z_1-\arg z_2  $  

$LHS = \arg\left(\dfrac{r_1e^{i\theta}}{r_2e^{i\phi}}\right)       $  

$= \arg\left(\dfrac{r_1}{r_2}e^{i(\theta - \phi)}\right)           $  
$= \theta-\phi  $  
$= RHS          $

**(a.v)** $|z^n_1| = |z_1|^n$  
$LHS = |(r_1e^{i\theta})^n| $  
$= r_1^n                    $  
$= RHS                      $  

**(a.vi)** $\arg(z^n_1) = n\arg z_1 $  
$LHS = \arg((r_1e^{i\theta})^n)     $  
$= n\theta                          $  
$= RHS                              $

**(a.vii)** $\overline{z_1} + \overline{z_2} = \overline{z_1+z_2}$  
$LHS = a-bi + c-di          $  
$RHS = \overline{a+c+bi+di} $  
$= \overline{a+c+i(b+d)}    $  
$= a+c-i(b+d)               $  
$= a+c-bi-di                $  
$= LHS                      $

**(a.viii)** $\overline{z_1} \times \overline{z_2} = \overline{z_1z_2}$  
$LHS = (a-bi)(c-di) $  
$= ac-adi-cbi+bdi^2 $  
$= ac-adi-cbi-bd    $  
$= ac-bd-i(ad+cb)   $  
$RHS = \overline{(a+bi)(c+di)}       $  
$= \overline{ac + adi + cbi + bdi^2} $  
$= \overline{ac- bd + i(ad + cb)}    $  
$= ac - bd - i(ad + cb)              $  
$= RHS                               $

**(a.ix)** $z_1\overline{z_1} = |z_1|^2$  
$LHS = (a+bi)(a-bi)       $
$= a^2-(bi)^2             $  
$= a^2+b^2                $  
$RHS = \left(\sqrt{a^2+(b)^2}\right)^2 $  
$= LHS                    $

**(a.x)** $z_1 + \overline{z_1} = 2Re(z)$  
$LHS = a+bi+a-bi $  
$= 2a            $  
$= RHS           $

**(b)**
Prove Euler's formula, that is, $\cos x+i\sin x=e^{ix}$
and hence evalulate $e^{i\pi}$ (known as Euler's identity).  

$f(x)=\dfrac{\cos x+i\sin x}{e^{ix}} $  
$= e^{-i x}(\cos x+i\sin x)          $  
$f'(x)=-ie^{-ix}(\cos x+i\sin x)     $
$+ e^{-ix}(i\cos x-\sin x)           $  
$= -e^{-ix}(i\cos x-\sin x)          $
$+ e^{-ix}(i\cos x-\sin x)           $  
$= 0$  
Therefore $f(x)$ is a constant.  
$f(0) = 1$, meaning that $f(x) = 1$  

Therefore,  
$1 = \dfrac{\cos x+i\sin x}{e^{ix}}$  
$e^{ix} = \cos x+i\sin x$

Hence, $e^{i\pi} = \cos\pi + i\sin\pi = -1$

---

## Question 2 - Proof Techniques
Using any of the proof techniques we have covered, prove the following statements.  
Clearly state which method you are using.

**(a)** The product of two consecutive even counting numbers is a multiple of 4.  
By direct proof:  
RTP: $2n(2n + 2) = 4M$, where $n, M \in\mathbb{Z} $  
$LHS = 4n^2 + 4n $  
$= 4(n^2 + n)    $  
$= RHS           $

**(b)** $\forall a,b\in \mathbb{Z}, a^2 = b^2,$ then $a = b$.  
By direct proof:  
$a^2 = b^2$  
$\pm a = \pm b$  

**(c)** There exists a number which is half the sum of its positive factors.  
Proof by example: 6 is such a number.  
$1 + 2 + 3 + 6 = 12$

**(d)** The number $\sqrt{5}$ is irrational.  
Proof by contradiction:  
$\sqrt{5} = \dfrac{a}{b}$, where $a, b \in\mathbb{Z}$ and are co-prime.

$5 = \left(\dfrac{a}{b}\right)^2 $  
$5b^2 = a^2                      $  
Therefore, both $a^2$ and $a$ are divisible by 5.  
Let $a = 5k, k \in\mathbb{Z} $  
$5b^2 = (5k)^2               $  
$b^2 = 5k^2                  $  
Therefore $b$ is divisible by 5, which is a contradiction 
as $\dfrac{a}{b}$ is meant to be in simplest form.  
This is a problem because this implies there are an infinite set of decreasing integer pairs
that represent the equivalent fraction, which is impossible.

$\therefore\sqrt{5}$ is irrational by contradiction.

**(e)** Within any group of $n\geq 2$ people, there are at least two people who have met with the same number of people.  
There are a maximum of $n-1$ people to meet, as meeting yourself is not counted.  
As according to the pigeon-hole principle, this means there will always be at least $2$ people who have met
the same number of people.

---

## Question 3 - The Triangle Inequality

**(a)** State the triangle inequality both in words and using mathematical symbols.  
The triangle inequality states that for any triangle,
the length sum of any two sides will be greater than that of the third side.  
$z \leq x + y$, where $x, y, z$ are the side lengths of a triangle.  

Or: $|x+y|\geq |x| + |y|$

**(b)** Prove the triangle inequality using two different methods. You are encouraged to research this.
Include references to any sources you used.

**Proof 1**:  
Property of absolute values:  
$x \leq |x|$ and $y \leq |y|$  
Therefore:  
$x+y \leq |x|+|y|$

**(c)** Summarise each of the proofs from **(b)** and highlight the similarities and differences between the two proofs.

**(d)** Which method do you prefer, and why?

---

## Question 4 - Quadrilateral and Polygon Properties

**(a.i)** Prove that the axis of a kite is the perpendicular bisector of the other diagonal.  
Definition of a kite:
A quadrilateral that has 2 pairs of equal-length sides and these sides are adjacent to each other.

(See graph in question **a.ii**)  
Let $AC$ and $BD$ cross at $E$.  
$AB=CB, AD=CD, BD$ is common.  
$\therefore△ABD\equiv△CBD$ (SSS $△$ equivalence)

$\angle{ABE}=\angle{CBE}, AB = CB, BE$ is common.  
$\therefore△ABE\equiv△CBE$ (SSA $△$ equivalence)  
From this congruence: $\angle BEC=\angle BEA$  
Because these two angles are on a straight line and are equal,
they are both $90\degree$ (supplementary angles).

Therefore $AC$ is perpendicular to $BD$.  
$AE$ and $AC$ are equal, because $△ABE\equiv△CBE, AB=BC, BE$ is common.  
Therefore $AC$ bisects, and is perpendicular, to $BD$.

**(a.ii)** Demonstrate this using Geogebra or similar technology.

![Kite graph](kite.svg)

Black line has length of 2 on either side of the bisecting orange line.

**(b.i)** Prove, by mathematical induction, 
that the interior angle sum of an *n*-gon is equal to $(n-2) \times 180$ degrees for all integers, $n \geq 3$.

Required to prove: 
angle sum $= (n-2)\times180\degree$.

Prove for the first case ($n=3$):  
$LHS = 180\degree$ (angle sum of a triangle)  
$RHS = (3-2)\times180 = 180\degree$  
$= LHS$

Assume true for $n=k$:  
$(k-2)\times 180\degree$

Prove for $n=k+1$:  


**(b.ii)** Hence prove that the exterior angle sum of an *n*-gon is $360\degree$.

**(c)**
Suppose we draw on a plane *n* lines in 'general position', i.e. with no three concurrent and no two parallel.  
Let $S_n$ be the number of regions into which these lines divide the plane.

**(c.i)** By drawing diagrams, find $S_1, S_2, S_3, S_4$ and $S_5$.

![s_1 graph](s_1.svg)  
![s_2 graph](s_2.svg)  
![s_3 graph](s_3.svg)  
![s_4 graph](s_4.svg)  
![s_5 graph](s_5.svg)

$S_1 = 2, S_2 = 4, S_3 = 7, S_4 = 11, S_5 = 16$

**(c.ii)** From these results, make a conjecture about a formula for $S_n$.  
$S_n = n + S_{n-1}   $  
$= n + (n-1+S_{n-2}) $

**(c.iii)** Prove this formula by mathematical induction.  
The first case, $n = 1$, is true:  
$LHS = 2$   
$RHS = 1 + S_0 = 2$ (as $S_0 = 0$)  
$= LHS$

Assume $n = k$ is true:  
$S_k = k + S_{k-1}$

Prove true for $n = k+1$:  
$RTP: S_{k+1} = k+1 + S_k    $  
$RHS = k + 1 + (k + S_{k-1}) $

<style>
    img{border: 1px solid #c8ccd1; max-height: 50vh;}
</style>