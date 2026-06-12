"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#MemberType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service_data.errors import DeserializationError

MemberType: TypeAlias = Literal[
    "USER",
    "GROUP",
    "COMPUTER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "GROUP",
        "COMPUTER",
    )
)


def serialize_json(value: MemberType) -> str:
    return value


def deserialize_json(data: str) -> MemberType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemberType value: {data!r}")
    return cast(MemberType, data)
