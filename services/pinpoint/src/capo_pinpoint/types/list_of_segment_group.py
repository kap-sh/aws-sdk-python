"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfSegmentGroup``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.segment_group

ListOfSegmentGroup: TypeAlias = list["capo_pinpoint.types.segment_group.SegmentGroup"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfSegmentGroup) -> list:
    import capo_pinpoint.types.segment_group

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.segment_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfSegmentGroup:
    import capo_pinpoint.types.segment_group

    out: ListOfSegmentGroup = []
    for item in data:
        out.append(capo_pinpoint.types.segment_group.deserialize_json(item))
    return out
