"""Generated from Smithy shape ``com.amazonaws.personalize#SolutionVersions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.solution_version_summary

SolutionVersions: TypeAlias = list[
    "capo_personalize.types.solution_version_summary.SolutionVersionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SolutionVersions) -> list:
    import capo_personalize.types.solution_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_personalize.types.solution_version_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SolutionVersions:
    import capo_personalize.types.solution_version_summary

    out: SolutionVersions = []
    for item in data:
        out.append(
            capo_personalize.types.solution_version_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
