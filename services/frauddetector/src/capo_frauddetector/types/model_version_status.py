"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelVersionStatus``."""

from typing import Literal, TypeAlias, cast

ModelVersionStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "TRAINING_CANCELLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelVersionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelVersionStatus:
    return cast(ModelVersionStatus, data)
