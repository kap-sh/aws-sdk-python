"""Generated from Smithy shape ``com.amazonaws.groundstation#TelemetrySinkType``."""

from typing import Literal, TypeAlias, cast

TelemetrySinkType: TypeAlias = Literal["KINESIS_DATA_STREAM",]


# --- restJson1 ser/de ---
def serialize_json(value: TelemetrySinkType) -> str:
    return value


def deserialize_json(data: str) -> TelemetrySinkType:
    return cast(TelemetrySinkType, data)
