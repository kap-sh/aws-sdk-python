"""Generated from Smithy shape ``com.amazonaws.sagemaker#DirectInternetAccess``."""

from typing import Literal, TypeAlias, cast

DirectInternetAccess: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectInternetAccess) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectInternetAccess:
    return cast(DirectInternetAccess, data)
