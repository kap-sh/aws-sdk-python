"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesMapField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ResourcesMapField: TypeAlias = Literal["ResourceTags",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ResourceTags",))


def serialize_json(value: ResourcesMapField) -> str:
    return value


def deserialize_json(data: str) -> ResourcesMapField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourcesMapField value: {data!r}")
    return cast(ResourcesMapField, data)
