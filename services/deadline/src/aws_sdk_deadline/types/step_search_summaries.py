"""Generated from Smithy shape ``com.amazonaws.deadline#StepSearchSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.step_search_summary

StepSearchSummaries: TypeAlias = list[
    "aws_sdk_deadline.types.step_search_summary.StepSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: StepSearchSummaries) -> list:
    import aws_sdk_deadline.types.step_search_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.step_search_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> StepSearchSummaries:
    import aws_sdk_deadline.types.step_search_summary

    out: StepSearchSummaries = []
    for item in data:
        out.append(aws_sdk_deadline.types.step_search_summary.deserialize_json(item))
    return out
