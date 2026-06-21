"""Generated from Smithy shape ``com.amazonaws.budgets#AutoAdjustType``."""

from typing import Literal, TypeAlias, cast

AutoAdjustType: TypeAlias = Literal[
    "HISTORICAL",
    "FORECAST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoAdjustType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoAdjustType:
    return cast(AutoAdjustType, data)
