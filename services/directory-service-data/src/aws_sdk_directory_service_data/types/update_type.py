"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#UpdateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service_data.errors import DeserializationError

UpdateType: TypeAlias = Literal[
    "ADD",
    "REPLACE",
    "REMOVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADD",
        "REPLACE",
        "REMOVE",
    )
)


def serialize_json(value: UpdateType) -> str:
    return value


def deserialize_json(data: str) -> UpdateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateType value: {data!r}")
    return cast(UpdateType, data)
