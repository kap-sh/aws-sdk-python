"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfSegmentResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.segment_response

ListOfSegmentResponse: TypeAlias = list[
    "capo_pinpoint.types.segment_response.SegmentResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfSegmentResponse) -> list:
    import capo_pinpoint.types.segment_response

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.segment_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfSegmentResponse:
    import capo_pinpoint.types.segment_response

    out: ListOfSegmentResponse = []
    for item in data:
        out.append(capo_pinpoint.types.segment_response.deserialize_json(item))
    return out
