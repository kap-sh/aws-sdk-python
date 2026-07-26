"""Generated from Smithy shape ``com.amazonaws.sagemaker#ServerlessJobType``."""

from typing import Literal, TypeAlias, cast

ServerlessJobType: TypeAlias = Literal[
    "FineTuning",
    "Evaluation",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServerlessJobType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServerlessJobType:
    return cast(ServerlessJobType, data)
