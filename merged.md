# Antiderivatives and Indefinite Integrals

## Introduction
Antiderivatives and indefinite integrals are foundational concepts in calculus, crucial for understanding areas under curves and solving differential equations. These concepts are closely related, yet distinct, in their applications and interpretations.

### Antiderivatives
An antiderivative of a function $f(x)$ is a function $F(x)$ whose derivative is $f(x)$. In other words, $F'(x) = f(x)$. The process of finding antiderivatives is often called anti-differentiation.

### Indefinite Integrals
The indefinite integral of $f(x)$ with respect to $x$ is a collection of all its antiderivatives and is denoted as $\int f(x) \, dx$. It includes a constant of integration, $C$, because the derivative of a constant is zero.

## Relation between Antiderivatives and Indefinite Integrals
The Fundamental Theorem of Calculus bridges the concept of antiderivatives and integrals. It states that if $F$ is an antiderivative of $f$ on an interval $I$, then $\int f(x) \, dx = F(x) + C$ for all $x$ in $I$.

## Examples
1. **Linear Functions:** If $f(x) = ax + b$, an antiderivative is $F(x) = \frac{1}{2}ax^2 + bx + C$.
2. **Exponential Functions:** For $f(x) = e^x$, the antiderivative is $F(x) = e^x + C$.

## Applications
1. **Area under Curves:** Indefinite integrals are used to calculate the area under curves.
2. **Solving Differential Equations:** Antiderivatives are key in solving ordinary differential equations.

## Test Questions
1. STARTI [Basic] Question: What is the antiderivative of $3x^2$? Back: The antiderivative of $3x^2$ is $x^3 + C$, where $C$ is the constant of integration. ENDI
2. STARTI [Basic] Question: Compute the indefinite integral of $\sin x$. Back: The indefinite integral of $\sin x$ is $-\cos x + C$. ENDI
3. STARTI [Basic] Question: If $F(x)$ is an antiderivative of $f(x)$, what is $\int (f(x) + 5) \, dx$? Back: $\int (f(x) + 5) \, dx = F(x) + 5x + C$. ENDI

For further reading and examples, you can explore resources linked under [[Calculus Resources]] and [[Integration Techniques]].

# Note on Arc Length in Polar Coordinates

## Introduction
Arc length in polar coordinates is a fascinating concept in mathematics, particularly useful in calculus and analytical geometry. Unlike rectangular coordinates, where x and y denote the horizontal and vertical distances respectively, polar coordinates use a radius and an angle to define the position of a point. This system is especially handy for dealing with curves that are symmetrical about a point, like circles and spirals.

## Polar Coordinates Basics
In polar coordinates, a point in the plane is represented by $(r, \theta)$, where:
- $r$ is the radial distance from the origin,
- $\theta$ is the angle formed with the positive x-axis.

## Arc Length Formula in Polar Coordinates
To find the length of a curve defined in polar coordinates from $\theta = a$ to $\theta = b$, the formula is:

$$
L = \int_{a}^{b} \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2} \, d\theta
$$

Here, $r$ is a function of $\theta$, and $\frac{dr}{d\theta}$ is its derivative with respect to $\theta$.

## Example
Consider the curve given by $r(\theta) = 2\theta$ from $\theta = 0$ to $\theta = \pi$.

1. First, find $\frac{dr}{d\theta}$: Given $r(\theta) = 2\theta$, $\frac{dr}{d\theta} = 2$.
2. Next, substitute into the arc length formula:

$$
L = \int_{0}^{\pi} \sqrt{(2\theta)^2 + 2^2} \, d\theta
$$

3. Solve the integral to find the arc length.

## Historical Context
The concept of polar coordinates can be traced back to the works of Isaac Newton and Jacob Bernoulli in the 17th century. It was further developed and popularized by Gregorio Fontana and Alexis Clairaut in the 18th century.

## Conclusion
Understanding arc length in polar coordinates not only deepens one's knowledge in geometry and calculus but also paves the way for exploring more complex curves and shapes in advanced mathematics.

## Test Questions
1. STARTI [Basic] Question: What is the basic formula for calculating arc length in polar coordinates? Back: $L = \int_{a}^{b} \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2} \, d\theta$. ENDI
2. STARTI [Basic] Question: Calculate the arc length for the curve $r(\theta) = \theta^2$ from $\theta = 0$ to $\theta = 2$. Back: Use the formula with appropriate limits and solve the integral. ENDI
3. STARTI [Basic] Question: How does the concept of arc length in polar coordinates differ from that in Cartesian coordinates? Back: In polar coordinates, the arc length accounts for the radial distance and angular change, whereas in Cartesian coordinates, it's based on horizontal and vertical distances. ENDI

# Areas in Polar Coordinates

## Introduction
Polar coordinates offer a unique and effective way to represent points in a plane using a radius and an angle, rather than x and y coordinates. This system is especially useful for analyzing curves and shapes that exhibit radial symmetry or are centered around a point. In this context, calculating areas in polar coordinates becomes an essential skill in mathematics, particularly in calculus and analytical geometry.

## Basics of Polar Coordinates
- **Polar Coordinates:** A point in the polar coordinate system is represented by $(r, \theta)$, where $r$ is the radius - the distance from the origin, and $\theta$ is the angle measured from the positive x-axis.
- **Conversion to Cartesian Coordinates:** A point $(r, \theta)$ in polar coordinates can be converted to Cartesian coordinates $(x, y)$ using $x = r \cos(\theta)$ and $y = r \sin(\theta)$.

## Area Calculation
The area $A$ enclosed by a curve in polar coordinates can be found using the integral:

$$A = \frac{1}{2} \int_{\alpha}^{\beta} r(\theta)^2 d\theta$$

where $r(\theta)$ is the polar equation of the curve, and $\alpha$ and $\beta$ are the limits of integration, representing the angles over which the curve extends.

## Example
Consider a simple polar curve, such as a circle with radius $a$, represented by the equation $r(\theta) = a$. To find the area of the entire circle, integrate from $0$ to $2\pi$:

$$A = \frac{1}{2} \int_{0}^{2\pi} a^2 d\theta$$
$$= \frac{a^2}{2} [ \theta ]_{0}^{2\pi}$$
$$= \pi a^2$$

This result confirms the well-known formula for the area of a circle.

## Historical Context
Polar coordinates were first introduced by Gregorio Fontana and further developed by Euler and Bernoulli in the 18th century. They were instrumental in advancing fields like astronomy, physics, and later, complex number analysis.

## Conclusion
Understanding areas in polar coordinates is crucial for tackling problems involving curves and shapes that are not easily addressed with Cartesian coordinates. This method is particularly effective for dealing with circular and spiral shapes, often encountered in physics and engineering.

## Test Questions
1. **Question:** If $r(\theta) = 2\sin(\theta)$, what is the area enclosed by one petal of the rose curve? **Back:** Use the integral $\frac{1}{2} \int_{0}^{\pi} (2\sin(\theta))^2 d\theta$.
2. **Question:** How would you convert the polar coordinate $(5, \frac{\pi}{3})$ to Cartesian coordinates? **Back:** $(x, y) = (5 \cos(\frac{\pi}{3}), 5 \sin(\frac{\pi}{3}))$.
3. **Question:** What is the area of a sector with radius 4 and central angle $\frac{\pi}{4}$ in polar coordinates? **Back:** $\frac{1}{2} \times 4^2 \times \frac{\pi}{4} = 2\pi$.

[[Calculus]] | [[Analytical Geometry]] | [[Polar Coordinates]]

# Argand Diagrams

## Introduction
Argand diagrams, named after Jean-Robert Argand, are a way to represent complex numbers geometrically. They are an essential tool in understanding and manipulating complex numbers in mathematics, particularly in fields like engineering, physics, and applied mathematics.

## Basic Concept
A complex number is of the form $a + bi$, where $a$ and $b$ are real numbers, and $i$ is the imaginary unit with the property $i^2 = -1$. In an Argand diagram, this complex number is represented as a point or a vector in a two-dimensional plane.

### Components of Argand Diagram:
1. **Real Axis**: The horizontal axis, representing the real part of the complex number.
2. **Imaginary Axis**: The vertical axis, representing the imaginary part of the complex number.
3. **Point Representation**: A complex number $a + bi$ is represented as a point with coordinates $(a, b)$.
4. **Vector Representation**: Alternatively, the same number can be represented as a vector from the origin (0, 0) to the point $(a, b)$.

### Example
Consider the complex number $3 + 4i$. On an Argand diagram, this is represented as a point at coordinates (3, 4), or as a vector from the origin to the point (3, 4).

## Applications
Argand diagrams are particularly useful in:
1. **Visualizing Complex Number Operations**: Addition, subtraction, and multiplication of complex numbers can be easily visualized.
2. **Modulus and Argument**: The length of the vector represents the modulus (or absolute value) of the complex number, and the angle it makes with the real axis represents its argument.
3. **Polar Form Representation**: Complex numbers can be expressed in polar form using Argand diagrams.

## Conclusion
Argand diagrams provide a powerful visual tool for understanding and working with complex numbers. They bridge the gap between algebraic and geometric representations of complex numbers.

---

### Test Questions
1. STARTI [Basic] Question: Represent the complex number 2 - 3i on an Argand Diagram. Back: The complex number 2 - 3i would be represented as a point at coordinates (2, -3) on the Argand Diagram. ENDI
2. STARTI [Basic] Question: What does the length of the vector in an Argand Diagram represent for a complex number? Back: The length of the vector represents the modulus (or absolute value) of the complex number. ENDI
3. STARTI [Basic] Question: If a complex number is represented by the point (4, 4) in an Argand Diagram, what is the complex number? Back: The complex number is 4 + 4i. ENDI

[[Complex Numbers]] | [[Polar Form of Complex Numbers]] | [[Mathematical Operations with Complex Numbers]]

# Intervals of Increase or Decrease in Functions

## Overview
In calculus, understanding the intervals of increase or decrease of a function is essential for analysing its behaviour. These intervals refer to the sections of the function's domain where its output either consistently rises (increases) or falls (decreases).

## Defining Intervals
- **Interval of Increase**: A function $f(x)$ is increasing on an interval if, for any two numbers $a$ and $b$ in that interval, $a < b$ implies $f(a) < f(b)$.
- **Interval of Decrease**: Conversely, $f(x)$ is decreasing on an interval if, for any two numbers $a$ and $b$ in that interval, $a < b$ implies $f(a) > f(b)$.

## Determining Intervals
To find these intervals, we typically use the first derivative $f'(x)$ of the function:
1. **Find the Derivative**: Calculate $f'(x)$, the first derivative of $f(x)$.
2. **Identify Critical Points**: Solve $f'(x) = 0$ and $f'(x)$ undefined to find critical points.
3. **Test Intervals**: Pick test points in the intervals created by the critical points and plug them into $f'(x)$. 
   - If $f'(x) > 0$ in an interval, $f(x)$ is increasing there.
   - If $f'(x) < 0$, $f(x)$ is decreasing.

## Historical Context
The concept of intervals of increase and decrease has been integral in calculus since its formalization by Isaac Newton and Gottfried Wilhelm Leibniz in the late 17th century. It is foundational in understanding the behaviour of functions and forms the basis for more advanced concepts like local maxima and minima.

## Example
Consider the function $f(x) = x^3 - 3x^2 - 9x + 10$.
1. Derivative: $f'(x) = 3x^2 - 6x - 9$.
2. Critical Points: Solve $3x^2 - 6x - 9 = 0$ to find the critical points.
3. Test Intervals: Choose test points in the intervals divided by the critical points and determine the sign of $f'(x)$.

## Test Questions
1. For the function $g(x) = x^2 - 4x + 3$, find the intervals where the function is increasing or decreasing.
2. Explain how the first derivative test helps in identifying the intervals of increase or decrease.
3. Determine the intervals of increase and decrease for $h(x) = \sin(x)$ in the interval $[0, 2\pi]$.

# Asymptotes

## Introduction
Asymptotes are lines that a graph approaches but never actually reaches. These occur in many types of functions and are crucial in understanding the behaviour of graphs, especially as the independent variable grows large or small.

## Types of Asymptotes
There are three main types of asymptotes:

### 1. Horizontal Asymptotes
These occur when the graph of a function approaches a particular y-value as x tends to infinity or negative infinity. Horizontal asymptotes are determined by the end behaviour of the function.

#### Example:
Consider $f(x) = \frac{1}{x}$. As $x$ approaches infinity, $f(x)$ approaches 0. Hence, the x-axis (y=0) is a horizontal asymptote.

### 2. Vertical Asymptotes
Vertical asymptotes occur when a function approaches infinity or negative infinity as the x-value approaches a particular number. This typically happens where the function is undefined.

#### Example:
For $g(x) = \frac{1}{x-1}$, as $x$ approaches 1, $g(x)$ approaches infinity. Thus, the line x=1 is a vertical asymptote.

### 3. Oblique (Slant) Asymptotes
These occur when the graph of a function approaches a line that is not horizontal as $x$ tends to infinity or negative infinity. They are common in rational functions where the degree of the numerator is one more than the degree of the denominator.

#### Example:
The function $h(x) = \frac{x^2 - 1}{x}$ has the oblique asymptote y = x, as the graph approaches this line for large values of $x$.

## Finding Asymptotes
To find asymptotes, one typically analyses the limits of the function as $x$ approaches certain critical values or infinity. For rational functions, polynomial division can also be used to identify oblique asymptotes.

## Historical Context
The concept of asymptotes dates back to Apollonius of Perga, an ancient Greek geometer and astronomer, who discussed the idea in terms of conic sections. The term "asymptote" comes from Greek, meaning "not falling together".

## Test Questions
1. Determine the horizontal and vertical asymptotes of $f(x) = \frac{2x}{x-3}$.
2. Does the function $g(x) = x^3 - 3x + 2$ have any asymptotes? Justify your answer.
3. Find the oblique asymptote of $h(x) = \frac{x^2 + 2x + 3}{x}$.

# Basic Complex Arithmetic

## Introduction
Complex numbers are a fundamental concept in mathematics, extending the real numbers and providing solutions to equations that have no real solutions. A complex number is defined as a number of the form $a + bi$, where $a$ and $b$ are real numbers, and $i$ is the imaginary unit with the property $i^2 = -1$.

## Definition and Representation
- **Real Part:** In a complex number $a + bi$, the term $a$ is the real part.
- **Imaginary Part:** The term $b$ is the imaginary part.
- **Imaginary Unit:** $i$ is defined such that $i^2 = -1$.

### Visual Representation
Complex numbers can be represented on a plane known as the Argand plane or complex plane, where the horizontal axis represents the real part and the vertical axis represents the imaginary part.

## Basic Operations
1. **Addition:** $(a + bi) + (c + di) = (a + c) + (b + d)i$.
2. **Subtraction:** $(a + bi) - (c + di) = (a - c) + (b - d)i$.
3. **Multiplication:** $(a + bi)(c + di) = ac + adi + bci + bdi^2 = (ac - bd) + (ad + bc)i$.
4. **Division:** For $c + di \neq 0$, $\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{c^2 + d^2}$.

### Conjugate
The conjugate of a complex number $a + bi$ is $a - bi$. It is useful in division and in finding the magnitude of a complex number.

### Magnitude
The magnitude (or modulus) of a complex number $a + bi$ is $\sqrt{a^2 + b^2}$.

## Historical Context
The concept of complex numbers emerged in the 16th century, initially in the context of solving cubic equations. Mathematicians like Gerolamo Cardano and Rafael Bombelli contributed to their development.

## Examples
1. **Addition Example:** $(3 + 2i) + (1 + 4i) = 4 + 6i$.
2. **Multiplication Example:** $(2 + 3i)(1 + 2i) = 2 + 4i + 3i + 6i^2 = -4 + 7i$.

## Conclusion and Test Questions
Understanding basic complex arithmetic is crucial for delving deeper into complex analysis and its applications in engineering, physics, and other sciences.

### Test Questions
1. STARTI [Basic] Question: Calculate the product of $(2 + i)$ and $(3 - 4i)$. Back: $2 \times 3 + 2 \times (-4i) + i \times 3 + i \times (-4i) = 6 - 8i + 3i - 4 = 2 - 5i$. ENDI
2. STARTI [Basic] Question: Find the magnitude of the complex number $3 + 4i$. Back: $\sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$. ENDI
3. STARTI [Basic] Question: What is the conjugate of the complex number $5 - 3i$? Back: $5 + 3i$. ENDI

---

For more detailed exploration of complex numbers and their properties, refer to the notes on [[Advanced Complex Analysis]].

# Calculus with Parametric Equations

## Introduction
Calculus with Parametric Equations offers a powerful way to analyse curves that cannot be defined as functions of a single variable. These curves, described by parametric equations, allow us to explore more complex geometries and motions.

### What Are Parametric Equations?
Parametric equations involve a set of equations where the coordinates of points on a curve (x and y) are defined as functions of a third variable, typically denoted as 't'. This 't' is a parameter, often representing time, allowing for the description of motion and change in geometry.

### Example:
The simple circular motion can be expressed parametrically as:
$$x(t) = r \cos(t), \quad y(t) = r \sin(t)$$
where $r$ is the radius of the circle and $t$ represents the angle from the positive x-axis.

## Calculus with Parametric Equations

### Differentiation
To find the slope of the tangent to a parametric curve, we differentiate both x and y with respect to t:
$$\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}}$$

### Integration
To find the area under a parametric curve, we integrate with respect to the parameter:
$$A = \int y(t) \, dx = \int y(t) \frac{dx}{dt} \, dt$$

### Length of a Parametric Curve
The formula for the length of a parametric curve from $t = a$ to $t = b$ is:
$$L = \int_{a}^{b} \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt$$

## Applications
1. **Physics and Engineering**: Modelling trajectories and movements.
2. **Computer Graphics**: Animating paths and shapes.
3. **Economics**: Analysing dynamic systems over time.

## Historical Context
The concept of parametric equations dates back to the 17th century, with notable contributions from Pierre de Fermat and René Descartes. Their work laid the foundation for modern calculus and analytical geometry.

## Example Problems

### Test Questions
1. STARTI [Basic] Question: If a particle moves along the curve given by x(t) = 3t^2 and y(t) = 2t^3, what is the slope of the tangent line at t = 1? Back: The slope at t = 1 is given by dy/dx = (dy/dt) / (dx/dt). Here, dy/dt = 6t^2 and dx/dt = 6t. So, at t = 1, the slope is 6/6 = 1. ENDI
2. STARTI [Basic] Question: How do you find the length of a parametric curve? Back: The length of a parametric curve from t = a to t = b is given by the integral L = ∫ from a to b of sqrt((dx/dt)^2 + (dy/dt)^2) dt. ENDI
3. STARTI [Basic] Question: For the parametric equations x = sin(t) and y = cos(t), what is the length of the curve from t = 0 to t = π/2? Back: The length is given by the integral ∫ from 0 to π/2 of sqrt((-sin(t))^2 + (-cos(t))^2) dt, which simplifies to π/2. ENDI

# Calculus with Polar Coordinates

## Introduction

Calculus with polar coordinates is a powerful tool in mathematics, especially in the realms of multivariable calculus and complex analysis. Polar coordinates provide an alternative to Cartesian coordinates and are particularly useful in dealing with problems involving circular or rotational symmetry.

### Overview of Polar Coordinates

In polar coordinates, a point in the plane is defined by two numbers: $r$ and $\theta$. Here, $r$ represents the radial distance from the origin, and $\theta$ is the angle measured from the positive x-axis to the point.

- **Conversion from Cartesian to Polar Coordinates**: Given a point $(x, y)$ in Cartesian coordinates, it can be converted to polar coordinates $(r, \theta)$ using:

  $$r = \sqrt{x^2 + y^2}$$
  $$\theta = \arctan\left(\frac{y}{x}\right)$$

- **Conversion from Polar to Cartesian Coordinates**: Given polar coordinates $(r, \theta)$, the Cartesian coordinates $(x, y)$ can be found as:

  $$x = r \cos(\theta)$$
  $$y = r \sin(\theta)$$

## Calculus in Polar Coordinates

### Differentiation

To differentiate a function given in polar coordinates, we often convert it to Cartesian coordinates, differentiate, and then convert back if necessary. Alternatively, for a curve defined by $r = f(\theta)$, the derivatives can be calculated directly in polar coordinates.

### Integration

In polar coordinates, integration is particularly useful for calculating areas and lengths of curves. 

- **Area of a Sector**: The area $A$ of a sector defined by the curve $r = f(\theta)$ from $\theta = a$ to $\theta = b$  is given by:

  $$A = \frac{1}{2} \int_{a}^{b} [f(\theta)]^2 d\theta$$

- **Length of a Curve**: The length $L$ of a curve defined by $r = f(\theta)$ from $\theta = a$ to $\theta = b$ is:

  $$L = \int_{a}^{b} \sqrt{[f(\theta)]^2 + \left[\frac{df(\theta)}{d\theta}\right]^2} d\theta$$

## Applications

Polar coordinates are extensively used in physics and engineering, especially in scenarios involving rotational motion, wave functions, and fields.

## Conclusion and Test Questions

Understanding calculus with polar coordinates expands your mathematical toolbox, allowing for a unique approach to problems involving circular or rotational symmetry.

### Test Questions

1. STARTI [Basic] Question: Convert the Cartesian point (3, 4) to polar coordinates. Back: $r = 5, \theta = \arctan(\frac{4}{3})$. ENDI
2. STARTI [Basic] Question: Calculate the area of a sector defined by $r = 2\theta$ for $\theta$ ranging from 0 to $\pi$. Back: $A = \frac{1}{2} \int_{0}^{\pi} (2\theta)^2 d\theta = \frac{\pi^3}{2}$. ENDI
3. STARTI [Basic] Question: Find the length of the curve $r = 1 + \sin(\theta)$ from $\theta = 0$ to $\theta = 2\pi$. Back: $L = \int_{0}^{2\pi} \sqrt{(1 + \sin(\theta))^2 + \cos^2(\theta)} d\theta$. ENDI

For further exploration, consider how these concepts apply in electromagnetism and orbital mechanics.

# Changing Double Integrals to Polar Coordinates

## Overview
Changing double integrals to polar coordinates is a technique used in multivariable calculus. This approach is particularly useful when evaluating integrals over circular or annular regions. The transformation simplifies the computation by aligning the integration region with the geometry of the polar coordinate system.

## Polar Coordinates
In polar coordinates, a point in the plane is represented by a radius $r$ and an angle $\theta$. The relationships between polar coordinates $(r, \theta)$ and Cartesian coordinates $(x, y)$ are:

- $x = r \cos(\theta)$
- $y = r \sin(\theta)$

## Transforming Double Integrals
When transforming a double integral from Cartesian to polar coordinates, the differential area element changes. In Cartesian coordinates, the area element is $dx \, dy$. In polar coordinates, it becomes $r \, dr \, d\theta$.

### The Jacobian
The Jacobian of the transformation is the determinant of the matrix of partial derivatives of $x$ and $y$ with respect to $r$ and $\theta$. For the polar coordinate transformation, the Jacobian is $r$. 

### The Integral
A double integral in Cartesian coordinates:

$$\int \int_R f(x,y) \, dx \, dy$$

transforms into polar coordinates as:

$$\int \int_R f(r\cos(\theta), r\sin(\theta)) \, r \, dr \, d\theta$$

## Examples
### Example 1: Circular Region
Consider a circle of radius $a$. The integral over this region can be transformed into polar coordinates where $r$ ranges from 0 to $a$ and $\theta$ ranges from 0 to $2\pi$.

### Example 2: Annular Region
For an annular region with inner radius $a$ and outer radius $b$, $r$ varies from $a$ to $b$ and $\theta$ from 0 to $2\pi$.

## Conclusion
Converting double integrals to polar coordinates simplifies the computation for circular or annular regions. This method leverages the natural symmetry of these regions in polar coordinates.

## Test Questions
1. What is the Jacobian in the transformation from Cartesian to polar coordinates?
2. How does the area element $dx \, dy$ in Cartesian coordinates change when transformed to polar coordinates?
3. For a double integral over a circle of radius $a$, what are the limits of integration for $r$ and $\theta$ in polar coordinates?

# Classifying Critical Points and Concavity

## Introduction
Classifying critical points and understanding concavity are fundamental concepts in calculus, particularly in the study of functions and their graphs. These concepts help in understanding the shape and behaviour of a function, which are crucial in fields like physics, engineering, and economics.

## Critical Points
A critical point of a function $f(x)$ occurs where its derivative $f'(x)$ is either zero or undefined. These points are essential in determining the local maxima and minima of the function.

### How to Find Critical Points
1. **Find the derivative**: Compute $f'(x)$.
2. **Solve for critical points**: Find values of $x$ where $f'(x) = 0$ or $f'(x)$ is undefined.

## Concavity
Concavity refers to the curvature of the graph of a function. A function is concave up if its graph lies above its tangent lines, and concave down if it lies below.

### How to Determine Concavity
1. **Second derivative**: Compute $f''(x)$, the second derivative of $f(x)$.
2. **Test for concavity**: 
   - If $f''(x) > 0$ for an interval, $f(x)$ is concave up on that interval.
   - If $f''(x) < 0$, $f(x)$ is concave down.

## Classifying Critical Points
Critical points can be classified using the first and second derivatives:
1. **First Derivative Test**: Analyse the sign of $f'(x)$ before and after the critical point.
2. **Second Derivative Test**: Use $f''(x)$ at the critical point.
   - If $f''(x) > 0$, the point is a local minimum.
   - If $f''(x) < 0$, it's a local maximum.
   - If $f''(x) = 0$, the test is inconclusive.

## Examples
1. **Function Example**: Consider $f(x) = x^3 - 3x^2 + 2$.
   - Find critical points.
   - Determine concavity.
   - Classify the critical points.

2. **Historical Context**: The concept of concavity and the classification of critical points have been pivotal in the development of calculus, tracing back to the works of Newton and Leibniz.

## Conclusion
Understanding the classification of critical points and concavity is crucial in analysing the behaviour of functions. It provides insight into the function's local and global behaviour, helping in various applications across multiple disciplines.

---

## Test Questions
1. What is a critical point, and how is it determined?
2. Explain the difference between concave up and concave down.
3. How can the second derivative test be used to classify critical points?

For further exploration, check out the resources on calculus in your [[Calculus Vault]].

# Complex Arithmetic in Different Forms

## Introduction

Complex numbers, a fundamental concept in mathematics, extend the idea of the one-dimensional number line to a two-dimensional complex plane. This note delves into complex arithmetic in various forms, primarily focusing on the rectangular (a + bi) and polar (r(cos θ + i sin θ)) forms.

## Rectangular Form

In the rectangular form, a complex number is expressed as $a + bi$, where $a$ and $b$ are real numbers, and $i$ is the imaginary unit with the property $i^2 = -1$.

### Operations:

1. **Addition/Subtraction**: Add or subtract corresponding real and imaginary parts.
   - $(a + bi) \pm (c + di) = (a \pm c) + (b \pm d)i$

2. **Multiplication**: Use distributive law and simplify using $i^2 = -1$.
   - $(a + bi)(c + di) = ac + adi + bci + bdi^2 = (ac - bd) + (ad + bc)i$

3. **Division**: Multiply numerator and denominator by the conjugate of the denominator.
   - $\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}$

## Polar Form

A complex number in polar form is represented as $r(\cos \theta + i \sin \theta)$, where $r$ is the magnitude and $\theta$ is the angle with the positive real axis.

### Operations:

1. **Multiplication**: Multiply the magnitudes and add the angles.
   - $r_1(\cos \theta_1 + i \sin \theta_1) \cdot r_2(\cos \theta_2 + i \sin \theta_2) = r_1r_2(\cos(\theta_1 + \theta_2) + i \sin(\theta_1 + \theta_2))$

2. **Division**: Divide the magnitudes and subtract the angles.
   - $\frac{r_1(\cos \theta_1 + i \sin \theta_1)}{r_2(\cos \theta_2 + i \sin \theta_2)} = \frac{r_1}{r_2}(\cos(\theta_1 - \theta_2) + i \sin(\theta_1 - \theta_2))$

3. **De Moivre's Theorem**: Useful for raising a complex number to a power.
   - $[r(\cos \theta + i \sin \theta)]^n = r^n(\cos(n\theta) + i \sin(n\theta))$

## Historical Context

The concept of complex numbers emerged in the 16th century, primarily in the works of Gerolamo Cardano and Rafael Bombelli. They were initially met with skepticism but gradually became essential in various fields of mathematics and physics.

## Examples

1. **Addition in Rectangular Form**: $(3 + 4i) + (1 - 2i) = 4 + 2i$
2. **Multiplication in Polar Form**: $2(\cos 45^\circ + i \sin 45^\circ) \cdot 3(\cos 30^\circ + i \sin 30^\circ)$

## Test Questions

1. STARTI [Basic] Question: Simplify $(2 + 3i) \cdot (1 - 4i)$. Back: $14 + 5i$. ENDI
2. STARTI [Basic] Question: Express $1 + i$ in polar form. Back: $\sqrt{2}(\cos 45^\circ + i \sin 45^\circ)$. ENDI
3. STARTI [Basic] Question: Use De Moivre's Theorem to find $(1 + i)^4$. Back: $-4$. ENDI

---

For further exploration, consider creating notes on related topics such as [[Euler's Formula]] and [[Applications of Complex Numbers in Engineering]].


# Complex Conjugates

## Introduction
Complex numbers, a fundamental concept in mathematics, are used to solve equations that do not have real solutions. A complex number is typically written in the form $a + bi$, where $a$ and $b$ are real numbers, and $i$ is the imaginary unit with the property $i^2 = -1$. 

## Definition of Complex Conjugate
The complex conjugate of a complex number is obtained by changing the sign of the imaginary part. Therefore, the complex conjugate of $a + bi$ is $a - bi$. This operation is crucial in various mathematical processes, such as simplifying the division of complex numbers.

## Properties
1. **Reflection**: The complex conjugate of $a + bi$ reflects the point across the real axis in the complex plane.
2. **Multiplication**: The product of a complex number and its conjugate is always a non-negative real number: $(a + bi)(a - bi) = a^2 + b^2$.
3. **Modulus**: The modulus of a complex number, given by $\sqrt{a^2 + b^2}$, is related to its conjugate. It can be computed as the square root of the product of a complex number and its conjugate.
4. **Addition and Subtraction**: The sum and difference of a complex number and its conjugate are real numbers. The sum $(a + bi) + (a - bi)$ is $2a$, and the difference is $2bi$.

## Applications
- **Simplifying Expressions**: In division, multiplying the numerator and denominator by the conjugate of the denominator simplifies the expression.
- **Solving Equations**: In quadratic equations with complex solutions, the roots are conjugates of each other.
- **Signal Processing**: Complex conjugates are used in signal processing and in the representation of waves.

## Historical Context
The concept of complex conjugates emerged alongside the development of complex numbers in the 16th century, primarily as a tool for solving cubic equations.

## Example
Consider the complex number $3 + 4i$. Its complex conjugate is $3 - 4i$. The product of these numbers is $(3 + 4i)(3 - 4i) = 9 + 16 = 25$, which is a real number.

## Test Questions
1. STARTI [Basic] Question: What is the complex conjugate of $5 - 3i$? Back: $5 + 3i$. ENDI
2. STARTI [Intermediate] Question: Calculate the modulus of $7 + 24i$. Back: $\sqrt{7^2 + 24^2} = 25$. ENDI
3. STARTI [Advanced] Question: If $z = 2 - 5i$, find the product $z \cdot \overline{z}$. Back: $(2 - 5i)(2 + 5i) = 4 + 25 = 29$. ENDI

For further exploration, see related topics like [[Euler's Formula]], [[Polar Form of Complex Numbers]], and [[Roots of Unity]].

# Composition of Functions

## Overview
In mathematics, the concept of the composition of functions (or function composition) is a fundamental operation. It involves applying one function to the results of another. This concept is essential in various branches of mathematics, including calculus, abstract algebra, and functional analysis.

### Definition
Given two functions $f: X \to Y$ and $g: Y \to Z$, the composition of $f$ and $g$ is written as $g \circ f$ and is defined as:
$$(g \circ f)(x) = g(f(x))$$
for all $x$ in $X$. In this composition, $f$ is first applied to $x$, and then $g$ is applied to the output of $f$.

### Properties
- **Associativity:** If $f, g,$ and $h$ are functions, then $h \circ (g \circ f) = (h \circ g) \circ f$.
- **Identity Function:** For any function $f: X \to Y$, the composition with the identity function $i_X: X \to X$ or $i_Y: Y \to Y$ is the same as $f$, i.e., $f \circ i_X = f$ and $i_Y \circ f = f$.

## Historical Context
The concept of function composition dates back to the origins of modern calculus in the 17th century. It was more rigorously formalized in the 19th century with the development of abstract algebra and set theory.

## Applications
- **Calculus:** In calculus, composition of functions is used in the chain rule for derivatives.
- **Computer Science:** Function composition is foundational in programming, particularly in functional programming languages.
- **Abstract Algebra:** In group theory, composition of functions (or operations) is a basic example of a binary operation.

## Examples

1. **Polynomial Composition:** If $f(x) = 2x + 3$ and $g(x) = x^2$, then $(g \circ f)(x) = (2x + 3)^2$.
2. **Trigonometric Composition:** For $f(x) = \sin(x)$ and $g(x) = x^2$, $(g \circ f)(x) = \sin^2(x)$.

## Test Questions
1. STARTI [Basic] Question: If $f(x) = x + 1$ and $g(x) = 3x$, what is $(g \circ f)(x)$? Back: $(g \circ f)(x) = 3(x + 1) = 3x + 3$. ENDI
2. STARTI [Basic] Question: What is the composition $(f \circ g)(x)$ for $f(x) = \sqrt{x}$ and $g(x) = 4x + 1$? Back: $(f \circ g)(x) = \sqrt{4x + 1}$. ENDI
3. STARTI [Basic] Question: Prove the associativity of function composition with functions $f, g,$ and $h$. Back: Demonstrate that $h \circ (g \circ f)(x) = (h \circ g) \circ f)(x)$ for all $x$ in the domain. ENDI

# Continuity and Differentiability

Continuity and differentiability are fundamental concepts in calculus, which form the backbone of mathematical analysis, particularly in the study of functions. Understanding these concepts is crucial for anyone studying undergraduate mathematics.

## Continuity

### Definition
A function $f(x)$ is said to be continuous at a point $x = a$ if the following three conditions are met:
1. $f(a)$ is defined.
2. The limit of $f(x)$ as $x$ approaches $a$ exists.
3. The limit of $f(x)$ as $x$ approaches $a$ is equal to $f(a)$.

In simpler terms, a function is continuous at a point if there is no interruption in its graph at that point. 

### Types of Continuity
- **Continuous on an Interval:** If a function is continuous at every point in an interval, it is said to be continuous on that interval.
- **Uniform Continuity:** A stronger form where the way the function behaves does not depend on the choice of the point in its domain.

## Differentiability

### Definition
A function $f(x)$ is differentiable at a point $x = a$ if the derivative of $f(x)$ at that point exists. This derivative is given by the limit:
$$f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}$$

If this limit exists, the function is differentiable at $x = a$. Differentiability implies a function's graph has a tangent at that point and is not sharply turning.

### Relationship with Continuity
A crucial aspect to remember is that if a function is differentiable at a point, then it must be continuous at that point. However, the converse is not necessarily true: a continuous function may not be differentiable at all points.

## Examples and Historical Context

1. **The Function $f(x) = |x|$:** This function is continuous everywhere but not differentiable at $x = 0$ because of the sharp point at the origin.
2. **The Discovery of Calculus:** The concepts of continuity and differentiability were central to the development of calculus by Newton and Leibniz in the 17th century.

## Test Questions

1. Is the function $f(x) = \frac{1}{x}$ continuous at $x = 0$? Why or why not?
2. Give an example of a function that is continuous at every point but not differentiable at exactly one point.
3. Show that the function $f(x) = x^2$ is differentiable at $x = 1$ and find its derivative at that point.

# Continuity at a Point

## Definition
Continuity at a point in the realm of mathematics, particularly in calculus, is a fundamental concept that describes the behaviour of functions at specific points. A function $f(x)$ is said to be continuous at a point $x = a$ if the following three conditions are met:
1. The function $f(x)$ is defined at $x = a$; that is, $f(a)$ exists.
2. The limit of $f(x)$ as $x$ approaches $a$ exists.
3. The limit of $f(x)$ as $x$ approaches $a$ is equal to the function value at $a$; mathematically, $\lim_{x \to a} f(x) = f(a)$.

## Intuitive Understanding
Imagine drawing the graph of a function without lifting your pen off the paper. If you can do this through a point $a$, the function is continuous at that point. This imagery helps understand continuity as a smooth, uninterrupted path.

## Historical Context
The concept of continuity has evolved over centuries. Early mathematicians like Newton and Leibniz, founders of calculus, used intuitive notions of continuity. Rigorous definitions, similar to the one used today, were developed in the 19th century by mathematicians like Augustin-Louis Cauchy and Karl Weierstrass. This period marked a shift from intuitive understandings to precise mathematical definitions.

## Examples
1. **Polynomial Functions**: Consider $f(x) = x^2$. This function is continuous at every point because it meets all three conditions for any value of $x$.
2. **Rational Functions**: The function $g(x) = \frac{1}{x}$ is continuous at every point except $x = 0$, where it is undefined.
3. **Piecewise Functions**: Consider $$h(x) = \begin{cases} 
x^2, & \text{if } x < 2 \\
5, & \text{if } x = 2 \\
x + 3, & \text{if } x > 2 
\end{cases}$$. Here, $h(x)$ is continuous at $x = 2$ because $\lim_{x \to 2} h(x) = h(2) = 5$.

## Test Questions
1. Is the function $f(x) = \frac{x^2 - 1}{x - 1}$ continuous at $x = 1$? Why or why not?
2. If $\lim_{x \to 3} g(x) = 6$ and $g(3) = 6$, is $g(x)$ continuous at $x = 3$?
3. For the function $h(x) = |x|$, identify a point where $h$ is not continuous. Explain your reasoning.

# Continuity over an Interval

## Introduction
Continuity is a fundamental concept in calculus, representing the idea that a function does not have any "jumps," "breaks," or "holes" in its graph. When we talk about a function being continuous over an interval, we mean that for every point within this interval, the function does not exhibit any of these disruptions.

## Definition
A function $f(x)$ is said to be continuous on an interval if it is continuous at every point in that interval. More formally, for any $c$ in the interval:

1. **Existence**: The function $f(x)$ is defined at $c$.
2. **Limit Existence**: The limit of $f(x)$ as $x$ approaches $c$ exists.
3. **Limit Equals Function**: The limit of $f(x)$ as $x$ approaches $c$ is equal to $f(c)$.

Mathematically, this is expressed as:
$$\lim_{{x \to c}} f(x) = f(c)$$

## Types of Intervals
There are different types of intervals, including open, closed, and half-open intervals. For example, an open interval $(a, b)$ does not include the end points $a$ and $b$, while a closed interval $[a, b]$ includes both $a$ and $b$.

## Historical Context
The formal definition of continuity was developed in the 19th century by mathematicians like Augustin-Louis Cauchy and Karl Weierstrass. This development was part of a broader effort to rigorize calculus, which was initially based on intuitive notions of continuity and infinitesimals.

## Examples
1. **Polynomial Functions**: All polynomial functions are continuous over any interval. For instance, the function $f(x) = x^2$ is continuous for all real numbers.
2. **Rational Functions**: A rational function, such as $f(x) = \frac{1}{x}$, is continuous everywhere except where the denominator is zero. For $f(x) = \frac{1}{x}$, the function is not continuous at $x = 0$.

## Application
Understanding continuity over an interval is crucial for various mathematical concepts like integration. The Fundamental Theorem of Calculus, for instance, requires the integrand to be continuous over the interval of integration.

## Test Questions
1. Is the function $g(x) = \frac{x}{x-2}$ continuous over the interval $(1, 3)$? Explain why or why not.
2. For the function $h(x) = |x|$, determine if it is continuous over the interval $[-1, 1]$. Provide reasoning.
3. Find an example of a function that is continuous over a closed interval $[a, b]$ and explain your choice.

[[Obsidian Mathematics Notes]] | [[Calculus Basics]] | [[Fundamental Theorem of Calculus]]

# Converting between Cartesian and Polar Coordinates

## Introduction
In mathematics, two common coordinate systems are used to specify the position of a point in a plane: Cartesian and polar coordinates. Cartesian coordinates are denoted in the form (x, y), representing points in terms of their horizontal (x) and vertical (y) distances. In contrast, polar coordinates use the form (r, $\theta$), where 'r' is the radius (distance from the origin) and '$\theta$' (theta) is the angle from the positive x-axis.

Understanding how to convert between these two systems is crucial in various fields like physics, engineering, and computer graphics.

## Cartesian to Polar Conversion
To convert Cartesian coordinates (x, y) to polar coordinates (r, $\theta$):

1. **Radius (r):** The radius is the distance of the point from the origin (0, 0). It is calculated using the Pythagorean theorem:
   
   $$r = \sqrt{x^2 + y^2}$$

2. **Angle ($\theta$):** The angle is measured from the positive x-axis to the line segment that joins the point to the origin. It is calculated using the arctan function, but remember to consider the quadrant in which the point lies:

   $$\theta = \arctan\left(\frac{y}{x}\right)$$
   
   Adjust $\theta$ based on the quadrant:
   - In the 2nd and 3rd quadrants, add π to $\theta$.
   - In the 4th quadrant, add 2π to $\theta$ if you need a positive angle.

## Polar to Cartesian Conversion
To convert polar coordinates (r, $\theta$) to Cartesian coordinates (x, y):

1. **X-coordinate:** It's the horizontal distance, calculated as:

   $$x = r \cos(\theta)$$

2. **Y-coordinate:** It's the vertical distance, calculated as:

   $$y = r \sin(\theta)$$

## Example
Consider a point P with Cartesian coordinates (3, 4). To convert it to polar coordinates:

1. Radius: $r = \sqrt{3^2 + 4^2} = 5$
2. Angle: $\theta = \arctan\left(\frac{4}{3}\right) \approx 53.13^\circ$ or $\approx 0.93$ radians.

Thus, the polar coordinates are approximately (5, 0.93).

## Conclusion and Test Questions
Understanding the conversion between Cartesian and Polar Coordinates is vital in many mathematical and practical applications. It allows us to approach problems from different perspectives and apply various mathematical tools.

### Test Questions
1. Convert the Cartesian coordinates (-3, 3) to polar coordinates.
2. Convert the polar coordinates (4, π/4) to Cartesian coordinates.
3. If a point in polar coordinates is given as (6, π/3), what are its Cartesian coordinates?

# Curve Length

Curve length, also known as arc length, is a fundamental concept in mathematics, particularly in calculus and geometry. It refers to the distance along a curved line or the length of a curve.

## Definition

The length of a curve $C$ from a point $A$ to a point $B$ is defined as the limit of the sum of line segment lengths that approximate the curve as the number of segments approaches infinity. Mathematically, for a curve defined by a function $y = f(x)$ from $x = a$ to $x = b$, the curve length $L$ is given by:

$$L = \int_{a}^{b} \sqrt{1 + \left( \frac{dy}{dx} \right)^2} \, dx$$

For a parametrically defined curve $x = g(t)$, $y = h(t)$, the formula becomes:

$$L = \int_{a}^{b} \sqrt{\left( \frac{dx}{dt} \right)^2 + \left( \frac{dy}{dt} \right)^2} \, dt$$

### Derivation

This derived with Pythagoras and the idea that the length of a curve at an infinitesimally small length $\Delta s=\sqrt{(\Delta x)^2+(\Delta y)^2}$, which can then be divided by $(\Delta x)^2$ in the square root and then balanced by multiplying $\Delta x$ outside of the square root, giving the required result.

The derivation is similar for a parametrically defined curve.

## Historical Context

The concept of curve length dates back to ancient Greece, where mathematicians like Archimedes began exploring the lengths of curves. The development of calculus by Newton and Leibniz in the 17th century provided the necessary tools for a more rigorous and general approach to determining curve lengths.

## Applications

- **Physics**: Calculating the length of a trajectory.
- **Engineering**: Determining the material needed for curved structures.
- **Computer Graphics**: In rendering curves and computing their properties.

## Examples

1. **Circle Arc**: For a circle of radius $r$, the length of an arc with angle $\theta$ (in radians) is $L = r\theta$.
2. **Parabola**: Finding the length of a segment of a parabola involves integrating the square root of a quadratic expression.

## Test Questions

1. Calculate the length of the curve $y = x^2$ from $x = 0$ to $x = 1$.
2. For a circle of radius 5, what is the length of an arc subtending a $\frac{\pi}{2}$ angle at the center?
3. Determine the length of the curve defined by $x = \cos(t)$, $y = \sin(t)$ from $t = 0$ to $t = \frac{\pi}{2}$.

---

This note aims to provide a foundational understanding of curve length, integrating historical perspectives and practical examples. For a deeper exploration, consider investigating more complex curves and their properties.

# Cylindrical Polar Coordinates

Cylindrical polar coordinates are a three-dimensional extension of the two-dimensional polar coordinate system. They provide a convenient way of describing points in space, especially in scenarios involving cylindrical symmetry.

## Definition

In cylindrical coordinates, a point $P$ in space is represented by three coordinates: $(r, \theta, z)$.

- $r$: Radial distance from the origin to the point's projection in the xy-plane.
- $\theta$: Angle (in radians or degrees) between the positive x-axis and the line from the origin to the point's projection in the xy-plane.
- $z$: Height above the xy-plane.

## Conversion to Cartesian Coordinates

To convert cylindrical coordinates $(r, \theta, z)$ to Cartesian coordinates $(x, y, z)$, use the following formulas:

$$x = r \cos(\theta)$$
$$y = r \sin(\theta)$$
$$z = z$$

## Applications

Cylindrical coordinates are particularly useful in dealing with problems involving cylindrical symmetry, such as the electric field of a long straight wire, or the flow of fluid in a pipe.

## Historical Context

The development of cylindrical coordinates can be traced back to the works of René Descartes and Isaac Newton, who laid the foundations for three-dimensional coordinate systems. These coordinates are an extension of polar coordinates, which were used in ancient Greek astronomy and developed further in the Islamic world during the medieval period.

## Examples

1. **Point on a Cylinder**: If you have a cylinder of radius $a$ aligned along the z-axis, any point on the surface of the cylinder will have cylindrical coordinates $(a, \theta, z)$, where $\theta$ and $z$ vary.

2. **Helix**: A helix (like a spring or corkscrew) can be represented as $(r, \theta, c\theta)$, where $c$ is a constant, showing how the helix moves upwards as it rotates around the axis.

## Test Questions

1. Convert the cylindrical coordinates $(5, \pi/4, 3)$ into Cartesian coordinates.
2. If a point in Cartesian coordinates is $(3, -3, 5)$, what are its cylindrical coordinates?
3. Describe the cylindrical coordinates of a point that lies on the y-axis, 4 units above the xy-plane.

For further exploration, consider how cylindrical coordinates are used in vector calculus, such as in expressing gradient, divergence, and curl. Remember to cross-reference with related concepts like [[Spherical Coordinates]] and [[Cartesian Coordinates]] for a more comprehensive understanding.

# Difference Quotient and Derivative

## Introduction
The concepts of the difference quotient and the derivative are fundamental in calculus, particularly in the study of functions and their rates of change. Understanding these concepts is crucial for students of mathematics at the undergraduate level.

## Difference Quotient
The difference quotient is a method used to approximate the slope of a line tangent to a point on a graph of a function. It is given by the formula:

$$\text{Difference Quotient} = \frac{f(x + h) - f(x)}{h}$$

where:
- $f(x)$ is the value of the function at point $x$,
- $h$ is an increment in $x$,
- $f(x + h)$ is the function value at $x + h$.

### Purpose
The difference quotient is used to find the average rate of change of the function over the interval $[x, x + h]$. This concept is pivotal in understanding how functions change and is a stepping stone towards the concept of derivatives.

## Derivative
The derivative of a function represents the rate at which the function's value changes at a particular point. It is defined as the limit of the difference quotient as $h$ approaches zero:

$$\text{Derivative} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

### Significance
- **Instantaneous Rate of Change**: Unlike the difference quotient, which gives the average rate of change, the derivative provides the instantaneous rate of change at a specific point.
- **Slope of Tangent Line**: The derivative at a point gives the slope of the tangent line to the function at that point.
- **Applications**: Derivatives have vast applications in physics, engineering, economics, and other fields, often used to model real-world scenarios.

## Relationship Between Difference Quotient and Derivative
The derivative is essentially the limit of the difference quotient as the interval $h$ becomes infinitesimally small. This relationship bridges the discrete approximation of the rate of change (difference quotient) to the continuous and exact rate of change (derivative).

## Example
Consider the function $f(x) = x^2$. The difference quotient and derivative are calculated as follows:

- **Difference Quotient**: $\frac{(x + h)^2 - x^2}{h}$
- **Derivative**: $\lim_{h \to 0} \frac{(x + h)^2 - x^2}{h} = 2x$

## Conclusion
The difference quotient and derivative are key concepts in calculus, each serving a unique purpose in understanding how functions behave. The transition from the difference quotient to the derivative marks the move from an average rate of change to an instantaneous one, a fundamental leap in mathematical analysis.

## Test Questions
1. What is the difference quotient of the function $f(x) = 3x + 2$?
2. Calculate the derivative of $f(x) = x^3$ at $x = 2$.
3. Explain how the derivative can be viewed as a limit of the difference quotient.

# Differentiability of Functions

## Introduction
In calculus, differentiability is a fundamental concept that deals with the existence and nature of derivatives of functions. A function is said to be differentiable at a point if it has a derivative at that point. This concept is closely related to continuity but is a stronger condition.

## Understanding Differentiability

### Definition
A function $f: \mathbb{R} \rightarrow \mathbb{R}$ is differentiable at a point $a$ if the following limit exists:
$$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$
This limit, if it exists, is known as the derivative of $f$ at $a$.

### Relationship with Continuity
For a function to be differentiable at a point, it must be continuous at that point. However, the converse is not true; a function can be continuous at a point but not differentiable there. A classic example is the absolute value function, which is continuous everywhere but not differentiable at $x = 0$.

## Examples of Differentiable Functions

1. **Linear Functions**: Any linear function $f(x) = mx + b$ is differentiable everywhere, and its derivative is the constant $m$.
2. **Polynomials**: Polynomials are differentiable everywhere. For example, the derivative of $f(x) = x^2$ is $f'(x) = 2x$.
3. **Trigonometric Functions**: Functions like $\sin(x)$ and $\cos(x)$ are differentiable everywhere, with their derivatives being $\cos(x)$ and $-\sin(x)$ respectively.

## Non-Examples
- **The Absolute Value Function**: As mentioned, $f(x) = |x|$ is not differentiable at $x = 0$ because the function makes a sharp turn there.
- **Step Functions**: Functions that have jumps or discontinuities, like the Heaviside step function, are not differentiable at those points of discontinuity.

## Historical Context
The concept of differentiability was formalized in the 17th century, primarily through the work of Isaac Newton and Gottfried Wilhelm Leibniz. Their development of calculus introduced the fundamental principles of differentiation, which have since become essential in mathematics, physics, and engineering.

## Test Questions
1. Is the function $f(x) = x^3$ differentiable at $x = 2$? What is its derivative at this point?
2. Give an example of a function that is continuous everywhere but not differentiable at exactly one point.
3. Explain why a function that has a corner or a cusp at a point is not differentiable at that point.

[[Calculus]] | [[Derivatives]] | [[Continuity]]

# Differentials and Chain Rule

## Introduction
In calculus, differentials play a crucial role in understanding how functions change. The concept of a differential is intimately connected with derivatives, providing a framework to approximate changes in functions. The Chain Rule, a fundamental theorem in calculus, enables us to differentiate composite functions. It's an essential tool for dealing with complex functions constructed from simpler ones.

## Differentials
Differentials can be thought of as the "change" in a function due to a small change in its input. If $y = f(x)$, the differential of $y$, denoted as $dy$, is defined as:
$$dy = f'(x) \, dx$$
Here, $dx$ represents a small change in $x$, and $f'(x)$ is the derivative of $f$ with respect to $x$. The differential $dy$ approximates the change in $y$ due to the change $dx$ in $x$.

## Chain Rule
The Chain Rule is a formula to compute the derivative of a composite function. If a function $y$ is defined as $y = g(f(x))$, then the derivative of $y$ with respect to $x$ is given by:
$$\frac{dy}{dx} = \frac{dg}{df} \cdot \frac{df}{dx}$$
This rule is incredibly useful when dealing with functions where one function is nested inside another.

## Application
Consider a scenario where we have a temperature function $T$ that depends on time $t$, and time $t$ depends on another variable $s$. To find how $T$ changes with $s$, we use the Chain Rule:
$$\frac{dT}{ds} = \frac{dT}{dt} \cdot \frac{dt}{ds}$$

## Test Questions
1. If $y = (3x^2 + 2x)^5$, find $\frac{dy}{dx}$ using the Chain Rule.
2. Calculate the differential $dy$ for the function $y = \sin(x)$ when $dx = 0.1$.
3. Given $f(x) = \ln(x)$ and $g(x) = e^x$, find $\frac{d}{dx}g(f(x))$ using the Chain Rule.

---

This note provides a foundational understanding of differentials and the Chain Rule. Remember, practicing these concepts with various functions enhances comprehension and skill in calculus.

# Domain and Range

## Introduction
The concepts of domain and range are fundamental in mathematics, particularly in the study of functions. Understanding these concepts is crucial for anyone studying undergraduate mathematics, as they form the basis for further exploration in calculus, algebra, and beyond.

## Domain
The domain of a function refers to the set of all possible input values (usually represented as x-values) for which the function is defined. It is essentially the collection of all inputs over which the function can operate.

### Examples
1. For a linear function like $f(x) = 2x + 3$, the domain is all real numbers, since you can input any real number and get a real number as output.
2. For the function $g(x) = \frac{1}{x}$, the domain is all real numbers except zero, as division by zero is undefined.

## Range
The range of a function refers to the set of all possible output values (usually represented as y-values) that the function can produce. It is the collection of all outputs that result from using the domain elements as inputs in the function.

### Examples
1. For $f(x) = 2x + 3$, the range is also all real numbers, as the output can be any real number depending on the input.
2. For $h(x) = \sqrt{x}$, the range is all non-negative real numbers, as the square root of a real number cannot be negative.

## Historical Context
The concepts of domain and range were developed as mathematicians began to understand functions more deeply. They are integral to the Cartesian coordinate system, conceptualized by René Descartes, where the domain and range represent the x and y-axes, respectively.

## Test Questions
1. STARTI [Basic] Question: What is the domain of the function $f(x) = \frac{1}{x-2}$? Back: All real numbers except 2, because the function is undefined at $x = 2$. ENDI
2. STARTI [Basic] Question: If a function's range is all non-negative real numbers, can it be a linear function? Back: No, a linear function has a range of all real numbers, not just non-negative ones. ENDI
3. STARTI [Basic] Question: How does the concept of domain differ from that of range in a function? Back: The domain consists of all possible input values, while the range consists of all possible output values. ENDI

---

Understanding domain and range sets the foundation for exploring more complex mathematical concepts and functions. For further exploration, consider creating notes on specific types of functions, such as quadratic or exponential, and examining their domains and ranges.

# Double Integrals and Areas

## Overview
Double integrals extend the concept of a single integral to calculate the volume under a surface in a two-dimensional region. They are crucial in multiple fields such as physics, engineering, and probability.

## Concept
A double integral, denoted as $\int\int f(x, y) \,dx\,dy$, sums up the function $f(x, y)$ over a region in the xy-plane. The inner integral $\int f(x, y) \,dx$ is integrated with respect to x, holding y constant. The outer integral $\int (...) \,dy$ then integrates the result over y.

## Application in Area Calculation
Double integrals are particularly useful in computing the area of a region in the xy-plane. For a region $R$, the area $A$ is given by:

$$A = \int\int_R \,dx\,dy$$

This integral sums up small elements of area $dA$ over the entire region $R$.

## Example
Consider calculating the area of a rectangle with length $l$ and width $w$. The area $A$ is given by:

$$A = \int_0^w\int_0^l \,dx\,dy = lw$$

This example demonstrates how a double integral can be used to compute areas of basic shapes.

## Historical Context
The concept of double integrals was developed in the 17th century as part of the broader development of calculus. Key figures like Isaac Newton and Gottfried Wilhelm Leibniz contributed to its foundational theories.

## Test Questions
1. **[Basic]** Question: What is the purpose of a double integral? Back: To calculate the volume under a surface over a two-dimensional region.
2. **[Basic]** Question: How is the area of a region calculated using double integrals? Back: By integrating 1 over the region, i.e., $\int\int_R \,dx\,dy$.
3. **[Basic]** Question: Compute the area of a circle with radius $r$ using a double integral. Back: $A = \int\int_R \,dx\,dy$, where $R$ is the circular region. The integral in polar coordinates is $\int_0^{2\pi}\int_0^r rdrd\theta = \pi r^2$.

For further exploration, consider extending these concepts to more complex shapes and their applications in various fields.

# Error Term in Taylor Series

## Overview
The Taylor series is a powerful tool in calculus for approximating functions using polynomials. For a given function $f(x)$, its Taylor series expansion around a point $a$ is given by:

$$f(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \frac{f'''(a)}{3!}(x - a)^3 + \cdots$$

However, this expansion is an approximation, and the difference between the actual function value and its Taylor series approximation is captured by the **error term**.

## The Error Term
The error term, also known as the remainder of a Taylor series, quantifies the accuracy of the approximation. For a Taylor series truncated after the $n$th term, the error term $R_n(x)$ is given by:

$$R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{(n+1)}$$

where $c$ is some value between $a$ and $x$. This form of the remainder is known as the Lagrange form of the remainder.

### Significance
- **Accuracy of Approximation**: The error term is crucial for understanding how good the Taylor series approximation is.
- **Convergence**: It helps in determining if the series converges to the function as $n$ tends to infinity.

## Examples in Context
1. **Exponential Function**: The Taylor series of $e^x$ around 0 is $1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$. The error term helps understand how many terms are needed to approximate $e^x$ to a desired accuracy.
2. **Trigonometric Functions**: Similarly, for sine and cosine functions, the error term indicates the degree of approximation for different polynomial degrees.

## Test Questions
1. **[Basic]** Question: What is the formula for the error term in Taylor series? Back: $R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{(n+1)}$.
2. **[Basic]** Question: Explain why the error term is important in the Taylor series. Back: It quantifies the accuracy of the Taylor series approximation and helps in understanding the convergence of the series.
3. **[Basic]** Question: Given the Taylor series of $\sin(x)$ around $0$, how does the error term help in deciding the number of terms to use for an approximation? Back: The error term helps in determining how many terms of the series are needed to achieve a desired level of accuracy in approximating $\sin(x)$.

---

This note provides a basic understanding of the error term in Taylor series, emphasizing its role in determining the accuracy and convergence of series approximations. For a deeper exploration, consider analysing specific functions and their Taylor series in detail, along with error analysis.

# Euler's Identity and De Moivre's Theorem

## Introduction

Euler's Identity and De Moivre's Theorem are two fundamental concepts in mathematics, specifically in the field of complex analysis. Both play a crucial role in linking trigonometry, exponential functions, and complex numbers.

## Euler's Identity

### Definition
Euler's Identity is an elegant equation that establishes a deep relationship between the most fundamental numbers in mathematics:

$$e^{i\pi} + 1 = 0$$

Here, $e$ is the base of natural logarithms, $i$ is the imaginary unit, and $\pi$ is the ratio of the circumference of a circle to its diameter.

### Significance
This identity is celebrated for its beauty and simplicity, as it combines five fundamental mathematical constants:
1. The number 0.
2. The number 1.
3. The number $\pi$ (Pi).
4. The number $e$ (Euler's Number).
5. The number $i$ (the imaginary unit).

## De Moivre's Theorem

### Definition
De Moivre's Theorem provides a formula for raising complex numbers to any power $n$ (where $n$ is an integer). It states that for any complex number $z$ (written in polar form as $r(\cos \theta + i\sin \theta)$), and any integer $n$, the following holds:

$$[r(\cos \theta + i\sin \theta)]^n = r^n (\cos(n\theta) + i\sin(n\theta))$$

### Applications
This theorem is particularly useful for:
- Calculating powers of complex numbers.
- Simplifying the computation of roots of complex numbers.

## Historical Context

### Euler
Leonhard Euler, a Swiss mathematician and physicist, made numerous contributions to various areas of mathematics, including the introduction of Euler's formula, of which Euler's Identity is a special case.

### De Moivre
Abraham de Moivre, a French mathematician, is known for his work in trigonometry, particularly for De Moivre's Theorem, which he formulated in the 18th century.

## Examples

1. **Euler's Identity Example:**
   To see Euler's Identity in action, simply substitute $\pi$ for $\theta$ in Euler's formula:
   $$e^{i\pi} = \cos(\pi) + i\sin(\pi) = -1$$
   Adding 1 to both sides gives Euler's Identity.

2. **De Moivre's Theorem Example:**
   Consider $z = 1 + i$ (where $r = \sqrt{2}$ and $\theta = \frac{\pi}{4}$). Using De Moivre's Theorem to find $z^3$, we get:
   $$(1 + i)^3 = (\sqrt{2})^3 \left(\cos\left(3 \times \frac{\pi}{4}\right) + i\sin\left(3 \times \frac{\pi}{4}\right)\right)$$

## Conclusion and Test Questions

Understanding Euler's Identity and De Moivre's Theorem provides a fundamental insight into the interplay between complex numbers, trigonometry, and exponential functions.

### Test Questions

1. STARTI [Basic] Question: What is Euler's Identity? Back: Euler's Identity is $e^{i\pi} + 1 = 0$. ENDI
2. STARTI [Basic] Question: State De Moivre's Theorem for a complex number $z$ and integer $n$. Back: De Moivre's Theorem states that $[r(\cos \theta + i\sin \theta)]^n = r^n (\cos(n\theta) + i\sin(n\theta))$. ENDI
3. STARTI [Basic] Question: Using Euler's formula, show how Euler's Identity is derived. Back: By substituting $\theta = \pi$ in Euler's formula, $e^{i\theta} = \cos(\theta) + i\sin(\theta)$, we get $e^{i\pi} = \cos(\pi) + i\sin(\pi) = -1$, leading to Euler's Identity. ENDI

# Evaluating Limits

**Overview:** 
Evaluating limits is a fundamental concept in calculus that deals with finding the value that a function approaches as the input approaches a certain point. This concept is crucial in understanding the behaviour of functions, especially near points of discontinuity or at infinity.

## 1. Direct Substitution
**Definition:** 
Direct substitution involves plugging the point of interest directly into the function, provided the function is continuous at that point.

**Example:**
Consider $\lim_{x \to 3} (2x + 1)$. 
Direct substitution yields $2 \cdot 3 + 1 = 7$.

## 2. Indeterminate Forms
**Definition:** 
An indeterminate form arises when the limit yields an expression like $\frac{0}{0}$ or $\frac{\infty}{\infty}$, which does not have a clear value.

**Example:**
$\lim_{x \to 0} \frac{\sin x}{x}$ results in the indeterminate form $\frac{0}{0}$.

## 3. L'Hôpital's Rule
**Definition:** 
L'Hôpital's Rule is used to evaluate limits involving indeterminate forms. It states that if the limit yields an indeterminate form $\frac{0}{0}$ or $\frac{\infty}{\infty}$, the limit can be computed by taking the derivative of the numerator and denominator separately.

[[Derivation of L'Hôpital's Rule]]

**Example:**
For $\lim_{x \to 0} \frac{\sin x}{x}$, applying L'Hôpital's Rule gives $\lim_{x \to 0} \frac{\cos x}{1}$, which evaluates to 1.

## Historical Context
The concept of limits was formalized in the 17th century, contributing significantly to the development of calculus. L'Hôpital, a French mathematician, published the first known text containing these rules, although the Scottish mathematician John Bernoulli may have discovered them independently.

## Test Questions
1. Evaluate $\lim_{x \to 2} (3x^2 - 2x + 4)$ using direct substitution.
2. Determine if $\lim_{x \to \infty} \frac{x^2 - 1}{x^2 + 1}$ is an indeterminate form and evaluate it.
3. Use L'Hôpital's Rule to find $\lim_{x \to 0} \frac{e^x - 1}{x}$. 

# Even and Odd Functions

## Introduction
Even and odd functions are fundamental concepts in mathematics, particularly in the study of functions in calculus and algebra. Understanding these types of functions aids in graph analysis, problem-solving, and understanding symmetry in mathematical contexts.

## Definitions

### Even Functions
A function $f(x)$ is called an **even function** if for every number $x$ in the function's domain, $f(-x) = f(x)$. This means that the graph of an even function is symmetric with respect to the y-axis. A classic example of an even function is $f(x) = x^2$.

### Odd Functions
A function $f(x)$ is considered an **odd function** if for every $x$ in the function's domain, $f(-x) = -f(x)$. Odd functions exhibit symmetry about the origin. The function $f(x) = x^3$ is a standard example of an odd function.

## Properties and Examples

### Even Functions
- **Symmetry:** Symmetric about the y-axis.
- **Zeroes:** If they exist, occur in symmetric pairs.
- **Integral Property:** The integral of an even function over a symmetric interval $[-a, a]$ is twice the integral from 0 to $a$.
- **Examples:** $f(x) = x^2, \cos(x), |x|$.

### Odd Functions
- **Symmetry:** Symmetric about the origin.
- **Zeroes:** Always include $x = 0$ (if the domain includes 0).
- **Integral Property:** The integral of an odd function over a symmetric interval is 0.
- **Examples:** $f(x) = x^3, \sin(x), x(1 - x^2)$.

## Historical Context
The concepts of even and odd functions were developed as part of the study of polynomial functions and later extended to more complex functions. These concepts are crucial in Fourier analysis, where functions are expressed as a sum of sine and cosine terms (odd and even functions, respectively).

## Applications
- **Physics:** Describing waveforms and harmonic oscillations.
- **Engineering:** Signal processing and symmetrical component analysis.
- **Mathematics:** Simplifying integrals, solving differential equations.

## Test Questions

1. STARTI [Basic] Question: Define an even function. Back: A function $f(x)$ is even if for all $x$ in its domain, $f(-x) = f(x)$. ENDI
2. STARTI [Basic] Question: Give an example of an odd function. Back: An example of an odd function is $f(x) = x^3$. ENDI
3. STARTI [Basic] Question: What is the integral of an odd function over a symmetric interval? Back: The integral of an odd function over a symmetric interval $[-a, a]$ is 0. ENDI

[[Mathematical Functions]] | [[Calculus]] | [[Algebra]]

# Exponential Functions

## Overview
Exponential functions are a cornerstone of mathematics, frequently appearing in various disciplines like physics, economics, and biology. Their general form is $f(x) = a \cdot b^x$, where $a$ and $b$ are constants, and $b$ is positive and not equal to 1. The variable $x$ is typically real-valued.

## Characteristics
1. **Base $b$**: It determines the rate of growth or decay. If $b > 1$, the function models exponential growth, while $0 < b < 1$ models exponential decay.
2. **Coefficient $a$**: This constant affects the initial value of the function. If $a > 0$, the function is always positive, and if $a < 0$, the function takes on negative values.
3. **Asymptotic behaviour**: Exponential functions approach zero but never reach it, forming an asymptote at $y = 0$.
4. **Growth Rate**: Exponential growth is characterized by the rate of change increasing over time, unlike linear growth where the rate is constant.

## Applications
Exponential functions are widely used in various fields:
- **Finance**: Calculating compound interest.
- **Biology**: modelling population growth or decay.
- **Physics**: Radioactive decay and cooling processes.

## Historical Context
The concept of exponential growth first appeared in the work of John Napier in the early 17th century, focusing on logarithms and their properties. Exponential functions were later formalized by Euler in the 18th century, who also introduced the constant $e \approx 2.71828$, now known as Euler's number, a fundamental base of natural logarithms and exponential functions.

## Examples
1. Compound Interest: If $P$ is the principal amount, $r$ the interest rate, and $t$ the time in years, the future value $A$ is given by $A = P \cdot e^{rt}$.
2. Population Growth: If $P_0$ is the initial population, and $r$ is the growth rate, the population after $t$ years is $P(t) = P_0 \cdot e^{rt}$.

## Test Questions
1. What is the general form of an exponential function?
   - Back: $f(x) = a \cdot b^x$, where $a$ and $b$ are constants and $b > 0, b \neq 1$.

2. If a population doubles every 5 years, what is the exponential growth model?
   - Back: $P(t) = P_0 \cdot 2^{t/5}$, where $P_0$ is the initial population and $t$ is time in years.

3. Calculate the future value of a $1000 investment after 10 years at an annual interest rate of 5%, compounded continuously.
   - Back: $A = 1000 \cdot e^{0.05 \times 10} \approx 1648.72$.

# Extreme Value Theorem, Fermat's Theorem, and Critical Points

## Extreme Value Theorem (EVT)

### Overview
The Extreme Value Theorem is a fundamental theorem in calculus which states that if a function $f$ is continuous on a closed interval $[a, b]$, then $f$ must attain a maximum and a minimum, at least once each, on $[a, b]$.

### Historical Context
Developed as part of the foundational work in calculus, EVT has roots in the ideas of mathematicians like Bernard Bolzano and Karl Weierstrass, who were pivotal in formalizing concepts of continuity and limits.

### Application
EVT is crucial in optimization problems where finding maximum and minimum values is essential, such as in economics, engineering, and physics.

### Obsidian Link
For more on continuous functions, see [[Continuity in Calculus]].

---

## Fermat's Theorem on Stationary Points

### Overview
Fermat's Theorem states that if a function $f$ has a local maximum or minimum at a point $c$ and $f$ is differentiable at $c$, then the derivative of $f$ at $c$ is zero, i.e., $f'(c) = 0$.

### Historical Context
Named after Pierre de Fermat, a 17th-century mathematician, this theorem plays a crucial role in identifying potential extrema, particularly in the field of calculus of variations.

### Application
Fermat's Theorem is used in finding local extrema (maximum or minimum values) of differentiable functions, an essential process in fields such as economics, physics, and engineering optimization.

### Obsidian Link
For applications in optimization, see [[Optimization Techniques in Calculus]].

---

## Critical Points

### Overview
Critical points of a function are points where the function's derivative is either zero or undefined. These are potential candidates for being local maxima or minima of the function.

### Application
Identifying critical points is a fundamental step in graphing functions and solving optimization problems in various scientific and engineering fields.

### Obsidian Link
For related concepts, see [[Derivatives in Calculus]] and [[Optimization Techniques in Calculus]].

---

## Test Questions

1. **STARTI [Basic] Question:** State the Extreme Value Theorem. Back: The Extreme Value Theorem states that if a function $f$ is continuous on a closed interval $[a, b]$, then $f$ must attain a maximum and a minimum, at least once each, on $[a, b]$. ENDI
2. **STARTI [Basic] Question:** What does Fermat's Theorem state about stationary points? Back: Fermat's Theorem states that if a function $f$ has a local maximum or minimum at a point $c$ and $f$ is differentiable at $c$, then the derivative of $f$ at $c$ is zero, i.e., $f'(c) = 0$. ENDI
3. **STARTI [Basic] Question:** Describe what critical points of a function are. Back: Critical points of a function are points where the function's derivative is either zero or undefined, and they are potential candidates for being local maxima or minima of the function. ENDI

# First Principles and Formal Definition of Integration

## Introduction
Integration is a fundamental concept in calculus, central to many areas of mathematics, physics, engineering, and other sciences. It extends the concept of summing up infinitely many small quantities, offering a way to calculate areas, volumes, and other quantities that require accumulation.

## Historical Context
The concept of integration can be traced back to ancient mathematicians like Archimedes, who used methods resembling integration to calculate areas and volumes. The formal development of calculus in the 17th century by Newton and Leibniz provided a more rigorous foundation for integration, framing it as the inverse process of differentiation.

## First Principles of Integration
### Riemann Sums
At the heart of understanding integration from first principles is the concept of a Riemann sum. It involves dividing the region to be integrated (under a curve, for example) into small segments, approximating the area of each segment, and then summing these areas. The process can be expressed as:

1. Divide the interval $[a, b]$ into $n$ subintervals.
2. In each subinterval, choose a point $x_i$.
3. The area of each rectangle is $f(x_i) \Delta x$, where $\Delta x = \frac{b-a}{n}$.
4. The Riemann sum is $\sum_{i=1}^{n} f(x_i) \Delta x$.

As $n$ approaches infinity, the Riemann sum approaches the exact area, leading to the concept of the definite integral.

### Formal Definition
The formal definition of the definite integral of a function $f$ from $a$ to $b$ is given by:

$$\int_{a}^{b} f(x) \,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i) \Delta x$$

This expression is read as "the integral from $a$ to $b$ of $f(x)$ with respect to $x$" and represents the limit of the Riemann sums as the number of subintervals goes to infinity.

## Applications
Integration is used extensively in various fields:
- In physics, for calculating quantities like work, energy, and electric potential.
- In engineering, for design and analysis in multiple domains.
- In economics, to model growth and accumulation.
- In probability, to find distributions and expectations.

## Test Questions
1. STARTI [Basic] Question: What is the primary difference between a Riemann sum and a definite integral? Back: A Riemann sum is an approximation made by summing the areas of rectangles under a curve, while a definite integral is the exact area, obtained by taking the limit of the Riemann sum as the number of rectangles approaches infinity. ENDI
2. STARTI [Basic] Question: How would you express the integral of a function $f(x)$ from 0 to 2 using the formal definition? Back: $\int_{0}^{2} f(x) \,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i) \frac{2}{n}$, where $x_i$ is a sample point in each subinterval. ENDI
3. STARTI [Basic] Question: In what situations is it impossible to use Riemann sums to define an integral? Back: Riemann sums and the corresponding definite integrals cannot be used when the function $f(x)$ is not defined or is discontinuous in the interval $[a, b]$. ENDI

---
Feel free to add more content or adjust existing content to suit the specific needs of your Obsidian vault. Hyperlinks can be integrated for related topics like "calculus", "Riemann sums", or specific mathematicians for a richer learning experience.

# Graphs of Functions

## Introduction
The graph of a function is a visual representation of the relationship between its inputs (usually denoted as $x$) and outputs (denoted as $y$ or $f(x)$). It's an essential concept in mathematics, particularly in calculus and analysis, as it helps in understanding the behaviour of functions.

## Definition
A graph of a function $f: X \rightarrow Y$ is the set of ordered pairs $(x, f(x))$ where $x$ is in the domain of $f$. In the Cartesian coordinate system, these pairs are represented as points in a two-dimensional plane.

## Characteristics
1. **Domain and Range**: The domain of a function is the set of all possible inputs, while the range is the set of all possible outputs. The graph shows the extent of these in the $x$- and $y$-axes respectively.
2. **Continuity**: A function is continuous if its graph can be drawn without lifting the pencil from the paper.
3. **Asymptotes**: These are lines that the graph of a function approaches but never touches.
4. **Intercepts**: Points where the graph intersects the axes. The $x$-intercept is where $f(x) = 0$, and the $y$-intercept is where $x = 0$.
5. **Slope and Concavity**: Indicate the rate of change and the direction of the curve, respectively.

## Types of Graphs
1. **Linear**: Straight line graph, indicating a constant rate of change.
2. **Quadratic**: Parabolic graph, representing polynomial functions of degree 2.
3. **Exponential**: Rapidly increasing or decreasing graph, common in growth and decay problems.
4. **Logarithmic**: The inverse of exponential functions, useful in scenarios involving logarithmic scales.
5. **Trigonometric**: Representing functions like sine, cosine, and tangent, these graphs are periodic.

## Historical Context
The use of graphs to represent functions dates back to the 17th century, with significant contributions from mathematicians like René Descartes and Isaac Newton. The Cartesian coordinate system, named after Descartes, is fundamental in graphing functions.

## Example: Graphing a Linear Function
Consider the linear function $f(x) = 2x + 3$. Its graph can be plotted by finding two points that satisfy the equation and drawing a line through them. For example, when $x = 0$, $y = 3$ and when $x = 1$, $y = 5$.

## Test Questions
1. **Question:** What is the range of the function $f(x) = x^2$ when the domain is $x \geq 0$? **Back:** The range is $y \geq 0$ because a square of a non-negative number is always non-negative.
2. **Question:** How do you identify a function's $y$-intercept on its graph? **Back:** The $y$-intercept is the point where the graph crosses the $y$-axis, which occurs when $x = 0$.
3. **Question:** What does the slope of a function's graph represent? **Back:** The slope represents the rate of change of the function.

For further study, you may refer to the related topics [[Calculus]], [[Algebra]], and [[Coordinate Geometry]].

# Higher-Degree Approximations

## Introduction
Higher-degree approximations are a fundamental concept in calculus and numerical analysis, used to estimate the values of functions. They expand upon the concept of linear approximation (first-degree) by including higher-degree terms, making them more accurate for approximating non-linear functions over a larger range.

## Taylor Series
A key tool for higher-degree approximations is the Taylor series. The Taylor series of a function $f(x)$ about a point $a$ is given by:

$$f(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \frac{f'''(a)}{3!}(x - a)^3 + \cdots$$
In Sigma notation, this is given by:
$$
\sum_{n=0}^\infty\frac{f^n(a)}{n!}(x-a)^n
$$
n
### Example
Consider the function $f(x) = e^x$. Its Taylor series expansion about $a = 0$ (also known as the Maclaurin series) is:

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

This series can be truncated to obtain a higher-degree approximation of $e^x$.

## Applications
1. **Physics and Engineering:** Used to solve differential equations and in numerical methods for complex systems.
2. **Economics:** In modelling and forecasting economic variables.
3. **Statistics:** For creating models and in hypothesis testing.

## Advantages and Limitations
- **Advantages:** Higher accuracy over linear approximations, especially near the point of expansion.
- **Limitations:** Complexity increases with degree, and accuracy can decrease far from the expansion point.

## Test Questions
1. STARTI [Basic] Question: What is the third-degree Taylor polynomial for $f(x) = sin(x)$ around $a = 0$? Back: The third-degree Taylor polynomial is $x - x^3/6$. ENDI
2. STARTI [Basic] Question: Why are higher-degree approximations more accurate near the point of expansion? Back: Higher-degree terms capture more of the function's curvature, providing a better fit near the expansion point. ENDI
3. STARTI [Basic] Question: Discuss the limitations of using a high-degree Taylor series for approximation. Back: While more accurate near the expansion point, high-degree polynomials can lead to increased complexity and less accuracy far from the point due to the phenomenon of Runge's phenomenon. ENDI

---

This note on Higher-Degree Approximations explores the concept’s basis, its application in various fields, and both its advantages and limitations. For further exploration, consider examining specific examples in different fields or delving deeper into the mathematical properties of Taylor series.

# Hyperbolic Functions in Mathematics

## Introduction
Hyperbolic functions are analogues of the ordinary trigonometric, or circular, functions. They are widely used in various areas of mathematics, including in the study of trigonometry, complex numbers, and calculus. These functions also appear in the solutions of certain differential equations and in the description of certain geometrical shapes.

## Definition
Hyperbolic functions are defined through exponential functions. The primary hyperbolic functions are:
1. **Hyperbolic Sine ($\sinh$)**: Defined as $\sinh x = \frac{e^x - e^{-x}}{2}$
2. **Hyperbolic Cosine ($\cosh$)**: Defined as $\cosh x = \frac{e^x + e^{-x}}{2}$
3. **Hyperbolic Tangent ($\tanh$)**: Defined as $\tanh x = \frac{\sinh x}{\cosh x}$

Other functions like hyperbolic cotangent ($\coth$), secant ($\text{sech}$), and cosecant ($\text{csch}$) are derived similarly to their trigonometric counterparts.

## Properties
1. **Relation to Exponential Function**: They are derived from and closely related to the exponential function $e^x$.
2. **Odd and Even Functions**: $\sinh(x)$ is an odd function, and $\cosh(x)$ is an even function.
3. **Hyperbolic Identity**: Similar to the Pythagorean identity in trigonometry, $\cosh^2 x - \sinh^2 x = 1$.

## Applications
- **Calculus**: Used in solving differential equations and integrals.
- **Geometry**: Describes the shape of a hanging cable or chain, known as a catenary.
- **Physics**: Appear in various physical contexts, such as in the theory of special relativity and wave equations.

## Historical Context
The hyperbolic functions were first introduced in the 18th century. Johann Heinrich Lambert coined the term "hyperbolic functions" in 1768 due to their relation to the hyperbola, similar to how circular functions are related to the circle.

## Examples
1. **Special Relativity**: In Einstein’s theory of special relativity, hyperbolic functions describe rapidity, a measure of velocity.
2. **Geometry of Hyperbolas**: In the Cartesian plane, the hyperbola $x^2 - y^2 = 1$ relates to the functions $\cosh$ and $\sinh$.

## Test Questions
1. **Basic**: What is the hyperbolic identity involving $\cosh$ and $\sinh$?
   - Back: $\cosh^2 x - \sinh^2 x = 1$
2. **Application**: How are hyperbolic functions used in the study of special relativity?
   - Back: They are used to describe rapidity, a measure of velocity.
3. **Historical**: Who first coined the term "hyperbolic functions" and when?
   - Back: Johann Heinrich Lambert in 1768.

# Implicit Differentiation Using Partial Derivatives

## Introduction
Implicit differentiation is a technique used in calculus to find the derivative of an implicitly defined function. Unlike explicit functions where $y$ is given explicitly as a function of $x$ (e.g., $y = f(x)$), implicit functions are presented in a form where $y$ cannot be easily isolated (e.g., $F(x, y) = 0$). 

When dealing with such functions, we often use partial derivatives to facilitate the process of differentiation. This approach is particularly useful in multivariable calculus, where functions are defined in terms of more than one variable.

## Conceptual Overview
In implicit differentiation, we differentiate both sides of an equation with respect to $x$ while treating $y$ as a function of $x$. This involves applying the chain rule for derivatives. The general process is as follows:

1. **Differentiate Both Sides**: Given an equation $F(x, y) = 0$, differentiate both sides with respect to $x$, treating $y$ as a function of $x$.

2. **Apply the Chain Rule**: When differentiating terms involving $y$, apply the chain rule. This means that for each occurrence of $y$, you'll add a term involving $\frac{dy}{dx}$.

3. **Solve for $\frac{dy}{dx}$**: After differentiating, you'll have an equation involving $\frac{dy}{dx}$. Solve this equation to find the derivative.

## Example
Consider the circle defined by the equation $x^2 + y^2 = r^2$, where $r$ is the radius.

Differentiating implicitly, we get:
$$2x + 2y\frac{dy}{dx} = 0$$

Solving for $\frac{dy}{dx}$, we find:
$$\frac{dy}{dx} = -\frac{x}{y}$$

This formula gives the slope of the tangent line to the circle at any point $(x, y)$.

## Historical Context
Implicit differentiation has been a fundamental tool in calculus since the time of Leibniz and Newton. Its development was crucial in solving complex geometrical problems and in the advancement of differential equations.

## Test Questions
1. STARTI [Basic] Question: What is the implicit derivative of $x^2 + xy + y^2 = 7$ with respect to $x$? Back: $2x + y + x\frac{dy}{dx} + 2y\frac{dy}{dx} = 0$. ENDI
2. STARTI [Basic] Question: For the ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, find $\frac{dy}{dx}$ at any point. Back: Differentiating implicitly, $\frac{2x}{a^2} + \frac{2y}{b^2}\frac{dy}{dx} = 0$. Solving for $\frac{dy}{dx}$, we get $\frac{dy}{dx} = -\frac{b^2x}{a^2y}$. ENDI
3. STARTI [Basic] Question: Explain how the chain rule is applied in implicit differentiation. Back: In implicit differentiation, when a term involves $y$, which is a function of $x$, the chain rule is applied. This results in an additional $\frac{dy}{dx}$ term for each $y$-containing term during differentiation. ENDI

# Integrals Over General Areas

## Introduction
Integral calculus is a fundamental part of mathematics with extensive applications in various fields such as physics, engineering, and economics. While most students are familiar with integrals over simple shapes or intervals, integrating over general areas extends this concept to more complex domains.

## Concept
The integral over a general area involves finding the sum of values of a function across a region in the plane. This is often visualized as calculating the area under a curve over an irregular region or the volume under a surface.

### Rectangular Coordinates
In rectangular coordinates (x, y), the double integral of a function $f(x, y)$ over a region $R$ is denoted as:

$$\iint_R f(x, y) \, dx \, dy$$

This represents the accumulated sum of $f(x, y)$ over every infinitesimal rectangle $dx \, dy$ within $R$.

### Polar Coordinates
For areas best described in polar coordinates (r, θ), the double integral changes to accommodate the radial and angular components:

$$\iint_R f(r, \theta) \, r \, dr \, d\theta$$

Here, the extra $r$ term accounts for the "wedge-shaped" elements of area in polar coordinates.

## Applications
1. **Physics**: Calculating moments, center of mass, and electric and magnetic fields over irregular shapes.
2. **Engineering**: Determining stress, strain, and heat distribution over complex structures.
3. **Economics**: Evaluating integrals in multivariate models for optimization problems.

## Example in Rectangular Coordinates
Consider the region bounded by $y = x^2$ and $y = 2x$. To find the integral of $f(x, y) = xy$ over this region:

1. Determine the bounds of integration.
2. Set up the double integral.
3. Evaluate using iterative integration.

## Example in Polar Coordinates
Integrating $f(r, \theta) = r^2$ over a circular region with radius $R$ involves:

1. Setting $0 \leq r \leq R$ and $0 \leq \theta \leq 2\pi$.
2. Computing the double integral $\iint_R r^2 \, r \, dr \, d\theta$.

## Test Questions
1. STARTI [Basic] Question: What is the purpose of integrating over general areas? Back: Integrating over general areas extends the concept of integration to complex domains and is used to calculate the sum of values of a function across a region in the plane. ENDI
2. STARTI [Basic] Question: How does the double integral change when shifting from rectangular to polar coordinates? Back: In polar coordinates, the double integral includes an extra 'r' term to account for the radial component, making it $\iint_R f(r, \theta) \, r \, dr \, d\theta$. ENDI
3. STARTI [Basic] Question: Describe the process of setting up and evaluating a double integral over a general area in rectangular coordinates. Back: First, determine the bounds of integration based on the region's limits. Next, set up the double integral $\iint_R f(x, y) \, dx \, dy$. Finally, evaluate the integral using iterative integration, integrating first with respect to one variable, then the other. ENDI

This note offers a foundational understanding of integrals over general areas, bridging the gap between simple integrals and their applications in complex domains. For further exploration, consider extending these concepts to triple integrals and beyond.

# Intercepts with Axes and Symmetry
## Introduction

In mathematics, understanding the concepts of intercepts and symmetry is crucial, especially in the study of functions and graphs. These concepts are fundamental in algebra, calculus, and other areas of mathematics, providing insights into the behavior of functions and their graphical representations.

## Intercepts with Axes

### Definition

**X-intercept:** A point where the graph of a function or an equation crosses the x-axis. At this point, the y-coordinate is zero.

**Y-intercept:** A point where the graph of a function or an equation crosses the y-axis. Here, the x-coordinate is zero.

### Finding Intercepts

- **X-intercept:** Set $y = 0$ in the equation and solve for $x$.
- **Y-intercept:** Set $x = 0$ in the equation and solve for $y$.

#### Example

Consider the linear equation $y = 2x + 3$:
- X-intercept: Set $y = 0$, $0 = 2x + 3$ ⇒ $x = -\frac{3}{2}$.
- Y-intercept: Set $x = 0$, $y = 2(0) + 3$ ⇒ $y = 3$.

## Symmetry

### Types of Symmetry

1. **Axial Symmetry:** The graph is symmetrical about a line (usually the y-axis or x-axis).
2. **Origin Symmetry:** The graph is symmetrical about the origin.

### Testing for Symmetry

- **Y-axis Symmetry:** Replace $x$ with $-x$ in the equation. If the equation remains unchanged, the graph is symmetric about the y-axis.
- **Origin Symmetry:** Replace $x$ with $-x$ and $y$ with $-y$. If the equation remains unchanged, the graph is symmetric about the origin.

#### Example

Consider the equation $y = x^2$:
- Replacing $x$ with $-x$ gives $y = (-x)^2 = x^2$, so it's symmetric about the y-axis.

## Test Questions

1. STARTI [Basic] Question: How do you find the x-intercept of a function? Back: Set $y = 0$ in the function and solve for $x$. ENDI
2. STARTI [Basic] Question: What does it mean if a graph is symmetric about the y-axis? Back: It means that for every point $(x, y)$ on the graph, there is a corresponding point $(-x, y)$ also on the graph. ENDI
3. STARTI [Basic] Question: If a function's equation remains unchanged when $x$ is replaced with $-x$ and $y$ is replaced with $-y$, what type of symmetry does the graph exhibit? Back: The graph exhibits origin symmetry. ENDI

# Note on Intermediate Value Theorem

## Introduction
The Intermediate Value Theorem (IVT) is a fundamental theorem in calculus, specifically in the field of real analysis. It's an essential tool for understanding the behaviour of continuous functions on real number intervals. 

## Definition
The theorem states that if $f$ is a continuous function on the interval $[a, b]$ and $N$ is any number between $f(a)$ and $f(b)$, then there exists at least one number $c$ in the interval $[a, b]$ such that $f(c) = N$. 

Mathematically, it's expressed as:
- Let $f: [a, b] \rightarrow \mathbb{R}$ be a continuous function.
- If $N$ is any number between $f(a)$ and $f(b)$,
- Then there exists a $c$ in $[a, b]$ such that $f(c) = N$.

## Historical Context
The IVT has its roots in the early development of calculus. It was implicitly used by mathematicians like Bolzano in the 19th century, but the formal and rigorous definition was established as part of the foundations of real analysis.

## Applications and Examples
### Finding Roots
The IVT is often used to show that a function has a root (a point where the function equals zero) within an interval. For example, if a continuous function has values of opposite signs at the ends of an interval, the IVT assures us that there is at least one root within that interval.

### Ensuring Continuity
The theorem also serves as a test for continuity. If a function fails to satisfy the conditions of the IVT on an interval, it's not continuous on that interval.

### Example
Consider the function $f(x) = x^2 - 2$ on the interval $[0, 2]$. We have $f(0) = -2$ and $f(2) = 2$. Since 0 lies between -2 and 2, by the IVT, there exists a $c$ in $[0, 2]$ such that $f(c) = 0$. This is the root of the equation $x^2 - 2 = 0$, which is $\sqrt{2}$.

## Conclusion and Test Questions
Understanding the Intermediate Value Theorem is crucial for analysing the behaviour of continuous functions. It's not only a theoretical tool but also has practical applications in finding roots and ensuring the continuity of functions.

### Test Questions
1. If $f(x)$ is a continuous function on the interval $[-1, 3]$ and $f(-1) = -4$ and $f(3) = 6$, show that there exists a $c$ such that $f(c) = 0$.
2. Provide an example of a function that does not satisfy the conditions of the IVT on a given interval.
3. Explain why the IVT cannot be applied to functions that are not continuous. 

---

For more related concepts, explore:
- [[Continuity in Calculus]]
- [[Root-Finding Algorithms]]
- [[Bolzano's Theorem]]

# Inverse Functions

## Introduction
Inverse functions are foundational in mathematics, particularly in algebra and calculus. They provide a way to 'undo' the action of a function. For example, if you have a function that adds 2 to any number, its inverse would subtract 2, returning you to your original number.

## Definition
A function $f: X \rightarrow Y$ has an inverse $f^{-1}$ if, for every element $y$ in the codomain $Y$, there is an element $x$ in the domain $X$ such that $f^{-1}(y) = x$. This implies that $f(f^{-1}(y)) = y$ and $f^{-1}(f(x)) = x$. The function $f$ must be bijective (both injective and surjective) to have an inverse.

## Examples
1. **Addition/Subtraction**: If $f(x) = x + 5$, then its inverse $f^{-1}(x) = x - 5$.
2. **Multiplication/Division**: For $f(x) = 3x$, the inverse is $f^{-1}(x) = \frac{x}{3}$.
3. **Exponential/Logarithmic Functions**: The inverse of $f(x) = e^x$ is $f^{-1}(x) = \ln(x)$.

## Properties
1. **Symmetry**: The graph of $f^{-1}$ is a reflection of the graph of $f$ across the line $y = x$.
2. **Composition**: $f(f^{-1}(x)) = x$ and $f^{-1}(f(x)) = x$.
3. **Domain and Range**: The domain of $f^{-1}$ is the range of $f$, and vice versa.

## Finding Inverse Functions
To find the inverse of a function:
1. Replace $f(x)$ with $y$.
2. Solve the equation for $x$ in terms of $y$.
3. Replace $y$ with $f^{-1}(x)$.

## Historical Context
The concept of inverse functions has been around since the introduction of functions themselves. It gained prominence with the development of calculus in the 17th century, especially in the work of mathematicians like Newton and Leibniz.

## Test Questions
1. **Basic**: Given $f(x) = 2x - 4$, find $f^{-1}(x)$.
   Back: $f^{-1}(x) = \frac{x + 4}{2}$.
2. **Intermediate**: Show that the inverse of $f(x) = \frac{1}{x}$ is itself.
   Back: Replacing $f(x)$ with $y$, we get $y = \frac{1}{x}$. Solving for $x$ gives $x = \frac{1}{y}$, so $f^{-1}(x) = \frac{1}{x}$, which is $f(x)$.
3. **Advanced**: Prove that the function $f(x) = x^3$ has an inverse.
   Back: $f(x) = x^3$ is a bijective function (both injective and surjective) since every $y$ value has a unique $x$ value. Therefore, it has an inverse, which is $f^{-1}(x) = \sqrt[3]{x}$.

[[Algebra]] | [[Calculus]]

# Inverse Hyperbolic Functions

## Introduction

Inverse hyperbolic functions are the inverses of the hyperbolic functions. Just as trigonometric functions play a pivotal role in the study of triangles and periodic phenomena, hyperbolic functions are crucial in the study of hyperbolas and have applications in areas such as calculus, complex analysis, and physics, particularly in the theory of relativity.

### Hyperbolic Functions Overview

Before diving into their inverses, let's briefly recall the hyperbolic functions:

- **Hyperbolic Sine (sinh):** Defined as $\sinh(x) = \frac{e^x - e^{-x}}{2}$
- **Hyperbolic Cosine (cosh):** Defined as $\cosh(x) = \frac{e^x + e^{-x}}{2}$
- **Hyperbolic Tangent (tanh):** Defined as $\tanh(x) = \frac{\sinh(x)}{\cosh(x)}$

These functions have properties and graphs similar to, yet distinct from, their trigonometric counterparts.

## Inverse Hyperbolic Functions

The inverse hyperbolic functions are defined as follows:

1. **Inverse Hyperbolic Sine (arsinh or sinh<sup>-1</sup>):**
   $$\text{arsinh}(x) = \ln\left(x + \sqrt{x^2 + 1}\right)$$
   It is the inverse of the hyperbolic sine function.

2. **Inverse Hyperbolic Cosine (arcosh or cosh<sup>-1</sup>):**
   $$\text{arcosh}(x) = \ln\left(x + \sqrt{x^2 - 1}\right)$$
   This function is defined for $x \geq 1$.

3. **Inverse Hyperbolic Tangent (artanh or tanh<sup>-1</sup>):**
   $$\text{artanh}(x) = \frac{1}{2} \ln\left(\frac{1 + x}{1 - x}\right)$$
   It is defined for $-1 < x < 1$.

### Properties

- **Range:** The range of arsinh and artanh is all real numbers, whereas the range of arcosh is from 0 to infinity.
- **Derivatives:** The derivatives of these functions are significant in calculus. For example, the derivative of arsinh(x) is $\frac{1}{\sqrt{x^2 + 1}}$.

### Applications

Inverse hyperbolic functions are used in various branches of science and engineering, including in the calculation of angles and distances in hyperbolic geometry, in solving certain differential equations, and in describing phenomena in physics such as wave propagation in hyperbolic space.

## Test Questions

1. **Question:** Describe the domain and range of the inverse hyperbolic sine function. **Back:** The domain is all real numbers, and the range is also all real numbers.
2. **Question:** What is the derivative of the inverse hyperbolic tangent function? **Back:** The derivative of artanh(x) is $\frac{1}{1 - x^2}$.
3. **Question:** How is the inverse hyperbolic cosine function defined for $x \geq 1$? **Back:** The inverse hyperbolic cosine function for $x \geq 1$ is defined as $\text{arcosh}(x) = \ln\left(x + \sqrt{x^2 - 1}\right)$.

# Limits at Infinity

## Introduction
In mathematics, particularly in calculus, the concept of limits at infinity is crucial for understanding the behaviour of functions as they approach infinitely large (or small) values. This concept helps in analysing and understanding the asymptotic behaviour of functions.

## Definition
The limit of a function $f(x)$ as $x$ approaches infinity, denoted as $\lim_{x \to \infty} f(x)$, is the value that $f(x)$ gets closer to as $x$ becomes arbitrarily large. Similarly, the limit of $f(x)$ as $x$ approaches negative infinity, denoted as $\lim_{x \to -\infty} f(x)$, is the value that $f(x)$ approaches as $x$ becomes arbitrarily large in the negative direction.

## Formal Definition
1. **Positive Infinity**: We say $\lim_{x \to \infty} f(x) = L$ if for every $\epsilon > 0$, there exists a $M$ such that if $x > M$, then $|f(x) - L| < \epsilon$.
2. **Negative Infinity**: We say $\lim_{x \to -\infty} f(x) = L$ if for every $\epsilon > 0$, there exists a $N$ such that if $x < N$, then $|f(x) - L| < \epsilon$.

## Examples
1. **Polynomial Functions**: For any polynomial function $p(x)$, $\lim_{x \to \infty} p(x)$ is either $\infty$, $-\infty$, or undefined, depending on the leading term.
2. **Rational Functions**: For a rational function $\frac{p(x)}{q(x)}$, where $p(x)$ and $q(x)$ are polynomials, the limit at infinity depends on the degrees of $p(x)$ and $q(x)$.

## Applications
- **Asymptotic behaviour**: Understanding how a function behaves as it approaches infinity is crucial in many areas of mathematics, including calculus and analysis.
- **Curve Sketching**: Limits at infinity are used to determine horizontal asymptotes of functions, which are essential in sketching graphs.

## Conclusion
The concept of limits at infinity is fundamental in calculus and helps in understanding the behaviour of functions over large scales. It's a critical tool for evaluating the long-term behaviour of various mathematical models.

---

## Test Questions
1. Calculate $\lim_{x \to \infty} \frac{2x^3 - 1}{x^3 + 5}$.
2. Determine if $\lim_{x \to -\infty} \sqrt{x^2 + 1}$ exists, and if so, find its value.
3. Evaluate $\lim_{x \to \infty} e^{-x}$ and explain why it approaches its limit.

# Linearisation and Quadratic Approximations

## Introduction

Linearisation and quadratic approximations are powerful mathematical techniques used in calculus and applied mathematics. They are used to approximate complex functions using simpler linear or quadratic functions, making them easier to analyse and work with.

## Linearisation

Linearisation is the process of approximating a function near a point using a linear function. The linear approximation of a function $f(x)$ at a point $a$ is given by the tangent line at that point. The formula for the linear approximation of $f(x)$ at $a$ is:

$$L(x) = f(a) + f'(a)(x - a)$$

### Example
Consider the function $f(x) = \sin(x)$. The linear approximation of $f(x)$ at $a = 0$ is:
$$L(x) = \sin(0) + \cos(0)(x - 0) = x$$

## Quadratic Approximations

Quadratic approximation takes this a step further by using a second-degree polynomial to approximate the function. The formula for the quadratic approximation of $f(x)$ at $a$ is:

$$Q(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2}(x - a)^2$$

### Example
For $f(x) = e^x$, the quadratic approximation at $a = 0$ is:
$$Q(x) = e^0 + e^0(x - 0) + \frac{e^0}{2}(x - 0)^2 = 1 + x + \frac{x^2}{2}$$

## Applications

- **Engineering**: Used in control systems and optimizations.
- **Economics**: Applied in marginal analysis.
- **Physics**: Helps simplify complex equations.

## Test Questions

1. STARTI [Basic] Question: What is the linear approximation of $f(x) = \ln(x)$ at $a = 1$? Back: $L(x) = x - 1$. ENDI
2. STARTI [Basic] Question: How do you find the quadratic approximation of a function at a given point? Back: Evaluate the function and its first and second derivatives at the point, and substitute these into the quadratic approximation formula. ENDI
3. STARTI [Basic] Question: If $f(x) = \cos(x)$, what is the quadratic approximation of $f$ at $a = \frac{\pi}{4}$? Back: $Q(x) = \frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2}(x - \frac{\pi}{4}) - \frac{\sqrt{2}}{4}(x - \frac{\pi}{4})^2$. ENDI

---

*For further exploration, consider how linearisation and quadratic approximations could be applied to real-world scenarios in your field of interest.*

# Local Maxima and Minima, Concavity, and Points of Inflection

## Introduction
This note delves into the fundamental concepts of calculus: local maxima and minima, concavity, and points of inflection. These concepts are crucial in understanding the behaviour of functions and their graphs.

## Local Maxima and Minima

### Definition
- **Local Maximum**: A function $f(x)$ has a local maximum at $x = a$ if $f(a)$ is greater than all values of $f(x)$ near $a$.
- **Local Minimum**: A function $f(x)$ has a local minimum at $x = a$ if $f(a)$ is less than all values of $f(x)$ near $a$.

### Finding Local Extrema
- **First Derivative Test**: If $f'(a) = 0$ and the sign of $f'(x)$ changes at $x = a$, then $f(x)$ has a local extremum at $a$.
- **Second Derivative Test**: If $f'(a) = 0$ and $f''(a) > 0$, $f(a)$ is a local minimum. If $f''(a) < 0$, $f(a)$ is a local maximum.

## Concavity

### Definition
- A function is **concave up** on an interval if its graph lies above its tangent lines on that interval.
- A function is **concave down** on an interval if its graph lies below its tangent lines on that interval.

### Determining Concavity
- **Second Derivative Test for Concavity**: If $f''(x) > 0$ on an interval, the function is concave up on that interval. If $f''(x) < 0$, it's concave down.

## Points of Inflection

### Definition
- A point of inflection is a point on the graph of a function at which the concavity changes.

### Finding Points of Inflection
- Solve $f''(x) = 0$ to find potential points of inflection.
- Confirm a change in concavity around these points to validate them as points of inflection.

## Historical Context
These concepts were developed in the context of calculus, a field predominantly developed by Isaac Newton and Gottfried Wilhelm Leibniz in the 17th century. Their work on derivatives and tangents laid the foundation for understanding these properties of functions.

## Examples
- Consider $f(x) = x^3 - 3x^2 - 9x + 5$. Analysing its first and second derivatives helps determine its local maxima and minima, concavity, and points of inflection.
- For a trigonometric function like $f(x) = \sin(x)$, observe how these concepts manifest in a periodic function.

## Test Questions

1. Given $f(x) = x^3 - 6x^2 + 9x + 1$, find any local maxima or minima.
2. Determine the concavity of $f(x) = 2x^3 - 3x^2 - 12x + 5$ on the interval $[-2, 3]$.
3. Identify the points of inflection for the function $f(x) = x^4 - 4x^3 + 6x^2$.

Remember, understanding these concepts not only helps in analysing mathematical functions but also in various real-world applications like physics, economics, and engineering.

# Logarithmic Differentiation

Logarithmic differentiation is a powerful technique in calculus, especially useful for differentiating products, quotients, and powers where traditional rules of differentiation like the product rule and quotient rule are cumbersome. This method involves taking the natural logarithm of both sides of an equation and then differentiating.

## Concept and Process

1. **Taking Logarithms**: Given a function $y = f(x)$, we take the natural logarithm of both sides: $\ln(y) = \ln(f(x))$.
2. **Applying Properties of Logarithms**: Utilize the properties of logarithms to simplify the equation. For instance, $\ln(a \cdot b) = \ln(a) + \ln(b)$, and $\ln(a^b) = b \ln(a)$.
3. **Differentiating**: Differentiate both sides with respect to $x$. Remember that $\frac{d}{dx}[\ln(y)] = \frac{1}{y} \frac{dy}{dx}$.
4. **Solving for $\frac{dy}{dx}$**: Rearrange and solve for $\frac{dy}{dx}$.

## Applications

Logarithmic differentiation is particularly useful in cases where direct differentiation is not straightforward, such as:

- Functions with variable bases and exponents, e.g., $y = x^x$.
- Complex products and quotients, e.g., $y = \frac{x^2 \cdot \sin(x)}{\sqrt{e^x + 3}}$.

## Example

Consider $y = x^x$. Applying logarithmic differentiation:

1. Take logarithms: $\ln(y) = \ln(x^x)$.
2. Simplify using log properties: $\ln(y) = x \ln(x)$.
3. Differentiate both sides: $\frac{1}{y} \frac{dy}{dx} = \ln(x) + x \cdot \frac{1}{x}$.
4. Solve for $\frac{dy}{dx}$: $\frac{dy}{dx} = y(\ln(x) + 1) = x^x(\ln(x) + 1)$.

## Test Questions

1. Question: Use logarithmic differentiation to find the derivative of $y = \frac{x^3}{\sqrt{e^{2x}}}$. Back: Apply logarithmic differentiation step by step to find $\frac{dy}{dx}$.
2. Question: Explain why logarithmic differentiation is advantageous for the function $y = (sin(x))^x$. Back: Discuss the complexity of the function and the simplification achieved through logarithmic differentiation.
3. Question: Differentiate $y = \prod_{i=1}^{n} f_i(x)$ using logarithmic differentiation, where $f_i(x)$ are differentiable functions. Back: Demonstrate the use of logarithmic properties and differentiation in the general case.

---

Hyperlinks for Further Reading:
- [[Calculus Fundamentals]]
- [[Differentiation Techniques]]
- [[Logarithm Properties]]

# Maxima and Minima Values

## Overview

Maxima and minima, fundamental concepts in calculus and mathematical analysis, refer to the highest and lowest values of a function within a given range. These points are crucial in various fields such as physics, engineering, economics, and optimization problems. 

## Historical Context

The concept of maxima and minima dates back to ancient times, with notable contributions from mathematicians like Fermat and Newton. Fermat's method of adequality in the early 17th century laid the groundwork for calculus, while Newton's method of fluxions provided a formal approach to finding these values.

## Definitions

1. **Local Maximum**: A function $f(x)$ has a local maximum at $x = a$ if $f(a)$ is greater than every value of $f(x)$ near $a$.
2. **Local Minimum**: Similarly, $f(x)$ has a local minimum at $x = a$ if $f(a)$ is less than every value of $f(x)$ near $a$.
3. **Global (or Absolute) Maximum/Minimum**: These are the highest and lowest values of the function over its entire domain.

## Finding Maxima and Minima

1. **Derivative Test**: If $f'(a) = 0$ and $f''(a) > 0$, $f(a)$ is a local minimum. If $f''(a) < 0$, it's a local maximum.
2. **Critical Points**: Points where $f'(x) = 0$ or $f'(x)$ does not exist are critical points, potential candidates for maxima or minima.
3. **Endpoints**: In a closed interval, the absolute maxima and minima can occur at endpoints or critical points within the interval.

## Applications

Maxima and minima are extensively used in optimizing resources, designing structures, financial modelling, and in the study of natural phenomena.

## Example

Consider the function $f(x) = x^2 - 4x + 4$. To find its minima or maxima:

1. Derivative: $f'(x) = 2x - 4$.
2. Critical Point: Set $f'(x) = 0$, so $x = 2$.
3. Second Derivative: $f''(x) = 2$, which is positive.
4. Conclusion: $f(x)$ has a local and absolute minimum at $x = 2$.

---

## Test Questions

1. Find the local maxima and minima of $f(x) = x^3 - 3x^2 + 2$.
2. Determine the absolute maximum and minimum values of $f(x) = \sin(x)$ in the interval $[0, 2\pi]$.
3. For the function $f(x) = e^{-x} \cos(x)$, identify the critical points and classify them.

# Modulus and Argument

## Introduction
Complex numbers, denoted as a + bi where a and b are real numbers and $i$ is the imaginary unit (satisfying $i^2 = -1$), form a fundamental part of mathematics, especially in fields like engineering, physics, and applied mathematics. Understanding the modulus and argument of complex numbers is crucial for visualizing and manipulating them in the complex plane.

## Modulus
The modulus of a complex number $z = a + bi$ is its absolute value and is represented by |z|. It is defined as the distance of the complex number from the origin in the complex plane. Mathematically, the modulus is given by:

$$|z| = \sqrt{a^2 + b^2}$$

This formula arises from the Pythagorean theorem, considering $a$ and $b$ as the legs of a right triangle.

### Example
For $z = 3 + 4i$, the modulus $|z|$ is calculated as:

$$|3 + 4i| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

## Argument
The argument of a complex number $z = a + bi$ is the angle $\theta$ formed with the positive direction of the x-axis. The argument is typically denoted as $\arg(z)$ and is measured in radians. The primary value of the argument lies in the interval $(-\pi, \pi]$. 

It is calculated using the formula:

$$\text{arg}(z) = \tan^{-1}\left(\frac{b}{a}\right)$$

### Example
For $z = 3 + 4i$, the argument is calculated as:

$$\text{arg}(3 + 4i) = \tan^{-1}\left(\frac{4}{3}\right)$$

This value would be in radians and can be converted to degrees if required.

## Visualization in the Complex Plane
In the complex plane, a complex number is represented as a point or a vector. The modulus represents the length of this vector, while the argument represents the angle it makes with the positive x-axis.

## Conclusion
The concepts of modulus and argument are crucial for understanding the geometric interpretation of complex numbers. They are instrumental in operations like multiplication and division of complex numbers.

---

### Test Questions
1. STARTI [Basic] Question: What is the modulus of the complex number $7 + 24i$? Back: $|7 + 24i| = \sqrt{7^2 + 24^2} = \sqrt{49 + 576} = \sqrt{625} = 25$. ENDI
2. STARTI [Basic] Question: Calculate the argument of the complex number $-4 + 3i$. Back: $\arg(-4 + 3i) = \tan^{-1}\left(\frac{3}{-4}\right)$. This value will be in the second quadrant as the real part is negative and the imaginary part is positive. ENDI
3. STARTI [Basic] Question: If a complex number has a modulus of 10 and an argument of π/4, what is the complex number? Back: Using the polar form, the complex number is $10(\cos(π/4) + i\sin(π/4)) = 10\left(\frac{\sqrt{2}}{2} + i \frac{\sqrt{2}}{2}\right) = 7.07 + 7.07i$ approximately. ENDI

# Multiple Integrals

## Overview
Multiple integrals are a key concept in advanced mathematics, particularly in the fields of calculus and analysis. They extend the idea of a single integral to functions of multiple variables. This note will delve into the basics of double and triple integrals, their applications, and some historical context.

### Historical Context
The development of multiple integrals can be traced back to the 17th century with the work of mathematicians like Isaac Newton and Gottfried Wilhelm Leibniz. Their foundational work in calculus paved the way for later advancements. In the 18th and 19th centuries, mathematicians such as Euler and Gauss further developed the theory, applying it to problems in physics, engineering, and other sciences.

## Double Integrals
A double integral refers to the integral of a function of two variables, usually x and y, over a two-dimensional region. It is denoted as:

$$\iint_D f(x, y) \,dx\,dy$$

Here, $D$ represents the domain of integration, which is a region in the xy-plane.

### Applications
- **Area Calculation**: Calculating the area under surfaces.
- **Physics**: Used in calculating mass, center of mass, and moments of inertia.
- **Engineering**: Applications in thermodynamics and fluid mechanics.

## Triple Integrals
Triple integrals extend this concept to functions of three variables, typically over a three-dimensional region. They are denoted as:

$$\iiint_D f(x, y, z) \,dx\,dy\,dz$$

### Applications
- **Volume Calculation**: Used for computing volumes under surfaces in 3D space.
- **Center of Mass**: Important in physics for bodies of arbitrary shape.
- **Electromagnetism**: Calculating electric and magnetic fields.

## Techniques and Challenges
- **Iterated Integrals**: Multiple integrals are often solved as iterated single integrals.
- **Choice of Order**: The order of integration can simplify calculations.
- **Change of Variables**: Techniques like polar, cylindrical, and spherical coordinates are used for convenient computation.

## Example Problems
1. Compute the double integral $\iint_D xy \,dx\,dy$ where $D$ is the rectangle defined by $0 \leq x \leq 1$ and $0 \leq y \leq 2$.
2. Evaluate the triple integral $\iiint_D z \,dx\,dy\,dz$ over the region $D$ bounded by the planes $x=0$, $y=0$, $z=0$, and $x+y+z=1$.

## Test Questions
- STARTI [Basic] Question: What is the geometrical interpretation of a double integral? Back: A double integral can be interpreted as the volume under a surface in the xy-plane. ENDI
- STARTI [Basic] Question: How does changing the order of integration in a double integral affect the solution? Back: Changing the order of integration can simplify the calculation by making the limits of integration easier to handle. It does not change the final result. ENDI
- STARTI [Basic] Question: Explain the importance of the Jacobian in changing variables for multiple integrals. Back: The Jacobian is a determinant that helps in transforming the integral when changing variables. It accounts for the scale change in volume or area in the new coordinate system. ENDI

For more detailed examples and applications, consider referencing resources like [[Calculus by James Stewart]] or [[Advanced Calculus by Lynn H. Loomis and Shlomo Sternberg]].

# Multivariable Functions

## Introduction
Multivariable functions are a fundamental concept in higher mathematics, especially in fields like calculus, physics, and engineering. Unlike a single-variable function, which has one input and one output, a multivariable function has multiple inputs. The most common are functions of two or three variables, but they can have any number of variables.

## Definition
A multivariable function is a function that has more than one input variable. For instance, a function f that takes two inputs x and y could be written as f(x, y). The output of this function depends on the combination of these inputs.

### Examples:
1. **Temperature Distribution in a Room**: The temperature at a point in a room can be a function of its x, y, and z coordinates: T(x, y, z).
2. **Economic Models**: An economic function might depend on multiple factors like investment, consumption, and interest rates: E(I, C, r).

## Graphical Representation
Graphically, a function of two variables can be represented as a surface in three-dimensional space. Each point (x, y, z) on this surface represents the value of the function f(x, y) = z.

## Partial Derivatives
An important aspect of multivariable functions is the concept of partial derivatives. A partial derivative is the derivative of a multivariable function with respect to one of its variables, holding the other variables constant. It shows how the function changes as one of the variables changes, keeping the others fixed.

### Example:
For f(x, y) = x² + y², the partial derivative with respect to x is 2x, and with respect to y is 2y.

## Applications
1. **Engineering**: Modeling physical systems like fluid dynamics.
2. **Economics**: Understanding how different economic factors interact.
3. **Optimization Problems**: Finding maxima and minima in multiple dimensions.

## Conclusion
Multivariable functions extend the concept of single-variable functions to multiple dimensions, providing a powerful tool for modeling complex systems in various scientific and engineering fields.

---

### Test Questions:
1. STARTI [Basic] Question: Define a multivariable function. Back: A multivariable function is a function with more than one input variable. For example, f(x, y) is a function of two variables x and y. ENDI
2. STARTI [Basic] Question: What is a partial derivative in the context of multivariable functions? Back: A partial derivative is the derivative of a multivariable function with respect to one of its variables, holding the other variables constant. It shows how the function changes as one variable changes, while keeping the others fixed. ENDI
3. STARTI [Basic] Question: How can a function of two variables be graphically represented? Back: A function of two variables can be graphically represented as a surface in three-dimensional space. Each point (x, y, z) on this surface corresponds to the value of the function f(x, y) = z. ENDI

# One-sided Limits

## Introduction
One-sided limits are an essential concept in calculus, particularly when studying functions that behave differently as they approach a certain point from different directions. Understanding one-sided limits is crucial for grasping the overall concept of limits, which forms the foundation for derivatives and integrals.

## Definition
A **one-sided limit** refers to the value that a function approaches as the input approaches a particular point from one side - either from the left or the right.

### Left-hand Limit
The **left-hand limit** of a function $f(x)$ as $x$ approaches a point $a$ is denoted as $\lim_{{x \to a^-}} f(x)$. It describes the behaviour of $f(x)$ as $x$ approaches $a$ from the left (i.e., from values less than $a$).

### Right-hand Limit
Conversely, the **right-hand limit** of $f(x)$ as $x$ approaches $a$ is denoted as $\lim_{{x \to a^+}} f(x)$. This limit explains what happens to $f(x)$ as $x$ approaches $a$ from the right (i.e., from values greater than $a$).

## Importance
One-sided limits are particularly important for understanding functions that are not continuous at certain points. They help in determining the behaviour of a function near points of discontinuity.

## Examples
1. **Step Function:** Consider the Heaviside step function $H(x)$, which is 0 for $x < 0$ and 1 for $x \geq 0$. The left-hand limit as $x$ approaches 0 is 0, while the right-hand limit is 1.

2. **Piecewise Functions:** Functions defined differently on different intervals often have distinct left-hand and right-hand limits at the points where the definition changes.

## Historical Context
The concept of limits, including one-sided limits, was formalized in the 19th century, though mathematicians like Newton and Leibniz used limit-like concepts in developing calculus in the 17th century.

## Conclusion
One-sided limits play a critical role in understanding the behaviour of functions, especially near points of discontinuity. They are fundamental in the study of calculus and are a stepping stone to more advanced concepts.

---

## Test Questions
1. Calculate the left-hand and right-hand limits of the function $f(x) = \frac{x}{|x|}$ as $x$ approaches 0.
2. For the function $$g(x) = \begin{cases} 
      x^2 & \text{if } x \leq 1 \\
      2x + 1 & \text{if } x > 1 
   \end{cases}$$, find $\lim_{{x \to 1^-}} g(x)$ and $\lim_{{x \to 1^+}} g(x)$.
3. Explain why the left-hand and right-hand limits are important for determining the continuity of a function at a point.

# Parametric Equations

## Introduction
Parametric equations are a way of defining a geometrical entity using parameters. Unlike the traditional Cartesian equations, where y is defined in terms of x or vice versa, parametric equations use an independent parameter, typically denoted as $t$, to express the coordinates of points on a curve.

## Understanding Parametric Equations
In a two-dimensional space, a pair of parametric equations can be represented as:
$$x = f(t)$$
$$y = g(t)$$
where $f(t)$ and $g(t)$ are functions of the parameter $t$.

### Example
Consider the circle with a radius $r$. The parametric equations are:
$$x = r \cos(t)$$
$$y = r \sin(t)$$
Here, $t$ represents the angle, in radians, from the positive x-axis to the point on the circle.

## Advantages of Parametric Equations
1. **Flexibility**: They can represent a wider variety of curves than Cartesian equations.
2. **Convenience in Calculations**: Easier to compute tangents, normals, and arc lengths.
3. **Motion Representation**: Useful in physics to represent the path of a moving object.

## Historical Context
Parametric equations have been around since the advent of analytical geometry in the 17th century. They gained prominence with the work of mathematicians like René Descartes and Pierre de Fermat.

## Application in Calculus
In calculus, parametric equations are used to:
- Find derivatives ($\frac{dy}{dx}$) using the chain rule.
- Compute the length of a curve.
- Evaluate the area under parametric curves.

## Example in Real World: Projectile Motion
In physics, the motion of a projectile is often represented using parametric equations:
$$x = v_0 \cos(\theta) t$$
$$y = v_0 \sin(\theta) t - \frac{1}{2} g t^2$$
where $v_0$ is the initial velocity, $\theta$ is the launch angle, and $g$ is the acceleration due to gravity.

## Test Questions
1. STARTI [Basic] Question: What are the parametric equations for a circle of radius 3? Back: $x = 3 \cos(t)$, $y = 3 \sin(t)$. ENDI
2. STARTI [Basic] Question: How do you find the slope of a curve represented by parametric equations? Back: Use the formula $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$. ENDI
3. STARTI [Basic] Question: If a particle moves along the curve given by $x = t^2$, $y = t^3$, what is the velocity at $t = 2$? Back: Velocity vector $\vec{v} = (2t, 3t^2)$. At $t = 2$, $\vec{v} = (4, 12)$. ENDI

For further reading and examples, consider exploring the links: [[Calculus with Parametric Equations]], [[History of Parametric Equations]], and [[Applications of Parametric Equations in Physics]].

# Partial Derivatives

## Introduction
Partial derivatives are fundamental in the field of multivariable calculus. They represent the rate at which a function changes as one of its variables is varied, while keeping other variables constant. This concept is crucial in physics, engineering, economics, and various other disciplines where functions depend on more than one variable.

## Basic Concepts
Consider a function $f(x, y)$ of two variables, $x$ and $y$. The partial derivative of $f$ with respect to $x$ is denoted as $\frac{\partial f}{\partial x}$ and represents the rate of change of $f$ as $x$ changes, while $y$ is held constant. Similarly, $\frac{\partial f}{\partial y}$ denotes the rate of change of $f$ with respect to $y$, keeping $x$ constant.

### Calculation
To compute $\frac{\partial f}{\partial x}$, treat $y$ as a constant and differentiate $f$ with respect to $x$ using the standard rules of differentiation. Apply the same process to find $\frac{\partial f}{\partial y}$, treating $x$ as a constant.

### Example
For $f(x, y) = x^2y + 3xy^3$:
- $\frac{\partial f}{\partial x} = 2xy + 3y^3$
- $\frac{\partial f}{\partial y} = x^2 + 9xy^2$

## Higher-Order Partial Derivatives
You can also take partial derivatives of partial derivatives. For example, the second-order partial derivatives of $f$ are:
- $\frac{\partial^2 f}{\partial x^2}$, $\frac{\partial^2 f}{\partial y^2}$: The second partial derivatives with respect to $x$ and $y$ respectively.
- $\frac{\partial^2 f}{\partial x \partial y}$, $\frac{\partial^2 f}{\partial y \partial x}$: The mixed partial derivatives.

### Clairaut's Theorem
Clairaut's Theorem states that if $f$ is continuously differentiable, then the mixed partial derivatives are equal: $\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}$.

## Applications
Partial derivatives are used in various fields:
- **Physics**: Describing systems with multiple variables (e.g., temperature gradients).
- **Engineering**: Optimization problems, fluid dynamics.
- **Economics**: Modeling how different factors affect economic indicators.

## Conclusion and Test Questions
Understanding partial derivatives is essential for any field that deals with functions of multiple variables. They form the foundation for more complex concepts in multivariable calculus, like gradients and Jacobians.

### Test Questions
1. Compute the partial derivatives $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$ for $f(x, y) = \ln(x) + e^{xy}$.
2. Explain the significance of Clairaut's Theorem in the context of partial derivatives.
3. How would you use partial derivatives to find the maximum and minimum values of a function of two variables?

# Periodicity

## Introduction
Periodicity is a fundamental concept in various fields of mathematics, especially in trigonometry and analysis. It refers to the property of a function where the function values repeat at regular intervals. This concept is critical in understanding waves, oscillations, and many phenomena in physics and engineering.

## Definition
A function $f(x)$ is said to be periodic if there exists a non-zero value $P$ such that for all values of $x$ in the function's domain, $f(x + P) = f(x)$. The smallest positive value of $P$ for which this holds true is known as the period of the function.

### Examples
- **Sine and Cosine Functions**: The sine and cosine functions are classic examples of periodic functions. They both have a period of $2\pi$. This means that $\sin(x + 2\pi) = \sin(x)$ and $\cos(x + 2\pi) = \cos(x)$ for all $x$.
- **Tangent Function**: The tangent function is periodic with a period of $\pi$, as $\tan(x + \pi) = \tan(x)$ for all $x$.

## Historical Context
The concept of periodic functions became prominent with the study of trigonometric functions in the context of astronomy and timekeeping. Ancient civilizations, notably the Greeks and Indians, developed a deep understanding of these functions, although the formal concept of periodicity was developed much later.

## Applications
Periodic functions are widely used in various applications:
- **Signal Processing**: In signal processing, periodic signals are analyzed using Fourier series and transforms.
- **Quantum Mechanics**: The wave functions in quantum mechanics often exhibit periodic properties.
- **Time Series Analysis**: Periodic trends in data are studied in economics, meteorology, and other fields.

## Test Questions
1. Question: Define a periodic function. Back: A function $f(x)$ is periodic if there exists a non-zero value $P$ such that $f(x + P) = f(x)$ for all $x$.
2. Question: What is the period of the sine function? Back: The period of the sine function is $2\pi$.
3. Question: Explain the significance of periodic functions in signal processing. Back: In signal processing, periodic functions are crucial for analyzing and synthesizing signals, particularly through the use of Fourier series and Fourier transforms.

---

*For more mathematical concepts, check out the notes on [[Trigonometric Functions]] and [[Fourier Series]].*

# Piecewise-defined Functions

## Introduction

Piecewise-defined functions are unique in that they have different expressions for different parts of their domains. This allows for greater flexibility in defining functions that change behaviour over different intervals.

## Definition

A piecewise-defined function is a function that is defined by multiple sub-functions, each applying to a certain interval of the main function's domain. The general form is:

$$f(x) = \begin{cases} 
f_1(x) & \text{for } x \text{ in interval } I_1 \\
f_2(x) & \text{for } x \text{ in interval } I_2 \\
\vdots \\
f_n(x) & \text{for } x \text{ in interval } I_n 
\end{cases}$$

Each $f_i(x)$ represents a different rule or formula applied over a specific interval $I_i$.

## Examples

1. **Absolute Value Function**: 
   $$|x| = \begin{cases} 
   x & \text{if } x \geq 0 \\
   -x & \text{if } x < 0 
   \end{cases}$$

2. **Piecewise Linear Function**:
   $$f(x) = \begin{cases} 
   2x + 3 & \text{if } x < 1 \\
   5 & \text{if } x = 1 \\
   3x - 2 & \text{if } x > 1
   \end{cases}$$

## Properties

1. **Continuity**: A piecewise-defined function can be continuous or discontinuous. Continuity at the points where the function changes from one piece to another depends on the limits of the sub-functions as they approach these points.

2. **Differentiability**: Similar to continuity, a piecewise-defined function can be differentiable or not, depending on the behaviour of the sub-functions at the points where they meet.

3. **Domain and Range**: The domain is the set of all x-values for which the function is defined, and the range is the set of all possible y-values.

## Applications

Piecewise-defined functions are used in various fields, such as engineering, economics, and physics, to model situations where a system behaves differently under different conditions.

## Historical Context

The concept of piecewise-defined functions developed alongside the formalization of function theory in mathematics. They were instrumental in understanding complex phenomena that could not be modelled by a single, uniform rule.

## **Test Questions

1. Define a piecewise function that describes the following scenario: A taxi company charges a flat rate for the first 2 kilometres and then a different rate for each additional kilometre.
2. Is it possible for a piecewise-defined function to be continuous? Provide an example.
3. How do you determine the domain and range of a piecewise-defined function?

## Conclusion

Understanding piecewise-defined functions is essential in mathematics, as they provide a way to model complex, real-world scenarios that vary over different intervals. Their unique structure allows for the flexibility needed in many applications, making them a valuable tool in the mathematician's toolkit.

# Points of Inflection

## Introduction
In mathematics, especially in calculus, a **point of inflection** (or inflection point) is a point on a curve at which the curve changes from being concave (curved upward) to convex (curved downward), or vice versa.

## Definition
A point of inflection occurs on a differentiable function $f(x)$ at a point $c$ if the function is continuous at $c$ and the sign of the second derivative $f''(x)$ changes at $c$. This means that $f''(x)$ will change from positive to negative, or from negative to positive, as x passes through $c$. 

## Mathematical Expression
Mathematically, a point $c$ is a point of inflection for a function $f(x)$ if:
1. $f''(c) = 0$ or $f''(c)$ does not exist.
2. There is a change in the sign of $f''(x)$ around $c$.

## Historical Context
The concept of an inflection point has been a part of calculus since its early development. Inflection points are important in the study of the curvature of curves and were extensively discussed by mathematicians like Fermat and Euler.

## Examples
1. **Cubic Polynomial:** Consider $f(x) = x^3$. Its second derivative is $f''(x) = 6x$. Setting $f''(x) = 0$ gives $x = 0$, which is an inflection point.
2. **Trigonometric Function:** Consider $f(x) = \sin(x)$. The second derivative is $f''(x) = -\sin(x)$. Inflection points occur at $x = n\pi$ where $n$ is an integer.

## Inflection Points in Real-World Applications
- **Engineering:** In the design of structures, like bridges, understanding inflection points can help predict points of potential structural stress or failure.
- **Economics:** Inflection points are used in economics to indicate a significant change in the direction of a trend, such as in market graphs.

## Test Questions
1. Find the inflection points of $f(x) = x^4 - 4x^3 + 6x^2$.
2. Explain why $f(x) = x^2$ has no inflection points.
3. Determine the inflection point(s) of the function $f(x) = \ln(x)$.

# Polar and Exponential Form

## Introduction
Polar and exponential forms are crucial in understanding complex numbers. These forms provide alternative ways to represent complex numbers, often simplifying multiplication, division, and finding powers and roots.

## Polar Form
A complex number $z = a + bi$ can be represented in polar form as $z = r(\cos \theta + i\sin \theta)$, where $r$ is the magnitude (or modulus) of the complex number, and $\theta$ is the argument (or angle).

### Calculating $r$ and $\theta$
- **Magnitude ($r$)**: It is the distance from the origin to the point in the complex plane, calculated as $r = \sqrt{a^2 + b^2}$.
- **Argument ($\theta$)**: This is the angle formed with the positive x-axis, determined by $\theta = \arctan\left(\frac{b}{a}\right)$, considering the quadrant where the complex number lies.

## Exponential Form
The exponential form of a complex number uses Euler's formula, $e^{i\theta} = \cos \theta + i\sin \theta$. Thus, a complex number $z = r(\cos \theta + i\sin \theta)$ can also be written as $z = re^{i\theta}$.

### Advantages
- **Simplifies Multiplication and Division**: Multiplication and division become simpler as they turn into addition or subtraction of exponents.
- **Powers and Roots**: Calculating powers and roots of complex numbers becomes more straightforward using the exponential form.

## Historical Context
The concept of representing complex numbers in polar and exponential forms was significantly developed in the 18th century. Leonhard Euler, a Swiss mathematician, made substantial contributions to these concepts, particularly through Euler's formula.

## Examples
1. Convert $1 + i$ into polar and exponential forms.
2. Find the product of $2e^{i\pi/4}$ and $3e^{i\pi/3}$ using exponential form.

## Conclusion
Understanding polar and exponential forms of complex numbers is pivotal in advanced mathematics, particularly in fields such as signal processing and quantum mechanics.

## Test Questions
1. STARTI [Basic] Question: Convert the complex number $3 + 4i$ into polar form. Back: $5(\cos \arctan(\frac{4}{3}) + i\sin \arctan(\frac{4}{3}))$. ENDI
2. STARTI [Basic] Question: Express $e^{i\pi/6}$ in standard complex form. Back: $\frac{\sqrt{3}}{2} + \frac{1}{2}i$. ENDI
3. STARTI [Basic] Question: Calculate the product of $2e^{i\pi/4}$ and $3e^{i\pi/3}$. Back: $6e^{i5\pi/12}$. ENDI

[[Mathematics]] | [[Complex Numbers]] | [[Euler's Formula]]

# Polar Coordinates

## Introduction
Polar coordinates are a two-dimensional coordinate system where each point on a plane is determined by a distance from a reference point and an angle from a reference direction. This system is particularly useful in scenarios where relationships are more naturally expressed in terms of angles and distances, such as in circular and spiral patterns.

## Basics of Polar Coordinates
In polar coordinates, the reference point is called the pole (analogous to the origin in Cartesian coordinates), and the ray from the pole in the reference direction is the polar axis. The distance from the pole is denoted by $r$, and the angle from the polar axis is denoted by $\theta$, typically measured in radians.

- **Representation**: A point is represented as $(r, \theta)$, where $r$ is the radial distance and $\theta$ is the angular coordinate.

## Conversion between Cartesian and Polar Coordinates
To convert between Cartesian coordinates $(x, y)$ and polar coordinates $(r, \theta)$:

- **Polar to Cartesian**:
  $$x = r \cos \theta$$
  $$y = r \sin \theta$$

- **Cartesian to Polar**:
  $$r = \sqrt{x^2 + y^2}$$
  $$\theta = \arctan\left(\frac{y}{x}\right)$$ (adjusted for the correct quadrant)

## Applications
Polar coordinates are used in various fields such as physics, engineering, and navigation. They are particularly useful in describing patterns like spirals, circular motion, and periodic functions.

## Historical Context
The concept of polar coordinates dates back to the work of Greek mathematician and astronomer Hipparchus who developed a table of chord functions, essentially using an early form of trigonometry. The modern version of polar coordinates is often attributed to Isaac Newton and Jacob Bernoulli in the 17th century.

## Examples
1. **Spiral**: A logarithmic spiral can be represented as $r = a \cdot e^{b\theta}$, where $a$ and $b$ are constants.
2. **Circle**: A circle with radius $a$ centered at the pole is described by $r = a$.

## Test Questions
1. STARTI [Basic] Question: Convert the Cartesian coordinates (3, 4) to polar coordinates. Back: $r = 5, \theta = \arctan\left(\frac{4}{3}\right)$. ENDI
2. STARTI [Basic] Question: What is the equation of a circle of radius 5 in polar coordinates? Back: $r = 5$. ENDI
3. STARTI [Basic] Question: Describe the curve represented by $r = 2\theta$ in polar coordinates. Back: It's a spiral increasing linearly with the angle. ENDI

---

This note on polar coordinates provides a fundamental understanding of their concept, conversion methods, and applications. The historical context and examples help in comprehending their practical relevance.

# Polynomial Functions

Polynomial functions are mathematical expressions involving a sum of powers in one or more variables multiplied by coefficients. A general form of a polynomial function in a single variable $x$ can be written as:

$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_2 x^2 + a_1 x + a_0$$

where $n$ is a non-negative integer and $a_0, a_1, \ldots, a_n$ are constants with $a_n \neq 0$.

## Key Characteristics

1. **Degree**: The highest power of the variable in the polynomial. For example, in $3x^4 - 2x^2 + x$, the degree is 4.
2. **Leading Coefficient**: The coefficient of the term with the highest degree. In the above example, it is 3.
3. **Constant Term**: The term without the variable, denoted as $a_0$ in the general form.
4. **Roots/Zeros**: Values of $x$ for which $P(x) = 0$. These are crucial in solving polynomial equations.

## Types of Polynomial Functions

- **Linear Polynomial**: Degree 1 (e.g., $f(x) = 2x + 1$)
- **Quadratic Polynomial**: Degree 2 (e.g., $f(x) = x^2 - 4x + 4$)
- **Cubic Polynomial**: Degree 3 (e.g., $f(x) = x^3 - 3x^2 + 3x - 1$)
- **Quartic Polynomial**: Degree 4 (e.g., $f(x) = x^4 - 4x^3 + 6x^2 - 4x + 1$)

## Historical Context

Polynomial functions have been studied for centuries. The study of polynomials led to the development of algebra and calculus. The roots of polynomial functions, especially quadratic, cubic, and quartic polynomials, were extensively studied by mathematicians like Al-Khwarizmi, Cardano, and Ferrari.

## Applications

Polynomials are used in a wide range of applications, including physics, engineering, and economics. They are essential in modeling phenomena, curve fitting, and numerical analysis.

## Test Questions

1. STARTI [Basic] Question: What is the degree of the polynomial $3x^5 - 2x^3 + x^2 - 7$? Back: The degree of the polynomial is 5. ENDI
2. STARTI [Basic] Question: What is the leading coefficient of the polynomial $x^4 - 3x^3 + 2x - 1$? Back: The leading coefficient of the polynomial is 1. ENDI
3. STARTI [Basic] Question: Give an example of a quadratic polynomial. Back: An example of a quadratic polynomial is $f(x) = x^2 - 5x + 6$. ENDI

# Precise Definition of a Limit

## Introduction
The concept of a limit is fundamental in calculus and mathematical analysis, serving as the cornerstone for understanding continuity, derivatives, and integrals. It allows mathematicians to describe how functions behave as their inputs approach a particular value, even if the function does not actually reach that value.

## Precise Definition
The precise definition of a limit, often attributed to Karl Weierstrass, is formulated using ε (epsilon) and δ (delta), two arbitrary positive numbers. This formulation is crucial for rigorous proofs and a deep understanding of calculus.

### Definition
Let $f(x)$ be a function defined on an open interval that contains $c$, except possibly at $c$ itself. We say that the limit of $f(x)$ as $x$ approaches $c$ is $L$, and write:

$$
\lim_{{x \to c}} f(x) = L
$$

if for every $\epsilon > 0$ there exists a $\delta > 0$ such that whenever $0 < |x - c| < \delta$, it follows that $|f(x) - L| < \epsilon$.

### Interpretation
This definition can be interpreted as follows:
- For any small ε-band (interval) around $L$, there is a δ-band (interval) around $c$ such that, when $x$ is within this δ-band (but not equal to $c$), $f(x)$ will be within the ε-band around $L$.
- Essentially, as $x$ gets closer to $c$, $f(x)$ gets arbitrarily close to $L$.

## Examples
To illustrate the precise definition, consider the following examples:

1. **Linear Function**: For $f(x) = 2x + 3$, show that $\lim_{{x \to 2}} f(x) = 7$.
2. **Quadratic Function**: For $f(x) = x^2$, find the limit as $x$ approaches 3.

## Historical Context
The formal definition of a limit was developed in the 19th century. Before this period, mathematicians like Newton and Leibniz used intuitive notions of limits to develop calculus. The rigorous definition by Weierstrass helped to resolve paradoxes and ambiguities inherent in these early methods.

## Test Questions
1. STARTI [Basic] Question: Explain in your own words what the δ (delta) represents in the definition of a limit. Back: δ represents a measure of how close x needs to be to c, such that f(x) is within ε of L. ENDI
2. STARTI [Basic] Question: For the function $f(x) = 3x$, what is $\lim_{{x \to 4}} f(x)$? Back: $\lim_{{x \to 4}} 3x = 12$. ENDI
3. STARTI [Basic] Question: Why is the precise definition of a limit important in calculus? Back: It provides a rigorous foundation for calculus, allowing for precise proofs and a deeper understanding of concepts like continuity, derivatives, and integrals. ENDI

## Conclusion
Understanding the precise definition of a limit is crucial for anyone studying advanced mathematics, especially calculus. It lays the groundwork for many other concepts and ensures a solid understanding of how functions behave near specific points.

# Properties of the Definite Integral and Fundamental Theorem of Calculus

## Introduction
Definite integrals are a cornerstone in calculus, representing the accumulation of quantities and areas under curves. The Fundamental Theorem of Calculus (FTC) bridges the concepts of differentiation and integration, revealing a profound connection between them. This note explores the properties of the definite integral and the FTC, providing a comprehensive understanding of these concepts.

## Properties of the Definite Integral
The definite integral of a function $f(x)$ over an interval $[a, b]$ is denoted by $\int_{a}^{b} f(x) \, dx$. It has several key properties:

1. **Additivity over Intervals**: 
   $\int_{a}^{c} f(x) \, dx + \int_{c}^{b} f(x) \, dx = \int_{a}^{b} f(x) \, dx$ for any $c$ between $a$ and $b$.

2. **Zero Width Interval**: 
   $\int_{a}^{a} f(x) \, dx = 0$.

3. **Reversal of Limits**: 
   $\int_{a}^{b} f(x) \, dx = -\int_{b}^{a} f(x) \, dx$.

4. **Linearity**:
   $\int_{a}^{b} [cf(x) + dg(x)] \, dx = c\int_{a}^{b} f(x) \, dx + d\int_{a}^{b} g(x) \, dx$, where $c$ and $d$ are constants.

## Fundamental Theorem of Calculus
The FTC is divided into two parts:

1. **FTC Part I**: 
   If $f$ is continuous on $[a, b]$ and $F$ is an antiderivative of $f$ on $[a, b]$, then $\int_{a}^{b} f(x) \, dx = F(b) - F(a)$.

2. **FTC Part II**: 
   If $f$ is continuous on $[a, b]$, then the function $g(x) = \int_{a}^{x} f(t) \, dt$ is continuous on $[a, b]$, differentiable on $(a, b)$, and $g'(x) = f(x)$.

## Applications and Historical Context
The FTC not only simplifies the computation of definite integrals but also signifies a major development in mathematical analysis. It was independently discovered by Isaac Newton and Gottfried Wilhelm Leibniz in the late 17th century, laying the groundwork for modern calculus.

## Test Questions

1. **STARTI [Basic] Question:** Calculate $\int_{0}^{2} x^2 \, dx$ using the FTC. **Back:** Let $F(x) = \frac{1}{3}x^3$ be an antiderivative of $f(x) = x^2$. Then, $\int_{0}^{2} x^2 \, dx = F(2) - F(0) = \frac{8}{3}$. ENDI

2. **STARTI [Basic] Question:** Show that $\int_{a}^{b} f(x) \, dx = -\int_{b}^{a} f(x) \, dx$. **Back:** Let $G(x)$ be an antiderivative of $f(x)$. Then, $\int_{a}^{b} f(x) \, dx = G(b) - G(a)$ and $\int_{b}^{a} f(x) \, dx = G(a) - G(b)$. Thus, $\int_{a}^{b} f(x) \, dx = -(G(a) - G(b)) = -\int_{b}^{a} f(x) \, dx$. ENDI

3. **STARTI [Basic] Question:** Explain the significance of the FTC in calculus. **Back:** The FTC links the concept of integration with differentiation. It shows that the accumulation process (integration) is the inverse of the rate of change (differentiation). This duality is fundamental to many areas of mathematics and physics. ENDI

---

For a deeper exploration, consider linking this note to related topics such as [[Differential Calculus]], [[Antiderivatives]], and [[Applications of Integration]] in your Obsidian vault.

# Rational Functions

## Definition
A **rational function** is a function of the form $f(x) = \frac{P(x)}{Q(x)}$, where $P(x)$ and $Q(x)$ are polynomial functions and $Q(x) \neq 0$. The domain of a rational function includes all real numbers except those that make $Q(x)$ equal to zero.

## Characteristics
- **Asymptotes**: Vertical asymptotes occur at values of $x$ where $Q(x) = 0$, provided $P(x)$ does not also equal zero at these points. Horizontal asymptotes are determined by the degrees of $P(x)$ and $Q(x)$.
- **Discontinuity**: Points where $Q(x) = 0$ are typically points of discontinuity.
- **Behavior at Infinity**: The behavior of $f(x)$ as $x$ approaches infinity depends on the leading terms of $P(x)$ and $Q(x)$.

## Examples
1. $f(x) = \frac{x^2 - 4}{x - 2}$ 
   - Notice the removable discontinuity at $x = 2$.
2. $g(x) = \frac{1}{x^2}$ 
   - This function has a horizontal asymptote at $y = 0$.

## Historical Context
Rational functions are a key component in the development of calculus and have been studied extensively since the time of Newton and Leibniz. They are crucial in understanding limits and derivatives.

## Test Questions
1. STARTI [Basic] Question: What is the domain of $f(x) = \frac{1}{x - 3}$? Back: All real numbers except $x = 3$. ENDI
2. STARTI [Basic] Question: For the function $g(x) = \frac{x^2 - 1}{x^2 + x - 6}$, identify the vertical and horizontal asymptotes. Back: Vertical asymptotes at $x = 2$ and $x = -3$, Horizontal asymptote at $y = 1$. ENDI
3. STARTI [Basic] Question: Explain why the function $h(x) = \frac{x^3}{x^2 - 4}$ does not have a horizontal asymptote. Back: The degree of the numerator is greater than the degree of the denominator. ENDI

# Rolle's Theorem and Mean Value Theorem

## Introduction

In the realm of calculus, two significant theorems that play a pivotal role are **Rolle's Theorem** and the **Mean Value Theorem**. These theorems are fundamental in understanding the behavior of functions and their derivatives. They provide essential insights into the relationship between a function and its rate of change.

## Rolle's Theorem

### Statement
Rolle's Theorem states that if a function $f(x)$ is continuous on a closed interval $[a, b]$ and differentiable on the open interval $(a, b)$, and if $f(a) = f(b)$, then there exists at least one $c$ in the interval $(a, b)$ such that the derivative $f'(c) = 0$.

### Intuition
The theorem essentially tells us that for any smooth curve that starts and ends at the same height, there must be at least one point where the tangent to the curve is horizontal.

### Historical Context
Rolle's Theorem is named after Michel Rolle, a French mathematician who formulated the theorem in 1691. His work laid the groundwork for the development of calculus, particularly in the study of the behavior of functions.

## Mean Value Theorem

### Statement
The Mean Value Theorem (MVT) extends Rolle's Theorem. It states that if a function $f(x)$ is continuous on a closed interval $[a, b]$ and differentiable on the open interval $(a, b)$, then there exists at least one $c$ in $(a, b)$ such that $f'(c) = \frac{f(b) - f(a)}{b - a}$.

### Intuition
The MVT asserts that somewhere on the curve, there is a point where the tangent to the curve is parallel to the secant line connecting the endpoints of the interval.

### Historical Context
The Mean Value Theorem plays a central role in calculus and analysis. It is a generalization of Rolle's Theorem and was developed as part of the formalization of calculus.

## Examples

1. **Rolle's Theorem Example**: Consider $f(x) = x^2 - 4x + 4$ on the interval [0, 4]. Since $f(0) = f(4)$ and $f(x)$ is both continuous and differentiable on this interval, Rolle's Theorem applies. We find that $f'(x) = 2x - 4$, and setting $f'(c) = 0$, we find $c = 2$.

2. **Mean Value Theorem Example**: For $f(x) = x^2$ on the interval [1, 3], the function is continuous and differentiable. Applying MVT, we find that there exists a $c$ such that $f'(c) = \frac{f(3) - f(1)}{3 - 1}$. Calculating, we find $c = \sqrt{5}$.

## Conclusion and Test Questions

Understanding these theorems is crucial for comprehending more advanced concepts in calculus. They not only provide a method to analyze the behavior of functions but also lay the foundation for further studies in differential equations and analysis.

### Test Questions

1. STARTI [Basic] Question: State Rolle's Theorem. Back: Rolle's Theorem states that if a function $f(x)$ is continuous on a closed interval $[a, b]$ and differentiable on the open interval $(a, b)$, and if $f(a) = f(b)$, then there exists at least one $c$ in $(a, b)$ such that $f'(c) = 0$. ENDI
2. STARTI [Basic] Question: What is the geometric interpretation of the Mean Value Theorem? Back: Geometrically, the Mean Value Theorem asserts that there is at least one point on the curve of the function where the tangent is parallel to the secant line connecting the endpoints of the interval. ENDI
3. STARTI [Basic] Question: Apply Rolle's Theorem to the function $f(x) = x^3 - 3x^2 + 2x$ on the interval [0, 3]. Back: Rolle's Theorem applies as $f(x)$ is continuous and differentiable, and $f(0) = f(3) = 0$. The derivative is $f'(x) = 3x^2 - 6x + 2$. Setting $f'(c) = 0$ and solving, we find $c = 1$ or $c = \frac{2}{3}$. ENDI

[[Calculus]] | [[Rolle's Theorem]] | [[Mean Value Theorem]]

# Roots of Complex Numbers

## Introduction
Complex numbers, a fundamental concept in mathematics, extend the idea of the number system to include the square roots of negative numbers. The most common form of a complex number is $a + bi$, where $a$ and $b$ are real numbers, and $i$ is the imaginary unit with the property $i^2 = -1$. 

## Roots of Complex Numbers
Finding the $n$-th roots of a complex number is a key operation. The $n$-th roots of a complex number $z$ are the solutions to the equation $x^n = z$. If $z$ is represented in polar form as $r(\cos \theta + i\sin \theta)$, where $r$ is the magnitude and $\theta$ the argument of $z$, its $n$-th roots can be found using De Moivre's Theorem. 

### De Moivre's Theorem
De Moivre's Theorem states that for any real number $\theta$ and any integer $n$, the following holds:

$$(\cos \theta + i\sin \theta)^n = \cos(n\theta) + i\sin(n\theta)$$

Using this theorem, we can express the $n$-th roots of $z$ as:

$$z^{1/n} = r^{1/n} \left( \cos\left(\frac{\theta + 2k\pi}{n}\right) + i\sin\left(\frac{\theta + 2k\pi}{n}\right) \right)$$

for $k = 0, 1, 2, ..., n-1$.

## Historical Context
The concept of complex numbers and their roots was initially met with skepticism. It was not until the 18th century that mathematicians like Abraham de Moivre and Leonhard Euler formalized these ideas, leading to significant developments in mathematics and physics.

## Examples
1. Find the square roots of $1 + i$.
2. Calculate the cube roots of $-8$.

## Test Questions
1. What is the polar form of the complex number $3 + 4i$?
2. Using De Moivre's Theorem, find the fourth roots of $16(\cos \pi + i\sin \pi)$.
3. Explain the significance of the argument $\theta$ in finding the roots of complex numbers.

# Rotation of Complex Numbers

## Introduction
In mathematics, particularly in complex analysis, rotation of complex numbers is an essential concept. Complex numbers, expressed in the form $a + bi$, where $a$ and $b$ are real numbers, and $i$ is the imaginary unit, can be represented as points or vectors in the complex plane. Rotation in this context involves turning the vector around the origin of the complex plane.

## Representing Complex Numbers
A complex number $z = a + bi$ can be represented in polar form as $z = r(\cos \theta + i\sin \theta)$, where $r$ is the magnitude of $z$ and $\theta$ is the argument (or the angle with the positive x-axis). This polar form is crucial for understanding rotations.

## Basic Rotation
To rotate a complex number $z$ by an angle $\phi$, we multiply $z$ by the complex number $e^{i\phi}$ (Euler's formula). The resulting complex number $z'$ is given by:

$$z' = z \cdot e^{i\phi}$$

This operation rotates $z$ counterclockwise by $\phi$ radians about the origin.

## Example
Consider a complex number $z = 1 + i$. Its polar form is $\sqrt{2}(\cos \frac{\pi}{4} + i\sin \frac{\pi}{4})$. To rotate this number by $\frac{\pi}{2}$ radians, we compute:

$$z' = (\sqrt{2}(\cos \frac{\pi}{4} + i\sin \frac{\pi}{4})) \cdot e^{i\frac{\pi}{2}}$$

This results in a new complex number, representing the rotated point in the complex plane.

## Applications
Rotation of complex numbers has applications in various fields, including engineering, physics, and computer graphics. In these domains, it's often used to model rotations in two-dimensional space.

## Test Questions
1. STARTI [Basic] Question: What is the result of rotating the complex number $1 + i$ by $\frac{\pi}{2}$ radians? Back: The result is $-1 + i$. ENDI
2. STARTI [Basic] Question: How do you represent a complex number in polar form? Back: A complex number $z = a + bi$ is represented in polar form as $z = r(\cos \theta + i\sin \theta)$, where $r$ is the magnitude and $\theta$ is the argument. ENDI
3. STARTI [Basic] Question: What is Euler's formula, and how is it used in the rotation of complex numbers? Back: Euler's formula is $e^{i\phi} = \cos \phi + i\sin \phi$. It is used in rotating a complex number by multiplying the number with $e^{i\phi}$. ENDI

# Rules for Differentiation

Differentiation is a fundamental concept in calculus, focusing on finding the rate at which a function changes at any given point. In undergraduate mathematics, understanding the rules of differentiation is crucial for solving complex problems. Here, we will explore these rules, with historical context and practical examples.

### Historical Context

Differentiation, as part of calculus, was developed independently in the late 17th century by Isaac Newton and Gottfried Wilhelm Leibniz. While their notation and approach differed, the essence of their findings laid the foundation for modern calculus.

### Basic Rules of Differentiation

1. **Power Rule**  
   $$\frac{d}{dx}[x^n] = nx^{n-1}$$  
   Where $n$ is any real number.

2. **Constant Rule**  
   $$\frac{d}{dx}[c] = 0$$  
   Where $c$ is a constant.

3. **Constant Multiple Rule**  
   $$\frac{d}{dx}[cf(x)] = c \cdot \frac{d}{dx}[f(x)]$$  
   Where $c$ is a constant.

4. **Sum Rule**  
   $$\frac{d}{dx}[f(x) + g(x)] = \frac{d}{dx}[f(x)] + \frac{d}{dx}[g(x)]$$

5. **Difference Rule**  
   $$\frac{d}{dx}[f(x) - g(x)] = \frac{d}{dx}[f(x)] - \frac{d}{dx}[g(x)]$$

6. **Product Rule**  
   $$\frac{d}{dx}[f(x) \cdot g(x)] = f(x) \cdot \frac{d}{dx}[g(x)] + g(x) \cdot \frac{d}{dx}[f(x)]$$

7. **Quotient Rule**  
   $$\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{g(x) \cdot \frac{d}{dx}[f(x)] - f(x) \cdot \frac{d}{dx}[g(x)]}{[g(x)]^2}$$

8. **Chain Rule**  
   $$\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$$

### Examples

1. **Power Rule Example**  
   If $f(x) = x^3$, then $\frac{d}{dx}f(x) = 3x^2$.

2. **Product Rule Example**  
   For $f(x) = x^2$ and $g(x) = x+1$, $\frac{d}{dx}[f(x)g(x)] = x^2 + 2x(x+1)$.

3. **Chain Rule Example**  
   Given $f(x) = (3x+1)^2$, $\frac{d}{dx}f(x) = 2(3x+1) \cdot 3$.

### Test Questions

1. **STARTI [Basic] Question:** Use the power rule to differentiate $f(x) = x^5$. Back: $\frac{d}{dx}f(x) = 5x^4$. ENDI
2. **STARTI [Basic] Question:** Apply the product rule to differentiate $f(x) = x^2 \cdot \ln(x)$. Back: $\frac{d}{dx}f(x) = 2x \cdot \ln(x) + x$. ENDI
3. **STARTI [Basic] Question:** Use the chain rule to differentiate $f(x) = \sqrt{4x+1}$. Back: $\frac{d}{dx}f(x) = \frac{1}{2\sqrt{4x+1}} \cdot 4$. ENDI

# Rules for Limits

## Overview

In calculus, limits are fundamental in understanding the behaviour of functions as they approach a specific point. Limits help in defining derivatives and integrals, which are core concepts in calculus. This note will cover the basic rules for calculating limits, which are essential for understanding more complex calculus topics.

## Basic Rules

1. **Constant Rule**: If $f(x) = c$, a constant, then $\lim_{x \to a} f(x) = c$.
2. **Identity Rule**: For $f(x) = x$, $\lim_{x \to a} f(x) = a$.
3. **Sum Rule**: $\lim_{x \to a} [f(x) + g(x)] = \lim_{x \to a} f(x) + \lim_{x \to a} g(x)$.
4. **Difference Rule**: $\lim_{x \to a} [f(x) - g(x)] = \lim_{x \to a} f(x) - \lim_{x \to a} g(x)$.
5. **Product Rule**: $\lim_{x \to a} [f(x) \cdot g(x)] = \lim_{x \to a} f(x) \cdot \lim_{x \to a} g(x)$.
6. **Quotient Rule**: If $\lim_{x \to a} g(x) \neq 0$, then $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}$.
7. **Power Rule**: $\lim_{x \to a} [f(x)]^n = [\lim_{x \to a} f(x)]^n$, where $n$ is a positive integer.

## Historical Context

The concept of limits was formalized in the late 17th century by Sir Isaac Newton and Gottfried Wilhelm Leibniz while developing calculus. This was a significant advancement over the previous methods of infinitesimals, providing a more rigorous foundation for calculus.

## Application in Calculus

- **Derivatives**: The derivative of a function at a point is defined as the limit of the function's average rate of change at that point.
- **Integrals**: The integral of a function is found using the limit of summing infinitely many infinitesimally small quantities.

## Examples

1. **Constant Rule Example**: $\lim_{x \to 4} 7 = 7$.
2. **Sum Rule Example**: $\lim_{x \to 3} (x^2 + 2x) = \lim_{x \to 3} x^2 + \lim_{x \to 3} 2x = 9 + 6 = 15$.

## Test Questions

1. Calculate $\lim_{x \to 2} (3x + 4)$ using the Sum and Constant rules.
2. Find $\lim_{x \to 5} x^3$ using the Power rule.
3. Determine $\lim_{x \to 0} \frac{x^2 - 1}{x - 1}$ using the Quotient rule.

# Standard Cases and Techniques of Integration

Integration is a crucial concept in calculus, used in areas like physics, engineering, and mathematics. It helps in calculating areas, solving differential equations, and more. This note explores standard cases, techniques of integration, and includes reduction formulas.

## Basic Definitions

**Integral:** A mathematical representation of the area under a curve over an interval.

- **Indefinite Integral:** Represents a family of functions without specified limits, including a constant of integration $C$.
- **Definite Integral:** An integral with specific upper and lower limits, providing a numerical value for the area under the curve.

## Standard Techniques of Integration

1. **Direct Integration:** Applying known integral formulas.
   - Example: $\int x^2 \, dx = \frac{x^3}{3} + C$

2. **Integration by Substitution:** Simplifying the integral through variable change.
   - Example: $\int 2x \cdot e^{x^2} \, dx$, set $u = x^2$.

3. **Integration by Parts:** Based on differentiation's product rule, for integrals involving products of functions.
   - Formula: $\int u \, dv = uv - \int v \, du$
   - Example: $\int x \cdot e^x \, dx$

4. **Partial Fraction Decomposition:** For rational functions, splitting the fraction into simpler parts.
   - Example: $\int \frac{1}{x^2 - 1} \, dx$

5. **Trigonometric Substitution:** For integrals involving square roots of trigonometric expressions.
   - Example: $\int \sqrt{1 - x^2} \, dx$

6. **Integration of Trigonometric Functions:** Specific techniques for trigonometric integrals.
   - Example: $\int \sin(x) \cos(x) \, dx$

7. **Improper Integrals:** For integrals with infinite limits or discontinuous integrands.
   - Example: $\int_1^\infty \frac{1}{x^2} \, dx$

## Reduction Formulas

Reduction formulas are recursive relations that reduce the power of the function being integrated. They are particularly useful in integrating powers of trigonometric functions.

- **Sine Reduction Formula:** 
  $$\int \sin^n(x) \, dx = -\frac{\sin^{n-1}(x) \cos(x)}{n} + \frac{n-1}{n} \int \sin^{n-2}(x) \, dx$$

- **Cosine Reduction Formula:** 
  $$\int \cos^n(x) \, dx = \frac{\cos^{n-1}(x) \sin(x)}{n} + \frac{n-1}{n} \int \cos^{n-2}(x) \, dx$$

- **Tangent Reduction Formula:** 
  $$\int \tan^n(x) \, dx = \frac{\tan^{n-1}(x)}{n-1} - \int \tan^{n-2}(x) \, dx$$

## Historical Context

Integration's roots trace back to the 17th century with significant contributions from Isaac Newton and Gottfried Wilhelm Leibniz. Their groundbreaking work in calculus laid the groundwork for its extensive modern applications.

## Test Questions

1. **STARTI [Basic] Question:** Calculate $\int 3x^2 \, dx$. **Back:** The integral of $3x^2$ is $x^3 + C$. **ENDI**
2. **STARTI [Intermediate] Question:** Apply integration by parts to $\int x \cdot e^x \, dx$. **Back:** Set $u = x$ and $dv = e^x dx$, leading to $xe^x - \int e^x \, dx = xe^x - e^x + C$. **ENDI**
3. **STARTI [Advanced] Question:** Solve $\int \sin^3(x) \, dx$ using the sine reduction formula. **Back:** Applying the formula, $\int \sin^3(x) \, dx = -\frac{\sin^2(x) \cos(x)}{3} + \frac{2}{3} \int \sin(x) \, dx$. **ENDI**

Incorporating these techniques and formulas in your studies will enhance your understanding and ability to tackle complex integrals. Consider creating flashcards on specific integration techniques or practicing more complex examples to deepen your understanding.

# Stationary Points of Functions with Two Variables

## Introduction
In mathematics, particularly in multivariable calculus, the concept of stationary points is crucial for understanding the behavior of functions with two variables. A stationary point of a function is a point at which the gradient (or the first derivative) of the function is zero. These points are significant because they potentially represent local maxima, local minima, or saddle points in the function's graph.

## Definition
Consider a function $f(x, y)$ of two variables. A point $(x_0, y_0)$ is called a **stationary point** of $f$ if both partial derivatives of $f$ are zero at that point, i.e.,

$$\frac{\partial f}{\partial x}(x_0, y_0) = 0 \quad \text{and} \quad \frac{\partial f}{\partial y}(x_0, y_0) = 0.$$

## Types of Stationary Points
1. **Local Maximum**: At $(x_0, y_0)$, $f(x, y)$ is greater than its immediate surroundings.
2. **Local Minimum**: At $(x_0, y_0)$, $f(x, y)$ is less than its immediate surroundings.
3. **Saddle Point**: At $(x_0, y_0)$, $f(x, y)$ is neither a local maximum nor a minimum but has a flat tangent plane.

## Finding Stationary Points
To find the stationary points of $f(x, y)$, follow these steps:
1. Find the first partial derivatives $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$.
2. Solve the simultaneous equations $\frac{\partial f}{\partial x} = 0$ and $\frac{\partial f}{\partial y} = 0$ to find the coordinates $(x_0, y_0)$ of the stationary points.

## Determining the Nature of Stationary Points
Once the stationary points are found, use the second derivative test to determine their nature:
1. Compute the second-order partial derivatives: $\frac{\partial^2 f}{\partial x^2}$, $\frac{\partial^2 f}{\partial y^2}$, and the mixed derivative $\frac{\partial^2 f}{\partial x \partial y}$.
2. Evaluate the second-order derivatives at the stationary point $(x_0, y_0)$.
3. Calculate the determinant of the [[Hessian matrix]] $D$ at $(x_0, y_0)$:

   $$D = \left( \frac{\partial^2 f}{\partial x^2} \right)\left( \frac{\partial^2 f}{\partial y^2} \right) - \left( \frac{\partial^2 f}{\partial x \partial y} \right)^2$$

4. Interpretation:
   - If $D > 0$ and $\frac{\partial^2 f}{\partial x^2} > 0$, then $(x_0, y_0)$ is a local minimum.
   - If $D > 0$ and $\frac{\partial^2 f}{\partial x^2} < 0$, then $(x_0, y_0)$ is a local maximum.
   - If $D < 0$, then $(x_0, y_0)$ is a saddle point.
   - If $D = 0$, the test is inconclusive.

## Examples
1. Consider $f(x, y) = x^2 + y^2$. The stationary point at $(0, 0)$ is a local minimum.
2. For $f(x, y) = x^2 - y^2$, the point $(0, 0)$ is a saddle point.

## Test Questions
1. Find the stationary points of $f(x, y) = x^3 - 3xy + y^3$ and classify them.
2. If $f(x, y) = x^2 + 2xy + y^2 + 3$, determine the nature of its stationary point(s).
3. Explain why saddle points are important in the study of functions with two variables.

---

This note provides a fundamental understanding of stationary points in functions of two variables, crucial for fields like optimization, economics, and engineering. Understanding and visualizing these concepts enhance the comprehension of the landscape of multivariable functions.

# Step Functions and their Limits

Step functions are a type of piecewise constant function, commonly used in mathematical analysis and applications. They are defined by partitioning a domain into a finite number of intervals and assigning a constant value to each interval. This creates a function that jumps from one value to another, resembling steps, hence the name.

## Definition and Examples

A step function, $f$, on an interval $[a, b]$ can be written as:

$$f(x) = \begin{cases} 
c_1 & \text{if } x \in [a_1, b_1) \\
c_2 & \text{if } x \in [a_2, b_2) \\
\vdots \\
c_n & \text{if } x \in [a_n, b_n]
\end{cases}$$

where $c_1, c_2, \ldots, c_n$ are constants, and the intervals $[a_i, b_i)$ cover $[a, b]$ without overlapping.

**Example:** The function defined by $f(x) = 1$ for $x \in [0, 1)$ and $f(x) = 2$ for $x \in [1, 2]$ is a simple step function.

## Properties

- **Discontinuities:** Step functions are discontinuous at the points where the function jumps from one value to another.
- **Integrability:** They are Riemann integrable on any interval over which they are defined.

## Limits of Step Functions

The concept of limits applies to step functions, particularly at points of discontinuity. The limit of a step function as $x$ approaches a point of discontinuity can be different from the function's value at that point.

### Left-Hand and Right-Hand Limits

- **Left-Hand Limit (LHL):** The limit of $f(x)$ as $x$ approaches a point $c$ from the left.
- **Right-Hand Limit (RHL):** The limit of $f(x)$ as $x$ approaches $c$ from the right.

In many cases, the LHL and RHL at a point of discontinuity of a step function are equal to the values of the function on the intervals immediately to the left and right of the point, respectively.

## Historical Context

Step functions have been essential in the development of integration theory, serving as a simple form of a function that is easy to integrate. They are also used in probability theory (e.g., in defining cumulative distribution functions) and in signal processing.

## Applications

- **Signal Processing:** Step functions model signals that change abruptly at certain points in time.
- **Economics:** They can represent tax brackets where the tax rate changes at specific income levels.

## Test Questions

1. **Question:** Provide an example of a step function defined on the interval $[0, 3]$.
   
   **Back:** One example could be: $f(x) = 1$ for $x \in [0, 1)$, $f(x) = 2$ for $x \in [1, 2)$, and $f(x) = 3$ for $x \in [2, 3]$.

2. **Question:** Explain why step functions are Riemann integrable.

   **Back:** Step functions are Riemann integrable because they are bounded and only have a finite number of discontinuities in any bounded interval.

3. **Question:** What is the left-hand limit of the step function $f(x)$ at $x = 2$ if $f(x) = 3$ for $x \in [1, 2)$ and $f(x) = 5$ for $x \in [2, 3]$?

   **Back:** The left-hand limit of $f(x)$ at $x = 2$ is 3, as it is the value of the function on the interval immediately to the left of 2.

# Tests for Continuity

## Introduction
Continuity of a function is a fundamental concept in calculus and mathematical analysis. It describes the behaviour of functions as they approach a particular point. A function is continuous at a point if there is no sudden change in its value at that point. Understanding continuity is crucial in studying limits, derivatives, and integrals.

## Definition
A function $f(x)$ is said to be continuous at a point $a$ if the following three conditions are met:
1. **Existence of $f(a)$**: The function $f(x)$ is defined at $a$.
2. **Limit Exists**: The limit of $f(x)$ as $x$ approaches $a$ exists.
3. **Limit Equals Function Value**: The limit of $f(x)$ as $x$ approaches $a$ is equal to $f(a)$.

Formally, $f(x)$ is continuous at $a$ if and only if 
$$\lim_{x \to a} f(x) = f(a)$$

## Types of Continuity
1. **Continuous at a Point**: If a function meets the above criteria at a particular point.
2. **Continuous on an Interval**: If a function is continuous at every point in a given interval.
3. **Uniform Continuity**: A stronger form of continuity that holds when the function's rate of change is bounded throughout its domain.

## Tests for Continuity
To determine whether a function is continuous at a point or over an interval, follow these steps:

1. **Check for Existence**: Ensure the function is defined at the point or throughout the interval.
2. **Evaluate the Limit**: Find the limit of the function as it approaches the point from both directions (left and right).
3. **Compare Limit and Function Value**: Ensure that the limit equals the function's value at the point.

### Special Cases
- **Piecewise Functions**: Check continuity at each segment and at the points where the function changes definition.
- **Rational Functions**: Check points where the denominator is zero.
- **Trigonometric Functions**: Pay attention to points where these functions are not defined.

## Historical Context
The concept of continuity has evolved significantly over time. Early notions by mathematicians like Newton and Leibniz were more intuitive. The rigorous definition, as given by Weierstrass in the 19th century, laid the groundwork for modern analysis.

## Examples
1. **Polynomials**: Polynomials are continuous everywhere.
2. **Rational Functions**: Rational functions are continuous wherever they are defined (i.e., where the denominator is non-zero).
3. **Trigonometric Functions**: Functions like sin(x) and cos(x) are continuous everywhere, but functions like tan(x) are not continuous where cos(x) = 0.

## Conclusion
Understanding continuity is essential for delving deeper into calculus. It's a concept that bridges the gap between intuitive and rigorous mathematical thinking.

## Test Questions
1. Is the function $f(x) = \frac{1}{x}$ continuous at $x = 0$? Why or why not?
2. Determine if the function $$g(x) = \left\{
   \begin{array}{ll}
   x^2 & \text{if } x < 1 \\
   x+1 & \text{if } x \geq 1
   \end{array}
\right.$$ is continuous at $x = 1$.
3. Prove that the function $h(x) = x^3 - 2x + 1$ is continuous for all values of $x$.

# Trigonometric Functions

Trigonometric functions are fundamental in mathematics, particularly in the fields of geometry, engineering, and physics. They relate the angles of a triangle to the lengths of its sides and have applications in periodic phenomena such as waves.

## Definition and Basic Concepts

### The Unit Circle
- The unit circle is a circle with a radius of one, centred at the origin of a coordinate plane.
- Any point on the unit circle can be represented as $(\cos \theta, \sin \theta)$, where $\theta$ is the angle formed with the positive x-axis.

### Sine and Cosine Functions
- **Sine ($\sin$)**: In a right triangle, the sine of an angle is the ratio of the length of the opposite side to the length of the hypotenuse.
- **Cosine ($\cos$)**: The cosine of an angle is the ratio of the length of the adjacent side to the length of the hypotenuse.
- In the unit circle, $\sin \theta$ and $\cos \theta$ represent the y and x coordinates, respectively.

### Other Functions
- **Tangent ($\tan$)**: $\tan \theta = \frac{\sin \theta}{\cos \theta}$.
- **Cotangent ($\cot$)**: $\cot \theta = \frac{1}{\tan \theta}$.
- **Secant ($\sec$)**: $\sec \theta = \frac{1}{\cos \theta}$.
- **Cosecant ($\csc$)**: $\csc \theta = \frac{1}{\sin \theta}$.

## Properties and Identities

### Periodicity
- Sine and cosine functions are periodic with a period of $2\pi$.
- Tangent and cotangent functions have a period of $\pi$.

### Symmetry
- Sine is an odd function: $\sin(-\theta) = -\sin(\theta)$.
- Cosine is an even function: $\cos(-\theta) = \cos(\theta)$.

### Pythagorean Identity
- $\sin^2 \theta + \cos^2 \theta = 1$.

### Addition Formulas
- $\sin(a + b) = \sin a \cos b + \cos a \sin b$.
- $\cos(a + b) = \cos a \cos b - \sin a \sin b$.

## Applications

- **Circles and Oscillations**: Modelling circular motion and wave patterns.
- **Sound and Light Waves**: Describing wave properties like amplitude and frequency.
- **Architecture and Engineering**: Solving problems involving angles and distances.

## Test Questions

1. If $\cos \theta = \frac{1}{2}$ and $\theta$ is in the first quadrant, what is $\sin \theta$?
2. Prove that $\tan(\theta + \pi) = \tan \theta$.
3. What is the period of the function $f(x) = 3 \sin(2x + \pi)$?

Linking to other notes can help expand on related concepts, such as [[Pythagorean Theorem]], [[Unit Circle]], and [[Wave Mechanics]].

# Types of Discontinuity

**Introduction**
In mathematics, particularly in calculus and real analysis, the concept of discontinuity plays a crucial role in understanding the behaviour of functions. Discontinuity refers to points at which a function is not continuous. Understanding different types of discontinuities helps in analysing functions and their properties. This note delves into the main types of discontinuities you'll encounter.

## Types of Discontinuities

### 1. Jump Discontinuity
A **jump discontinuity** occurs when the function has two distinct limit values as it approaches from the left and the right of a certain point. In other words, the function 'jumps' from one value to another.

- **Example:** Consider the function $$f(x) = \left\{
   \begin{array}{ll}
   x + 1 & \mbox{if } x < 0 \\
   x - 1 & \mbox{if } x \geq 0
   \end{array}
\right.$$- This function has a jump discontinuity at $x = 0$.

### 2. Infinite Discontinuity
An **infinite discontinuity** occurs when the function approaches infinity as it nears a certain point.

- **Example:** The function $g(x) = \frac{1}{x}$ has an infinite discontinuity at $x = 0$.

### 3. Removable Discontinuity
A **removable discontinuity** is present when a function is not defined at a point, but the limit exists and is the same from both sides. By redefining the function at that point, the discontinuity can be 'removed.'

- **Example:** The function $h(x) = \frac{{x^2 - 1}}{{x - 1}}$ can be simplified to $h(x) = x + 1$ for $x \neq 1$. It has a removable discontinuity at $x = 1$.

### 4. Oscillating Discontinuity
An **oscillating discontinuity** occurs when the function oscillates between different values as it approaches the discontinuous point.

- **Example:** The function $k(x) = \sin\left(\frac{1}{x}\right)$ oscillates between -1 and 1 as $x$ approaches 0.

## Historical Context
The concept of continuity and discontinuity in mathematics dates back to the 19th century. Bernhard Riemann, a German mathematician, was among the pioneers in formalizing the definition of a continuous function. His work paved the way for rigorous mathematical analysis and a deeper understanding of function behaviour.

## Test Questions
1. **Identify the Discontinuity:** For the function $f(x) = \frac{x^2 - 4}{x - 2}$, determine the type of discontinuity at $x = 2$.
2. **True or False:** Every infinite discontinuity is also a jump discontinuity.
3. **Application:** Describe the behaviour of the function $g(x) = \tan(x)$ near $x = \frac{\pi}{2}$ and classify the type of discontinuity.

# Note on the Vertical Line Test

## Introduction
The **Vertical Line Test** is a visual method used to determine if a curve is the graph of a function for a real variable. It is a fundamental concept in the study of functions in mathematics, particularly in calculus and precalculus.

## Understanding the Vertical Line Test
A function, by definition, assigns exactly one output to each input. The Vertical Line Test uses this principle to check if a graph represents a function.

### How it Works:
- **Draw Vertical Lines:** Imagine drawing vertical lines (parallel to the y-axis) across the graph.
- **Check for Intersections:** If any vertical line intersects the graph in more than one point, the graph does not represent a function.

### Why it Works:
- **Uniqueness of Output:** A function has only one output for each input. If a vertical line crosses more than one point, it means there are multiple outputs for a single input, violating the definition of a function.

## Application in Different Contexts
- **Pre-Calculus and Calculus:** Used to identify functions.
- **Graph Analysis:** Helps in understanding the nature of a graph.
- **Troubleshooting:** Identifies issues in graphical representations.

## Historical Context
The concept of functions dates back to the 17th century, but the formal definition was refined over time. The Vertical Line Test emerged as a simple, yet powerful tool to visually assess the functionality of a graph.

## Examples
- **Linear Equations:** Straight lines (not vertical) always pass the test.
- **Parabolas:** Standard parabolas pass the test, but if rotated, they might fail.
- **Circles:** A circle fails the test as vertical lines cut it at two points.

## Conclusion
The Vertical Line Test is a simple, yet effective method to determine whether a graph represents a function. Its visual nature makes it an accessible tool for students and mathematicians alike.

---

### Test Questions
1. STARTI [Basic] Question: What does it mean if a graph fails the Vertical Line Test? Back: It means that the graph does not represent a function, as there are multiple outputs for a single input. ENDI
2. STARTI [Basic] Question: Can a horizontal line be used in a similar way to the Vertical Line Test? Back: No, a horizontal line test is used to determine if a function is one-to-one, not to determine if a graph is a function. ENDI
3. STARTI [Basic] Question: Give an example of a graph that would pass the Vertical Line Test but is not a function over the entire real line. Back: The graph of $y = \sqrt{x}$ passes the Vertical Line Test but is not a function over the entire real line as it is undefined for negative values of x. ENDI

