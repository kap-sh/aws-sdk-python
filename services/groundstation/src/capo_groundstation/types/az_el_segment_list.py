"""Generated from Smithy shape ``com.amazonaws.groundstation#AzElSegmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.az_el_segment

AzElSegmentList: TypeAlias = list["capo_groundstation.types.az_el_segment.AzElSegment"]


# --- restJson1 ser/de ---
def serialize_json(value: AzElSegmentList) -> list:
    import capo_groundstation.types.az_el_segment

    out: list = []
    for item in value:
        out.append(capo_groundstation.types.az_el_segment.serialize_json(item))
    return out


def deserialize_json(data: list) -> AzElSegmentList:
    import capo_groundstation.types.az_el_segment

    out: AzElSegmentList = []
    for item in data:
        out.append(capo_groundstation.types.az_el_segment.deserialize_json(item))
    return out
