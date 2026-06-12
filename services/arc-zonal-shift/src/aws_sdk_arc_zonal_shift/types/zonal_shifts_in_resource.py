"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ZonalShiftsInResource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.zonal_shift_in_resource

ZonalShiftsInResource: TypeAlias = list[
    "aws_sdk_arc_zonal_shift.types.zonal_shift_in_resource.ZonalShiftInResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ZonalShiftsInResource) -> list:
    import aws_sdk_arc_zonal_shift.types.zonal_shift_in_resource

    out: list = []
    for item in value:
        out.append(
            aws_sdk_arc_zonal_shift.types.zonal_shift_in_resource.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ZonalShiftsInResource:
    import aws_sdk_arc_zonal_shift.types.zonal_shift_in_resource

    out: ZonalShiftsInResource = []
    for item in data:
        out.append(
            aws_sdk_arc_zonal_shift.types.zonal_shift_in_resource.deserialize_json(item)
        )
    return out
