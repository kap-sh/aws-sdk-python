"""Generated from Smithy shape ``com.amazonaws.sagemaker#RStudioServerProUserGroup``."""

from typing import Literal, TypeAlias, cast

RStudioServerProUserGroup: TypeAlias = Literal[
    "R_STUDIO_ADMIN",
    "R_STUDIO_USER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RStudioServerProUserGroup) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RStudioServerProUserGroup:
    return cast(RStudioServerProUserGroup, data)
