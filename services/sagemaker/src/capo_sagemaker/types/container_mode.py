"""Generated from Smithy shape ``com.amazonaws.sagemaker#ContainerMode``."""

from typing import Literal, TypeAlias, cast

ContainerMode: TypeAlias = Literal[
    "SingleModel",
    "MultiModel",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerMode:
    return cast(ContainerMode, data)
