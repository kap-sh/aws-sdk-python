"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionOriginType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeartifact.errors import DeserializationError

PackageVersionOriginType: TypeAlias = Literal[
    "INTERNAL",
    "EXTERNAL",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERNAL",
        "EXTERNAL",
        "UNKNOWN",
    )
)


def serialize_json(value: PackageVersionOriginType) -> str:
    return value


def deserialize_json(data: str) -> PackageVersionOriginType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PackageVersionOriginType value: {data!r}")
    return cast(PackageVersionOriginType, data)
