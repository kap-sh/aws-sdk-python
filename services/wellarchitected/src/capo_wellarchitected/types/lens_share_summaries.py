"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensShareSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_share_summary

LensShareSummaries: TypeAlias = list[
    "capo_wellarchitected.types.lens_share_summary.LensShareSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: LensShareSummaries) -> list:
    import capo_wellarchitected.types.lens_share_summary

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.lens_share_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> LensShareSummaries:
    import capo_wellarchitected.types.lens_share_summary

    out: LensShareSummaries = []
    for item in data:
        out.append(capo_wellarchitected.types.lens_share_summary.deserialize_json(item))
    return out
