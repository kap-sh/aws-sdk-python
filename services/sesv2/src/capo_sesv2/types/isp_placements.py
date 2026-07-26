"""Generated from Smithy shape ``com.amazonaws.sesv2#IspPlacements``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.isp_placement

IspPlacements: TypeAlias = list["capo_sesv2.types.isp_placement.IspPlacement"]


# --- restJson1 ser/de ---
def serialize_json(value: IspPlacements) -> list:
    import capo_sesv2.types.isp_placement

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.isp_placement.serialize_json(item))
    return out


def deserialize_json(data: list) -> IspPlacements:
    import capo_sesv2.types.isp_placement

    out: IspPlacements = []
    for item in data:
        out.append(capo_sesv2.types.isp_placement.deserialize_json(item))
    return out
