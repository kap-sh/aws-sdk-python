"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ModelQuality``."""

from typing import Literal, TypeAlias, cast

ModelQuality: TypeAlias = Literal[
    "QUALITY_THRESHOLD_MET",
    "CANNOT_DETERMINE_QUALITY",
    "POOR_QUALITY_DETECTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ModelQuality) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ModelQuality:
    return cast(ModelQuality, data)
