#!/usr/bin/env python3
"""Observer pattern with topic-based subscriptions."""


class NewsSubject:
    """Manage subscribers and notify them about news."""

    def __init__(self):
        """Initialize the subscriber registry."""
        self._observers = []

    def subscribe(self, observer, topics=None):
        """Subscribe an observer to selected topics."""
        self._observers.append((observer, topics))

    def unsubscribe(self, observer):
        """Remove an observer from subscriptions."""
        self._observers = [
            entry for entry in self._observers
            if entry[0] is not observer
        ]

    def notify(self, topic, data):
        """Notify observers subscribed to the given topic."""
        for observer, topics in list(self._observers):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    """Log sports and breaking news."""

    def update(self, topic, data):
        """Print a log notification."""
        print(f"log:{topic}={data}")


class EmailObserver:
    """Send email notifications for all topics."""

    def update(self, topic, data):
        """Print an email notification."""
        print(f"email:{topic}={data}")


class SmsObserver:
    """Send SMS notifications for subscribed topics."""

    def update(self, topic, data):
        """Print an SMS notification."""
        print(f"sms:{topic}={data}")


def main():
    """Demonstrate topic-based observer subscriptions."""
    subject = NewsSubject()
    log_observer = LogObserver()
    email_observer = EmailObserver()
    sms_observer = SmsObserver()

    subject.subscribe(log_observer, topics={"sports", "breaking"})
    subject.subscribe(email_observer)
    subject.subscribe(sms_observer, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
