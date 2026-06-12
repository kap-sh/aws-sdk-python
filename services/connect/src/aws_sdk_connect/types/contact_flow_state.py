"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ContactFlowState: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "ARCHIVED",
    )
)


def serialize_json(value: ContactFlowState) -> str:
    return value


def deserialize_json(data: str) -> ContactFlowState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactFlowState value: {data!r}")
    return cast(ContactFlowState, data)
