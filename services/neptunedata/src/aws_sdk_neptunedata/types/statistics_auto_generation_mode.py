"""Generated from Smithy shape ``com.amazonaws.neptunedata#StatisticsAutoGenerationMode``."""

from typing import Literal, TypeAlias, cast

StatisticsAutoGenerationMode: TypeAlias = Literal[
    "disableAutoCompute",
    "enableAutoCompute",
    "refresh",
]


# --- restJson1 ser/de ---
def serialize_json(value: StatisticsAutoGenerationMode) -> str:
    return value


def deserialize_json(data: str) -> StatisticsAutoGenerationMode:
    return cast(StatisticsAutoGenerationMode, data)
