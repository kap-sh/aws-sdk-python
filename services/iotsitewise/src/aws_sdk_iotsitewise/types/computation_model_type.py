"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelType``."""

from typing import Literal, TypeAlias, cast

ComputationModelType: TypeAlias = Literal["ANOMALY_DETECTION",]


# --- restJson1 ser/de ---
def serialize_json(value: ComputationModelType) -> str:
    return value


def deserialize_json(data: str) -> ComputationModelType:
    return cast(ComputationModelType, data)
