"""Generated from Smithy shape ``com.amazonaws.xray#SamplingStrategyName``."""

from typing import Literal, TypeAlias, cast

SamplingStrategyName: TypeAlias = Literal[
    "PartialScan",
    "FixedRate",
]


# --- restJson1 ser/de ---
def serialize_json(value: SamplingStrategyName) -> str:
    return value


def deserialize_json(data: str) -> SamplingStrategyName:
    return cast(SamplingStrategyName, data)
