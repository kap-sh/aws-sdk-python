"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ImprovementSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.improvement_summary

ImprovementSummaries: TypeAlias = list[
    "capo_wellarchitected.types.improvement_summary.ImprovementSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImprovementSummaries) -> list:
    import capo_wellarchitected.types.improvement_summary

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.improvement_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImprovementSummaries:
    import capo_wellarchitected.types.improvement_summary

    out: ImprovementSummaries = []
    for item in data:
        out.append(
            capo_wellarchitected.types.improvement_summary.deserialize_json(item)
        )
    return out
