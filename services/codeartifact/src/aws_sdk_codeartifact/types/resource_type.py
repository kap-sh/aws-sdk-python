"""Generated from Smithy shape ``com.amazonaws.codeartifact#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeartifact.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "domain",
    "repository",
    "package",
    "package-version",
    "asset",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "domain",
        "repository",
        "package",
        "package-version",
        "asset",
    )
)


def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
