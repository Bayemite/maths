# Part A - Proof Assignment
## Question 1 - Complex Number Proofs

Prove the following identities. These are required proofs for this course.  
Let $z_1 = a + bi = r_1(\cos\theta + i\sin\theta)$
and $z_2 = c + di = r_2(\cos\phi   +  i\sin\phi )$.  
Note: you may wish to write both $z_1$ and $z_2$ in exponential form.

**(i)**
$|z_1 z_2| = |z_1||z_2|$

In exponential form:  
$z_1 = r_1e^{i\theta}$                      
$z_2 = r_2e^{i\phi}  $
$\begin{aligned}
LHS &= |r_1e^{i\theta}r_2e^{i\phi}|     \\
    &= |r_1r_2e^{i(\theta+\phi)}|       \\
    &= r_1r_2                           \\
    &= |z_1||z_2|                       \\
    &= RHS                              \\
\end{aligned}$   

**(ii)**
$\arg(z_1z_2) = \arg z_1 \arg z_2$

**(iii)**
$|\dfrac{z_1}{z_2}| = \dfrac{|z_1|}{|z_2|}$

**(iv)**
$\arg(\dfrac{z_1}{z_2}) = \arg z_1-\arg z_2$

**(v)**
$|z^n_1| = |z_1|^n$

**(vi)**
$\arg(z^n_1) = n\arg z_1$

**(vii)**
$\overline{z_1} + \overline{z_2} = \overline{z_1+z_2}$

**(viii)**
$\overline{z_1} * \overline{z_2} = \overline{z_1z_2}$

**(ix)**
$z_1\overline{z_1} = |z_1|^2$

**(x)**
$z_1 + \overline{z_1} = 2Re(z)$

Prove Euler's formula, that is, $\cos x+i\sin x=e^{ix}$ 
and hence evalulate $e^{i\pi}$ (known as Euler's identity).