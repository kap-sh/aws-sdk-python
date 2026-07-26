"""Generated from Smithy shape ``com.amazonaws.devopsguru#ResourceCollectionType``."""

from typing import Literal, TypeAlias, cast

ResourceCollectionType: TypeAlias = Literal[
    "AWS_CLOUD_FORMATION",
    "AWS_SERVICE",
    "AWS_TAGS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceCollectionType) -> str:
    return value


def deserialize_json(data: str) -> ResourceCollectionType:
    return cast(ResourceCollectionType, data)
