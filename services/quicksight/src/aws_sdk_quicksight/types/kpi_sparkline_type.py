"""Generated from Smithy shape ``com.amazonaws.quicksight#KPISparklineType``."""

from typing import Literal, TypeAlias, cast

KPISparklineType: TypeAlias = Literal[
    "LINE",
    "AREA",
]


# --- restJson1 ser/de ---
def serialize_json(value: KPISparklineType) -> str:
    return value


def deserialize_json(data: str) -> KPISparklineType:
    return cast(KPISparklineType, data)
