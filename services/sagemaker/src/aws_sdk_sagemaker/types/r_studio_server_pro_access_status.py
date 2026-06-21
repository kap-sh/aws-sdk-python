"""Generated from Smithy shape ``com.amazonaws.sagemaker#RStudioServerProAccessStatus``."""

from typing import Literal, TypeAlias, cast

RStudioServerProAccessStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RStudioServerProAccessStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RStudioServerProAccessStatus:
    return cast(RStudioServerProAccessStatus, data)
