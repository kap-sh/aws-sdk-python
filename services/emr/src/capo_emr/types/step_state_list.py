"""Generated from Smithy shape ``com.amazonaws.emr#StepStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.step_state

StepStateList: TypeAlias = list["capo_emr.types.step_state.StepState"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepStateList) -> list:
    import capo_emr.types.step_state

    out: list = []
    for item in value:
        out.append(capo_emr.types.step_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StepStateList:
    import capo_emr.types.step_state

    out: StepStateList = []
    for item in data:
        out.append(capo_emr.types.step_state.deserialize_aws_json_1_1(item))
    return out
