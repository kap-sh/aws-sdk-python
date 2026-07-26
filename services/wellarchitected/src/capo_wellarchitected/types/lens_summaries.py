"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_summary

LensSummaries: TypeAlias = list["capo_wellarchitected.types.lens_summary.LensSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: LensSummaries) -> list:
    import capo_wellarchitected.types.lens_summary

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.lens_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> LensSummaries:
    import capo_wellarchitected.types.lens_summary

    out: LensSummaries = []
    for item in data:
        out.append(capo_wellarchitected.types.lens_summary.deserialize_json(item))
    return out
