"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpdateActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_clouddirectory.errors import DeserializationError

UpdateActionType: TypeAlias = Literal[
    "CREATE_OR_UPDATE",
    "DELETE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_OR_UPDATE",
        "DELETE",
    )
)


def serialize_json(value: UpdateActionType) -> str:
    return value


def deserialize_json(data: str) -> UpdateActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateActionType value: {data!r}")
    return cast(UpdateActionType, data)
