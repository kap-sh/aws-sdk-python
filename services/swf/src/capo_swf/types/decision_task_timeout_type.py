"""Generated from Smithy shape ``com.amazonaws.swf#DecisionTaskTimeoutType``."""

from typing import Literal, TypeAlias, cast

DecisionTaskTimeoutType: TypeAlias = Literal[
    "START_TO_CLOSE",
    "SCHEDULE_TO_START",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DecisionTaskTimeoutType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DecisionTaskTimeoutType:
    return cast(DecisionTaskTimeoutType, data)
