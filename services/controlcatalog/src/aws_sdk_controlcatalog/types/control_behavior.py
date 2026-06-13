"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controlcatalog.errors import DeserializationError

ControlBehavior: TypeAlias = Literal[
    "PREVENTIVE",
    "PROACTIVE",
    "DETECTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PREVENTIVE",
        "PROACTIVE",
        "DETECTIVE",
    )
)


def serialize_json(value: ControlBehavior) -> str:
    return value


def deserialize_json(data: str) -> ControlBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ControlBehavior value: {data!r}")
    return cast(ControlBehavior, data)
