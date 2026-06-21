"""Generated from Smithy shape ``com.amazonaws.configservice#MaximumExecutionFrequency``."""

from typing import Literal, TypeAlias, cast

MaximumExecutionFrequency: TypeAlias = Literal[
    "One_Hour",
    "Three_Hours",
    "Six_Hours",
    "Twelve_Hours",
    "TwentyFour_Hours",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaximumExecutionFrequency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaximumExecutionFrequency:
    return cast(MaximumExecutionFrequency, data)
