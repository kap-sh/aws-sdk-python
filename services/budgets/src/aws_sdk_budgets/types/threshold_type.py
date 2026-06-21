"""Generated from Smithy shape ``com.amazonaws.budgets#ThresholdType``."""

from typing import Literal, TypeAlias, cast

"""<p> The type of threshold for a notification.</p>"""
ThresholdType: TypeAlias = Literal[
    "PERCENTAGE",
    "ABSOLUTE_VALUE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThresholdType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThresholdType:
    return cast(ThresholdType, data)
