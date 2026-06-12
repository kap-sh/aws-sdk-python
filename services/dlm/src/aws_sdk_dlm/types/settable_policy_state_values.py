"""Generated from Smithy shape ``com.amazonaws.dlm#SettablePolicyStateValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dlm.errors import DeserializationError

SettablePolicyStateValues: TypeAlias = Literal[
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


def serialize_json(value: SettablePolicyStateValues) -> str:
    return value


def deserialize_json(data: str) -> SettablePolicyStateValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SettablePolicyStateValues value: {data!r}")
    return cast(SettablePolicyStateValues, data)
