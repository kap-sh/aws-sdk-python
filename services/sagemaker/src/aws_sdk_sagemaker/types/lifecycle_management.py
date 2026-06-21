"""Generated from Smithy shape ``com.amazonaws.sagemaker#LifecycleManagement``."""

from typing import Literal, TypeAlias, cast

LifecycleManagement: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecycleManagement) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LifecycleManagement:
    return cast(LifecycleManagement, data)
