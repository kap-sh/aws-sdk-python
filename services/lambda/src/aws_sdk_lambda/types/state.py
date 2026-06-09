"""Generated from Smithy shape ``com.amazonaws.lambda#State``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

State: TypeAlias = Literal[
    "Pending",
    "Active",
    "Inactive",
    "Failed",
    "Deactivating",
    "Deactivated",
    "ActiveNonInvocable",
    "Deleting",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "Active",
        "Inactive",
        "Failed",
        "Deactivating",
        "Deactivated",
        "ActiveNonInvocable",
        "Deleting",
    )
)


def serialize_json(value: State) -> str:
    return value


def deserialize_json(data: str) -> State:
    if data not in _VALUES:
        raise DeserializationError(f"unknown State value: {data!r}")
    return cast(State, data)
