"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModuleState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ContactFlowModuleState: TypeAlias = Literal[
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


def serialize_json(value: ContactFlowModuleState) -> str:
    return value


def deserialize_json(data: str) -> ContactFlowModuleState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactFlowModuleState value: {data!r}")
    return cast(ContactFlowModuleState, data)
