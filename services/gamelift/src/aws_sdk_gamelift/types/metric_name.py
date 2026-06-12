"""Generated from Smithy shape ``com.amazonaws.gamelift#MetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

MetricName: TypeAlias = Literal[
    "ActivatingGameSessions",
    "ActiveGameSessions",
    "ActiveInstances",
    "AvailableGameSessions",
    "AvailablePlayerSessions",
    "CurrentPlayerSessions",
    "IdleInstances",
    "PercentAvailableGameSessions",
    "PercentIdleInstances",
    "QueueDepth",
    "WaitTime",
    "ConcurrentActivatableGameSessions",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ActivatingGameSessions",
        "ActiveGameSessions",
        "ActiveInstances",
        "AvailableGameSessions",
        "AvailablePlayerSessions",
        "CurrentPlayerSessions",
        "IdleInstances",
        "PercentAvailableGameSessions",
        "PercentIdleInstances",
        "QueueDepth",
        "WaitTime",
        "ConcurrentActivatableGameSessions",
    )
)


def serialize_aws_json_1_1(value: MetricName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricName value: {data!r}")
    return cast(MetricName, data)
