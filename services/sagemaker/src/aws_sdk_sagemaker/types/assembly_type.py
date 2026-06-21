"""Generated from Smithy shape ``com.amazonaws.sagemaker#AssemblyType``."""

from typing import Literal, TypeAlias, cast

AssemblyType: TypeAlias = Literal[
    "None",
    "Line",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssemblyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssemblyType:
    return cast(AssemblyType, data)
