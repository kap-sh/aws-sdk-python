"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingIncrementalRunType``."""

from typing import Literal, TypeAlias, cast

IdMappingIncrementalRunType: TypeAlias = Literal["ON_DEMAND",]


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingIncrementalRunType) -> str:
    return value


def deserialize_json(data: str) -> IdMappingIncrementalRunType:
    return cast(IdMappingIncrementalRunType, data)
