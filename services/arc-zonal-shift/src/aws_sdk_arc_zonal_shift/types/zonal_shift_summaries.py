"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ZonalShiftSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.zonal_shift_summary

ZonalShiftSummaries: TypeAlias = list[
    "aws_sdk_arc_zonal_shift.types.zonal_shift_summary.ZonalShiftSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ZonalShiftSummaries) -> list:
    import aws_sdk_arc_zonal_shift.types.zonal_shift_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_arc_zonal_shift.types.zonal_shift_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ZonalShiftSummaries:
    import aws_sdk_arc_zonal_shift.types.zonal_shift_summary

    out: ZonalShiftSummaries = []
    for item in data:
        out.append(
            aws_sdk_arc_zonal_shift.types.zonal_shift_summary.deserialize_json(item)
        )
    return out
