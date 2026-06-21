"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesMapField``."""

from typing import Literal, TypeAlias, cast

ResourcesMapField: TypeAlias = Literal["ResourceTags",]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesMapField) -> str:
    return value


def deserialize_json(data: str) -> ResourcesMapField:
    return cast(ResourcesMapField, data)
