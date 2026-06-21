"""Generated from Smithy shape ``com.amazonaws.sagemaker#Processor``."""

from typing import Literal, TypeAlias, cast

Processor: TypeAlias = Literal[
    "CPU",
    "GPU",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Processor) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Processor:
    return cast(Processor, data)
