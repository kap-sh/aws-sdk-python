"""Generated from Smithy shape ``com.amazonaws.emr#StepStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

StepStateChangeReasonCode: TypeAlias = Literal["NONE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StepStateChangeReasonCode:
    return cast(StepStateChangeReasonCode, data)
