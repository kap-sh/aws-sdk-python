"""Generated from Smithy shape ``com.amazonaws.workdocs#ResourceCollectionType``."""

from typing import Literal, TypeAlias, cast

ResourceCollectionType: TypeAlias = Literal["SHARED_WITH_ME",]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceCollectionType) -> str:
    return value


def deserialize_json(data: str) -> ResourceCollectionType:
    return cast(ResourceCollectionType, data)
