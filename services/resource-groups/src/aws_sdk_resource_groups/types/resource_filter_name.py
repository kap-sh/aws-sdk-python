"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ResourceFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resource_groups.errors import DeserializationError

ResourceFilterName: TypeAlias = Literal["resource-type",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("resource-type",))


def serialize_json(value: ResourceFilterName) -> str:
    return value


def deserialize_json(data: str) -> ResourceFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceFilterName value: {data!r}")
    return cast(ResourceFilterName, data)
