"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMountHomeEFS``."""

from typing import Literal, TypeAlias, cast

AutoMountHomeEFS: TypeAlias = Literal[
    "Enabled",
    "Disabled",
    "DefaultAsDomain",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMountHomeEFS) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMountHomeEFS:
    return cast(AutoMountHomeEFS, data)
