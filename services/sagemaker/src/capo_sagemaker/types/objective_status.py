"""Generated from Smithy shape ``com.amazonaws.sagemaker#ObjectiveStatus``."""

from typing import Literal, TypeAlias, cast

ObjectiveStatus: TypeAlias = Literal[
    "Succeeded",
    "Pending",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObjectiveStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ObjectiveStatus:
    return cast(ObjectiveStatus, data)
