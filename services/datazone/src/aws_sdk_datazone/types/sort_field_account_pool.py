"""Generated from Smithy shape ``com.amazonaws.datazone#SortFieldAccountPool``."""

from typing import Literal, TypeAlias, cast

SortFieldAccountPool: TypeAlias = Literal["NAME",]


# --- restJson1 ser/de ---
def serialize_json(value: SortFieldAccountPool) -> str:
    return value


def deserialize_json(data: str) -> SortFieldAccountPool:
    return cast(SortFieldAccountPool, data)
