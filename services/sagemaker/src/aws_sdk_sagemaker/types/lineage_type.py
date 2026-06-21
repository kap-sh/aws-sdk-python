"""Generated from Smithy shape ``com.amazonaws.sagemaker#LineageType``."""

from typing import Literal, TypeAlias, cast

LineageType: TypeAlias = Literal[
    "TrialComponent",
    "Artifact",
    "Context",
    "Action",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LineageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LineageType:
    return cast(LineageType, data)
