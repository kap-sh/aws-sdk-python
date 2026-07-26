"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ResourceFilterName``."""

from typing import Literal, TypeAlias, cast

ResourceFilterName: TypeAlias = Literal["resource-type",]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceFilterName) -> str:
    return value


def deserialize_json(data: str) -> ResourceFilterName:
    return cast(ResourceFilterName, data)
