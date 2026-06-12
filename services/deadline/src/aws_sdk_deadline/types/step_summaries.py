"""Generated from Smithy shape ``com.amazonaws.deadline#StepSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.step_summary

StepSummaries: TypeAlias = list["aws_sdk_deadline.types.step_summary.StepSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: StepSummaries) -> list:
    import aws_sdk_deadline.types.step_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.step_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> StepSummaries:
    import aws_sdk_deadline.types.step_summary

    out: StepSummaries = []
    for item in data:
        out.append(aws_sdk_deadline.types.step_summary.deserialize_json(item))
    return out
