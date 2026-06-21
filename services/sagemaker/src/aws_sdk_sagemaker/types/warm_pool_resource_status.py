"""Generated from Smithy shape ``com.amazonaws.sagemaker#WarmPoolResourceStatus``."""

from typing import Literal, TypeAlias, cast

WarmPoolResourceStatus: TypeAlias = Literal[
    "Available",
    "Terminated",
    "Reused",
    "InUse",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WarmPoolResourceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WarmPoolResourceStatus:
    return cast(WarmPoolResourceStatus, data)
