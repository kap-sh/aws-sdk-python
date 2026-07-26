"""Generated from Smithy shape ``com.amazonaws.novaact#TraceLocationType``."""

from typing import Literal, TypeAlias, cast

TraceLocationType: TypeAlias = Literal["S3",]


# --- restJson1 ser/de ---
def serialize_json(value: TraceLocationType) -> str:
    return value


def deserialize_json(data: str) -> TraceLocationType:
    return cast(TraceLocationType, data)
