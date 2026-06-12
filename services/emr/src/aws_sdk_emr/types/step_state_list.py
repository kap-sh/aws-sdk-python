"""Generated from Smithy shape ``com.amazonaws.emr#StepStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.step_state

StepStateList: TypeAlias = list["aws_sdk_emr.types.step_state.StepState"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepStateList) -> list:
    import aws_sdk_emr.types.step_state

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.step_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StepStateList:
    import aws_sdk_emr.types.step_state

    out: StepStateList = []
    for item in data:
        out.append(aws_sdk_emr.types.step_state.deserialize_aws_json_1_1(item))
    return out
