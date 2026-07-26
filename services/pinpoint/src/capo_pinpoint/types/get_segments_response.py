"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetSegmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.segments_response


class GetSegmentsResponse(TypedDict, closed=True):
    segments_response: NotRequired[
        "capo_pinpoint.types.segments_response.SegmentsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetSegmentsResponse) -> dict:
    out: dict = {}
    if "segments_response" in value:
        import capo_pinpoint.types.segments_response

        out["SegmentsResponse"] = capo_pinpoint.types.segments_response.serialize_json(
            value["segments_response"]
        )
    return out


def deserialize_json(data: dict) -> GetSegmentsResponse:
    out: GetSegmentsResponse = {}  # type: ignore[typeddict-item]
    if "SegmentsResponse" in data:
        import capo_pinpoint.types.segments_response

        out["segments_response"] = (
            capo_pinpoint.types.segments_response.deserialize_json(
                data["SegmentsResponse"]
            )
        )
    return out
