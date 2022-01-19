## Deferred Acceptance Algorithm

In mathematics, economics, and computer science, the Gale–Shapley algorithm (also known as the deferred acceptance algorithm or propose-and-reject algorithm) is an algorithm for finding a solution to the stable matching problem, named for David Gale and Lloyd Shapley who had described it as solving both the college admission problem and the stable marriage problem. It takes polynomial time, and the time is linear in the size of the input to the algorithm. It is a truthful mechanism from the point of view of the proposing participants, for whom the solution will always be optimal.

The Gale–Shapley algorithm involves a number of "rounds" (or "iterations"):

- In the first round, first a) each unengaged man proposes to the woman he prefers most, and then b) each woman replies "maybe" to her suitor she most prefers and "no" to all other suitors. She is then provisionally "engaged" to the suitor she most prefers so far, and that suitor is likewise provisionally engaged to her.
- In each subsequent round, first a) each unengaged man proposes to the most-preferred woman to whom he has not yet proposed (regardless of whether the woman is already engaged), and then b) each woman replies "maybe" if she is currently not engaged or if she prefers this man over her current provisional partner (in this case, she rejects her current provisional partner who becomes unengaged). The provisional nature of engagements preserves the right of an already-engaged woman to "trade up" (and, in the process, to "jilt" her until-then partner).
- This process is repeated until everyone is engaged.


Source: https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm
