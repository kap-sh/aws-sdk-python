"""Generated from Smithy shape ``com.amazonaws.datazone#DomainVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

DomainVersion: TypeAlias = Literal[
    "V1",
    "V2",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "V1",
        "V2",
    )
)


def serialize_json(value: DomainVersion) -> str:
    return value


def deserialize_json(data: str) -> DomainVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainVersion value: {data!r}")
    return cast(DomainVersion, data)
