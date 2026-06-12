"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionSortType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeartifact.errors import DeserializationError

PackageVersionSortType: TypeAlias = Literal["PUBLISHED_TIME",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PUBLISHED_TIME",))


def serialize_json(value: PackageVersionSortType) -> str:
    return value


def deserialize_json(data: str) -> PackageVersionSortType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PackageVersionSortType value: {data!r}")
    return cast(PackageVersionSortType, data)
