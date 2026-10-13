#!/usr/bin/env python3
"""Demonstrate the Decorator pattern with beverages."""


class Beverage:
    """Define the beverage interface."""

    def cost(self):
        """Return the beverage cost."""
        raise NotImplementedError

    def description(self):
        """Return the beverage description."""
        raise NotImplementedError


class Coffee(Beverage):
    """Represent a basic coffee."""

    def cost(self):
        """Return the coffee cost."""
        return 50

    def description(self):
        """Return the coffee description."""
        return "Coffee"


class MilkDecorator(Beverage):
    """Add milk to a beverage."""

    def __init__(self, inner):
        """Wrap a beverage."""
        self._inner = inner

    def cost(self):
        """Return the cost including milk."""
        return self._inner.cost() + 10

    def description(self):
        """Return the description including milk."""
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """Add sugar to a beverage."""

    def __init__(self, inner):
        """Wrap a beverage."""
        self._inner = inner

    def cost(self):
        """Return the cost including sugar."""
        return self._inner.cost() + 5

    def description(self):
        """Return the description including sugar."""
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """Add caramel to a beverage."""

    def __init__(self, inner):
        """Wrap a beverage."""
        self._inner = inner

    def cost(self):
        """Return the cost including caramel."""
        return self._inner.cost() + 15

    def description(self):
        """Return the description including caramel."""
        return self._inner.description() + " + caramel"


def main():
    """Print examples of decorated beverages."""
    first = MilkDecorator(Coffee())
    print(first.description(), first.cost())

    second = MilkDecorator(SugarDecorator(Coffee()))
    print(second.description(), second.cost())

    third = CaramelDecorator(
        MilkDecorator(SugarDecorator(Coffee()))
    )
    print(third.description(), third.cost())


if __name__ == "__main__":
    main()
