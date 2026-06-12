"""Generated from Smithy shape ``com.amazonaws.mq#BrokerState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mq.errors import DeserializationError

"""<p>The broker's status.</p>"""
BrokerState: TypeAlias = Literal[
    "CREATION_IN_PROGRESS",
    "CREATION_FAILED",
    "DELETION_IN_PROGRESS",
    "RUNNING",
    "REBOOT_IN_PROGRESS",
    "CRITICAL_ACTION_REQUIRED",
    "REPLICA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATION_IN_PROGRESS",
        "CREATION_FAILED",
        "DELETION_IN_PROGRESS",
        "RUNNING",
        "REBOOT_IN_PROGRESS",
        "CRITICAL_ACTION_REQUIRED",
        "REPLICA",
    )
)


def serialize_json(value: BrokerState) -> str:
    return value


def deserialize_json(data: str) -> BrokerState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BrokerState value: {data!r}")
    return cast(BrokerState, data)
