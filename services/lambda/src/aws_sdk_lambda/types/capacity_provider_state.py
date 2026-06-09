"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

CapacityProviderState: TypeAlias = Literal[
    "Pending",
    "Active",
    "Failed",
    "Deleting",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "Active",
        "Failed",
        "Deleting",
    )
)


def serialize_json(value: CapacityProviderState) -> str:
    return value


def deserialize_json(data: str) -> CapacityProviderState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapacityProviderState value: {data!r}")
    return cast(CapacityProviderState, data)
