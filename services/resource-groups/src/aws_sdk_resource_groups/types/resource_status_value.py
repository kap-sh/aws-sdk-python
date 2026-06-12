"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ResourceStatusValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resource_groups.errors import DeserializationError

ResourceStatusValue: TypeAlias = Literal["PENDING",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PENDING",))


def serialize_json(value: ResourceStatusValue) -> str:
    return value


def deserialize_json(data: str) -> ResourceStatusValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceStatusValue value: {data!r}")
    return cast(ResourceStatusValue, data)
