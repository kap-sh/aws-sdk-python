"""Generated from Smithy shape ``com.amazonaws.securityir#ActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_security_ir.errors import DeserializationError

ActionType: TypeAlias = Literal[
    "Evidence",
    "Investigation",
    "Summarization",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Evidence",
        "Investigation",
        "Summarization",
    )
)


def serialize_json(value: ActionType) -> str:
    return value


def deserialize_json(data: str) -> ActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionType value: {data!r}")
    return cast(ActionType, data)
