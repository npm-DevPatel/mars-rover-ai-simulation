# Mars Rover Simulation 🚀

A Python simulation of a Mars Rover performing exploration ventures across four locations on Mars, sampling rocks along the way. Built for APT3010-VA — Introduction to Artificial Intelligence.

---

## What It Does

The rover explores four Mars locations — **A, B, C, D** — over two separate ventures. At each location, it checks for rocks and samples them if present. Between ventures, the environment changes randomly (wind can uncover or cover rocks). The rover keeps track of where it's already been and won't sample the same location twice.

At the end, it reports which locations were sampled and gives a performance score based on how many successful samples it collected out of all actions taken.

---

## How to Run

Make sure you have Python 3 installed, then:

```bash
python mars_rover.py
```

No extra libraries needed — only Python's built-in `random` module is used.

---

## Project Structure

```
mars-rover-ai-simulation/
│
├── mars_rover.py        # Main simulation
└── README.md
```

---

## The Three Classes

**`MarsEnvironment`** — Randomly assigns rocks to each location. Simulates wind by re-randomizing between explorations.

**`RoverPerformance`** — Tracks the rover's sampling history and calculates its final performance percentage.

**`RoverAgent`** — The rover itself. Decides where to go, checks for rocks, and remembers locations it has already sampled.

---

## Example Output

```
----Explorartion Venture  0 -------
{'A': 1, 'B': 1, 'C': 0, 'D': 0}
Rover is in Location. C
C  has no Rocks.
D  has no Rocks.
A Rocks Sampled.
B Rocks Sampled.

----Explorartion Venture  1 -------
{'A': 1, 'B': 1, 'C': 1, 'D': 0}
Rover is in Location. A
A Location has been Sampled before.
B Location has been Sampled before.
C Rocks Sampled.
D  has no Rocks.

Locations Sampled {'A': 1, 'B': 1, 'C': 1, 'D': 0}
Rovers performance  75.0 %
```

---

## Group 3

| Name | Student ID |
|---|---|
| Dev Patel | 670820 |
| Juliet Karakacha | 671759 |
| Harshni Beed | 674078 |
| Megan Surmat | 673644 |
| Shreyas Dodhia | 673432 |
| Muriuki Lenny | 670597 |
| Steve Kyoni | 673382 |