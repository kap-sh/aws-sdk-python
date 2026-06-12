"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AlarmType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

AlarmType: TypeAlias = Literal[
    "Metric",
    "Composite",
    "Canary",
    "Logs",
    "Event",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Metric",
        "Composite",
        "Canary",
        "Logs",
        "Event",
    )
)


def serialize_json(value: AlarmType) -> str:
    return value


def deserialize_json(data: str) -> AlarmType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AlarmType value: {data!r}")
    return cast(AlarmType, data)
