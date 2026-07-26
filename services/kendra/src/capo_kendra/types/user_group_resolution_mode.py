"""Generated from Smithy shape ``com.amazonaws.kendra#UserGroupResolutionMode``."""

from typing import Literal, TypeAlias, cast

UserGroupResolutionMode: TypeAlias = Literal[
    "AWS_SSO",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserGroupResolutionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserGroupResolutionMode:
    return cast(UserGroupResolutionMode, data)
