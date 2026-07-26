"""Generated from Smithy shape ``com.amazonaws.entityresolution#IncrementalRunType``."""

from typing import Literal, TypeAlias, cast

IncrementalRunType: TypeAlias = Literal["IMMEDIATE",]


# --- restJson1 ser/de ---
def serialize_json(value: IncrementalRunType) -> str:
    return value


def deserialize_json(data: str) -> IncrementalRunType:
    return cast(IncrementalRunType, data)
