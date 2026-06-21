"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppStatus``."""

from typing import Literal, TypeAlias, cast

AppStatus: TypeAlias = Literal[
    "Deleted",
    "Deleting",
    "Failed",
    "InService",
    "Pending",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppStatus:
    return cast(AppStatus, data)
