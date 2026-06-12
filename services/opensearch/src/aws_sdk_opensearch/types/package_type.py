"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

PackageType: TypeAlias = Literal[
    "TXT-DICTIONARY",
    "ZIP-PLUGIN",
    "PACKAGE-LICENSE",
    "PACKAGE-CONFIG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TXT-DICTIONARY",
        "ZIP-PLUGIN",
        "PACKAGE-LICENSE",
        "PACKAGE-CONFIG",
    )
)


def serialize_json(value: PackageType) -> str:
    return value


def deserialize_json(data: str) -> PackageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PackageType value: {data!r}")
    return cast(PackageType, data)
