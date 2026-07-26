"""Generated from Smithy shape ``com.amazonaws.datazone#SortFieldProject``."""

from typing import Literal, TypeAlias, cast

SortFieldProject: TypeAlias = Literal["NAME",]


# --- restJson1 ser/de ---
def serialize_json(value: SortFieldProject) -> str:
    return value


def deserialize_json(data: str) -> SortFieldProject:
    return cast(SortFieldProject, data)
