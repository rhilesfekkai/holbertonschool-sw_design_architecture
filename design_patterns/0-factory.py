#!/usr/bin/env python3
"""Factory pattern using an extensible vehicle registry."""


class Bus:
    """Represent a bus."""

    def mode(self):
        """Return the bus mode."""
        return "road"


class Train:
    """Represent a train."""

    def mode(self):
        """Return the train mode."""
        return "rails"


class Bike:
    """Represent a bike."""

    def mode(self):
        """Return the bike mode."""
        return "lane"


class Scooter:
    """Represent a scooter."""

    def mode(self):
        """Return the scooter mode."""
        return "scooter_lane"


class VehicleFactory:
    """Create vehicles using a registry."""

    def __init__(self):
        """Initialize the vehicle registry."""
        self._registry = {
            "bus": Bus,
            "train": Train,
            "bike": Bike,
        }

    def register_kind(self, name: str, cls):
        """Register a vehicle class."""
        self._registry[name] = cls

    def create(self, kind: str):
        """Create a vehicle from the registry."""
        return self._registry[kind]()


def main():
    """Demonstrate the vehicle factory."""
    factory = VehicleFactory()
    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    factory.register_kind("scooter", Scooter)
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
