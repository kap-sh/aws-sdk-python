"""Generated from Smithy shape ``com.amazonaws.emr#AdjustmentType``."""

from typing import Literal, TypeAlias, cast

AdjustmentType: TypeAlias = Literal[
    "CHANGE_IN_CAPACITY",
    "PERCENT_CHANGE_IN_CAPACITY",
    "EXACT_CAPACITY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdjustmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdjustmentType:
    return cast(AdjustmentType, data)
