"""Generated from Smithy shape ``com.amazonaws.bedrock#SortModelsBy``."""

from typing import Literal, TypeAlias, cast

SortModelsBy: TypeAlias = Literal["CreationTime",]


# --- restJson1 ser/de ---
def serialize_json(value: SortModelsBy) -> str:
    return value


def deserialize_json(data: str) -> SortModelsBy:
    return cast(SortModelsBy, data)
