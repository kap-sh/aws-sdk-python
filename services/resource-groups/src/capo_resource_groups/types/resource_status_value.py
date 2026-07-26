"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ResourceStatusValue``."""

from typing import Literal, TypeAlias, cast

ResourceStatusValue: TypeAlias = Literal["PENDING",]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStatusValue) -> str:
    return value


def deserialize_json(data: str) -> ResourceStatusValue:
    return cast(ResourceStatusValue, data)
