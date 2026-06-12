"""Generated from Smithy shape ``com.amazonaws.dlm#GettablePolicyStateValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dlm.errors import DeserializationError

GettablePolicyStateValues: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "ERROR",
    )
)


def serialize_json(value: GettablePolicyStateValues) -> str:
    return value


def deserialize_json(data: str) -> GettablePolicyStateValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GettablePolicyStateValues value: {data!r}")
    return cast(GettablePolicyStateValues, data)
