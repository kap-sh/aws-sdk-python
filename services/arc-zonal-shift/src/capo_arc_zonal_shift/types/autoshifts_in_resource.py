"""Generated from Smithy shape ``com.amazonaws.arczonalshift#AutoshiftsInResource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.autoshift_in_resource

AutoshiftsInResource: TypeAlias = list[
    "capo_arc_zonal_shift.types.autoshift_in_resource.AutoshiftInResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoshiftsInResource) -> list:
    import capo_arc_zonal_shift.types.autoshift_in_resource

    out: list = []
    for item in value:
        out.append(
            capo_arc_zonal_shift.types.autoshift_in_resource.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutoshiftsInResource:
    import capo_arc_zonal_shift.types.autoshift_in_resource

    out: AutoshiftsInResource = []
    for item in data:
        out.append(
            capo_arc_zonal_shift.types.autoshift_in_resource.deserialize_json(item)
        )
    return out
