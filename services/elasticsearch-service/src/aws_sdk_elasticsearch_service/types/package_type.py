"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#PackageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

PackageType: TypeAlias = Literal["TXT-DICTIONARY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TXT-DICTIONARY",))


def serialize_json(value: PackageType) -> str:
    return value


def deserialize_json(data: str) -> PackageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PackageType value: {data!r}")
    return cast(PackageType, data)
