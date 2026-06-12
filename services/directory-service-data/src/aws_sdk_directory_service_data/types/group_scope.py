"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#GroupScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service_data.errors import DeserializationError

GroupScope: TypeAlias = Literal[
    "DomainLocal",
    "Global",
    "Universal",
    "BuiltinLocal",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DomainLocal",
        "Global",
        "Universal",
        "BuiltinLocal",
    )
)


def serialize_json(value: GroupScope) -> str:
    return value


def deserialize_json(data: str) -> GroupScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupScope value: {data!r}")
    return cast(GroupScope, data)
