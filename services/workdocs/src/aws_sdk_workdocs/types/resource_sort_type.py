"""Generated from Smithy shape ``com.amazonaws.workdocs#ResourceSortType``."""

from typing import Literal, TypeAlias, cast

ResourceSortType: TypeAlias = Literal[
    "DATE",
    "NAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSortType) -> str:
    return value


def deserialize_json(data: str) -> ResourceSortType:
    return cast(ResourceSortType, data)
