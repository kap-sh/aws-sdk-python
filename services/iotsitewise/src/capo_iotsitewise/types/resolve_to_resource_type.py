"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ResolveToResourceType``."""

from typing import Literal, TypeAlias, cast

ResolveToResourceType: TypeAlias = Literal["ASSET",]


# --- restJson1 ser/de ---
def serialize_json(value: ResolveToResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResolveToResourceType:
    return cast(ResolveToResourceType, data)
