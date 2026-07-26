"""Generated from Smithy shape ``com.amazonaws.transfer#CustomStepStatus``."""

from typing import Literal, TypeAlias, cast

CustomStepStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAILURE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomStepStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomStepStatus:
    return cast(CustomStepStatus, data)
