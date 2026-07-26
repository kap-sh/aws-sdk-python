"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ModelVersionSourceType``."""

from typing import Literal, TypeAlias, cast

ModelVersionSourceType: TypeAlias = Literal[
    "TRAINING",
    "RETRAINING",
    "IMPORT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ModelVersionSourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ModelVersionSourceType:
    return cast(ModelVersionSourceType, data)
