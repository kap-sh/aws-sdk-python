"""Generated from Smithy shape ``com.amazonaws.personalize#Solutions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.solution_summary

Solutions: TypeAlias = list["capo_personalize.types.solution_summary.SolutionSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Solutions) -> list:
    import capo_personalize.types.solution_summary

    out: list = []
    for item in value:
        out.append(capo_personalize.types.solution_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Solutions:
    import capo_personalize.types.solution_summary

    out: Solutions = []
    for item in data:
        out.append(
            capo_personalize.types.solution_summary.deserialize_aws_json_1_1(item)
        )
    return out
