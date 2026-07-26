"""Generated from Smithy shape ``com.amazonaws.emr#StepDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.step_detail

StepDetailList: TypeAlias = list["capo_emr.types.step_detail.StepDetail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepDetailList) -> list:
    import capo_emr.types.step_detail

    out: list = []
    for item in value:
        out.append(capo_emr.types.step_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StepDetailList:
    import capo_emr.types.step_detail

    out: StepDetailList = []
    for item in data:
        out.append(capo_emr.types.step_detail.deserialize_aws_json_1_1(item))
    return out
