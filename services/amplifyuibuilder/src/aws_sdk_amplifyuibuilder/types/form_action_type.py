"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifyuibuilder.errors import DeserializationError

FormActionType: TypeAlias = Literal[
    "create",
    "update",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "create",
        "update",
    )
)


def serialize_json(value: FormActionType) -> str:
    return value


def deserialize_json(data: str) -> FormActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FormActionType value: {data!r}")
    return cast(FormActionType, data)
