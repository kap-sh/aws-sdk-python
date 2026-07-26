"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CheckSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.check_summary

CheckSummaries: TypeAlias = list[
    "capo_wellarchitected.types.check_summary.CheckSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CheckSummaries) -> list:
    import capo_wellarchitected.types.check_summary

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.check_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CheckSummaries:
    import capo_wellarchitected.types.check_summary

    out: CheckSummaries = []
    for item in data:
        out.append(capo_wellarchitected.types.check_summary.deserialize_json(item))
    return out
