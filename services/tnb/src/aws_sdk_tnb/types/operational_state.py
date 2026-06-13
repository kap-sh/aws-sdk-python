"""Generated from Smithy shape ``com.amazonaws.tnb#OperationalState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_tnb.errors import DeserializationError

OperationalState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: OperationalState) -> str:
    return value


def deserialize_json(data: str) -> OperationalState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationalState value: {data!r}")
    return cast(OperationalState, data)
