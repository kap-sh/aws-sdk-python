"""Generated from Smithy shape ``com.amazonaws.wellarchitected#MilestoneSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.milestone_summary

MilestoneSummaries: TypeAlias = list[
    "aws_sdk_wellarchitected.types.milestone_summary.MilestoneSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MilestoneSummaries) -> list:
    import aws_sdk_wellarchitected.types.milestone_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_wellarchitected.types.milestone_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MilestoneSummaries:
    import aws_sdk_wellarchitected.types.milestone_summary

    out: MilestoneSummaries = []
    for item in data:
        out.append(
            aws_sdk_wellarchitected.types.milestone_summary.deserialize_json(item)
        )
    return out
