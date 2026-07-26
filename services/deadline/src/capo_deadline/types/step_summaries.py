"""Generated from Smithy shape ``com.amazonaws.deadline#StepSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.step_summary

StepSummaries: TypeAlias = list["capo_deadline.types.step_summary.StepSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: StepSummaries) -> list:
    import capo_deadline.types.step_summary

    out: list = []
    for item in value:
        out.append(capo_deadline.types.step_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> StepSummaries:
    import capo_deadline.types.step_summary

    out: StepSummaries = []
    for item in data:
        out.append(capo_deadline.types.step_summary.deserialize_json(item))
    return out
