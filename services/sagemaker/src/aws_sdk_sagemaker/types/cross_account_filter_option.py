"""Generated from Smithy shape ``com.amazonaws.sagemaker#CrossAccountFilterOption``."""

from typing import Literal, TypeAlias, cast

CrossAccountFilterOption: TypeAlias = Literal[
    "SameAccount",
    "CrossAccount",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrossAccountFilterOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CrossAccountFilterOption:
    return cast(CrossAccountFilterOption, data)
