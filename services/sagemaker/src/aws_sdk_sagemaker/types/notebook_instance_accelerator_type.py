"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceAcceleratorType``."""

from typing import Literal, TypeAlias, cast

NotebookInstanceAcceleratorType: TypeAlias = Literal[
    "ml.eia1.medium",
    "ml.eia1.large",
    "ml.eia1.xlarge",
    "ml.eia2.medium",
    "ml.eia2.large",
    "ml.eia2.xlarge",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookInstanceAcceleratorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookInstanceAcceleratorType:
    return cast(NotebookInstanceAcceleratorType, data)
