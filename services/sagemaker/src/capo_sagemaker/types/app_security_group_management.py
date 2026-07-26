"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppSecurityGroupManagement``."""

from typing import Literal, TypeAlias, cast

AppSecurityGroupManagement: TypeAlias = Literal[
    "Service",
    "Customer",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppSecurityGroupManagement) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppSecurityGroupManagement:
    return cast(AppSecurityGroupManagement, data)
