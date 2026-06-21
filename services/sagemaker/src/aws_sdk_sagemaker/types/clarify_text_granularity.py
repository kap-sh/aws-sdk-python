"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClarifyTextGranularity``."""

from typing import Literal, TypeAlias, cast

ClarifyTextGranularity: TypeAlias = Literal[
    "token",
    "sentence",
    "paragraph",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClarifyTextGranularity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClarifyTextGranularity:
    return cast(ClarifyTextGranularity, data)
