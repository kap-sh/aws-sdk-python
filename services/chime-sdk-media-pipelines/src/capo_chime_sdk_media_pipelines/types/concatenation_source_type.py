"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ConcatenationSourceType``."""

from typing import Literal, TypeAlias, cast

ConcatenationSourceType: TypeAlias = Literal["MediaCapturePipeline",]


# --- restJson1 ser/de ---
def serialize_json(value: ConcatenationSourceType) -> str:
    return value


def deserialize_json(data: str) -> ConcatenationSourceType:
    return cast(ConcatenationSourceType, data)
