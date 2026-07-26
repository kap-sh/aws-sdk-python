"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLProcessingUnit``."""

from typing import Literal, TypeAlias, cast

AutoMLProcessingUnit: TypeAlias = Literal[
    "CPU",
    "GPU",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLProcessingUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLProcessingUnit:
    return cast(AutoMLProcessingUnit, data)
