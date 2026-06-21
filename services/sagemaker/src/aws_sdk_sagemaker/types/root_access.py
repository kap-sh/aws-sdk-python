"""Generated from Smithy shape ``com.amazonaws.sagemaker#RootAccess``."""

from typing import Literal, TypeAlias, cast

RootAccess: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RootAccess) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RootAccess:
    return cast(RootAccess, data)
