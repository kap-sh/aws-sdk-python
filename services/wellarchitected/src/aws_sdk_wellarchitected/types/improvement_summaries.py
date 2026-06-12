"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ImprovementSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.improvement_summary

ImprovementSummaries: TypeAlias = list[
    "aws_sdk_wellarchitected.types.improvement_summary.ImprovementSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImprovementSummaries) -> list:
    import aws_sdk_wellarchitected.types.improvement_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wellarchitected.types.improvement_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ImprovementSummaries:
    import aws_sdk_wellarchitected.types.improvement_summary

    out: ImprovementSummaries = []
    for item in data:
        out.append(
            aws_sdk_wellarchitected.types.improvement_summary.deserialize_json(item)
        )
    return out
