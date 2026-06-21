"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLMode``."""

from typing import Literal, TypeAlias, cast

AutoMLMode: TypeAlias = Literal[
    "AUTO",
    "ENSEMBLING",
    "HYPERPARAMETER_TUNING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLMode:
    return cast(AutoMLMode, data)
