"""Generated from Smithy shape ``com.amazonaws.tnb#PackageContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_tnb.errors import DeserializationError

PackageContentType: TypeAlias = Literal["application/zip",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("application/zip",))


def serialize_json(value: PackageContentType) -> str:
    return value


def deserialize_json(data: str) -> PackageContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PackageContentType value: {data!r}")
    return cast(PackageContentType, data)
