"""Generated from Smithy shape ``com.amazonaws.sagemaker#WorkforceStatus``."""

from typing import Literal, TypeAlias, cast

WorkforceStatus: TypeAlias = Literal[
    "Initializing",
    "Updating",
    "Deleting",
    "Failed",
    "Active",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkforceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkforceStatus:
    return cast(WorkforceStatus, data)
