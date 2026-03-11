"""
APT3010-VA - Introduction to Artificial Intelligence
Assignment 2 - Mars Rover Simulation

This program simulates a Mars Rover performing two exploration ventures
across four Mars locations (A, B, C, D), sampling rocks at each location.
The environment changes randomly between explorations (wind uncovers/covers rocks).
The rover avoids re-sampling locations it has already visited.
"""

import random  # Used to randomize the Mars environment (rock presence)


# ─────────────────────────────────────────────
# CLASS 1: RoverPerformance
# Tracks what the rover has done (sampling history & score)
# ─────────────────────────────────────────────
class RoverPerformance:
    def __init__(self):
        # Dictionary to record how many times each location was sampled
        # Starts at 0 for all four locations
        self.locations_sampled = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

        # Counters for total actions taken vs. successful samples
        self.total_actions = 0       # Every time the rover tries to do something
        self.successful_samples = 0  # Every time the rover actually gets a rock sample

    def record_sample(self, location):
        """Call this when the rover successfully samples a location."""
        self.locations_sampled[location] += 1  # Add 1 to that location's count
        self.successful_samples += 1            # Increase success count
        self.total_actions += 1                 # Increase total action count

    def record_action(self):
        """Call this for any action the rover takes (even unsuccessful ones)."""
        self.total_actions += 1

    def get_performance(self):
        """Calculate and return the rover's performance as a percentage."""
        if self.total_actions == 0:
            return 0  # Avoid dividing by zero if no actions were taken
        return (self.successful_samples / self.total_actions) * 100

    def display_results(self):
        """Print the final summary: locations sampled and performance score."""
        print(f"\nLocations Sampled {self.locations_sampled}")
        print(f"Rovers performance  {self.get_performance():.1f} %")


# ─────────────────────────────────────────────
# CLASS 2: MarsEnvironment
# Represents the four Mars locations and whether each has rocks
# ─────────────────────────────────────────────
class MarsEnvironment:
    def __init__(self):
        # Each location (A, B, C, D) randomly has rocks (1) or no rocks (0)
        # random.randint(0, 1) gives either 0 or 1 with equal chance
        self.locations = {
            'A': random.randint(0, 1),
            'B': random.randint(0, 1),
            'C': random.randint(0, 1),
            'D': random.randint(0, 1)
        }

    def randomize(self):
        """Randomize the environment again (simulates wind between explorations)."""
        self.locations = {
            'A': random.randint(0, 1),
            'B': random.randint(0, 1),
            'C': random.randint(0, 1),
            'D': random.randint(0, 1)
        }

    def has_rocks(self, location):
        """Returns True if the given location currently has rocks."""
        return self.locations[location] == 1

    def display(self):
        """Print the current state of the environment (which locations have rocks)."""
        print(self.locations)


# ─────────────────────────────────────────────
# CLASS 3: RoverAgent
# The rover itself - decides where to go and what to do
# ─────────────────────────────────────────────
class RoverAgent:
    def __init__(self, environment, performance):
        self.environment = environment    # The Mars environment the rover operates in
        self.performance = performance    # The performance tracker

        # The rover picks a random starting location each exploration
        self.current_location = random.choice(['A', 'B', 'C', 'D'])

        # Keep track of which locations have already been sampled (to avoid repeats)
        self.sampled_locations = []

    def explore(self, venture_number):
        """
        Perform one full exploration venture.
        The rover visits all 4 locations and tries to sample rocks.
        """
        print(f"\n----Explorartion Venture  {venture_number} -------")
        self.environment.display()  # Show current environment state
        print(f"Rover is in Location. {self.current_location}")

        # Go through all four locations in order
        for location in ['A', 'B', 'C', 'D']:

            # RULE: Skip this location if it was already sampled in a previous venture
            if location in self.sampled_locations:
                print(f"{location} Location has been Sampled before.")
                self.performance.record_action()  # Still counts as an action
                continue  # Move to the next location

            # Check if this location has rocks
            if self.environment.has_rocks(location):
                # There are rocks here - sample them!
                print(f"{location} Rocks Sampled.")
                self.performance.record_sample(location)   # Record success
                self.sampled_locations.append(location)    # Mark as sampled
            else:
                # No rocks at this location
                print(f"{location}  has no Rocks.")
                self.performance.record_action()  # Still an action, just no sample


# ─────────────────────────────────────────────
# MAIN PROGRAM
# Sets everything up and runs both exploration ventures
# ─────────────────────────────────────────────
def main():
    # Create the performance tracker (shared across both ventures)
    performance = RoverPerformance()

    # Create the Mars environment (randomly initialised)
    environment = MarsEnvironment()

    # ── VENTURE 0 ──
    # Create the rover and run the first exploration
    rover = RoverAgent(environment, performance)
    rover.explore(0)

    # Between explorations, the environment changes (wind!)
    environment.randomize()

    # Update the rover's location randomly for the next venture
    rover.current_location = random.choice(['A', 'B', 'C', 'D'])

    # ── VENTURE 1 ──
    # Run the second exploration with the new environment
    rover.explore(1)

    # Print the final results
    performance.display_results()

    # Pause so the user can read the output (like "Press any key to continue...")
    input("\nPress any key to continue . . .")


# This makes sure main() only runs when we execute this file directly
if __name__ == "__main__":
    main()
