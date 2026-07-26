"""Generated from Smithy shape ``com.amazonaws.emr#StepSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.step_summary

StepSummaryList: TypeAlias = list["capo_emr.types.step_summary.StepSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepSummaryList) -> list:
    import capo_emr.types.step_summary

    out: list = []
    for item in value:
        out.append(capo_emr.types.step_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StepSummaryList:
    import capo_emr.types.step_summary

    out: StepSummaryList = []
    for item in data:
        out.append(capo_emr.types.step_summary.deserialize_aws_json_1_1(item))
    return out
