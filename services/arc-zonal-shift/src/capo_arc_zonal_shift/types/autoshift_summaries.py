"""Generated from Smithy shape ``com.amazonaws.arczonalshift#AutoshiftSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.autoshift_summary

AutoshiftSummaries: TypeAlias = list[
    "capo_arc_zonal_shift.types.autoshift_summary.AutoshiftSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoshiftSummaries) -> list:
    import capo_arc_zonal_shift.types.autoshift_summary

    out: list = []
    for item in value:
        out.append(capo_arc_zonal_shift.types.autoshift_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AutoshiftSummaries:
    import capo_arc_zonal_shift.types.autoshift_summary

    out: AutoshiftSummaries = []
    for item in data:
        out.append(capo_arc_zonal_shift.types.autoshift_summary.deserialize_json(item))
    return out
