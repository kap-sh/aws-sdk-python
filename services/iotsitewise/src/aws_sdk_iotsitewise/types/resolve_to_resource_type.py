"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ResolveToResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

ResolveToResourceType: TypeAlias = Literal["ASSET",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ASSET",))


def serialize_json(value: ResolveToResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResolveToResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResolveToResourceType value: {data!r}")
    return cast(ResolveToResourceType, data)
