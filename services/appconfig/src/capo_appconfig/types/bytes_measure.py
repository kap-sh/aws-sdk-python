"""Generated from Smithy shape ``com.amazonaws.appconfig#BytesMeasure``."""

from typing import Literal, TypeAlias, cast

BytesMeasure: TypeAlias = Literal["KILOBYTES",]


# --- restJson1 ser/de ---
def serialize_json(value: BytesMeasure) -> str:
    return value


def deserialize_json(data: str) -> BytesMeasure:
    return cast(BytesMeasure, data)
