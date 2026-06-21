"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ConcatenationSinkType``."""

from typing import Literal, TypeAlias, cast

ConcatenationSinkType: TypeAlias = Literal["S3Bucket",]


# --- restJson1 ser/de ---
def serialize_json(value: ConcatenationSinkType) -> str:
    return value


def deserialize_json(data: str) -> ConcatenationSinkType:
    return cast(ConcatenationSinkType, data)
