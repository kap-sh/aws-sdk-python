"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetSegmentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.segments_response


class GetSegmentsResponse(TypedDict):
    segments_response: NotRequired[
        "aws_sdk_pinpoint.types.segments_response.SegmentsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetSegmentsResponse) -> dict:
    out: dict = {}
    if "segments_response" in value:
        import aws_sdk_pinpoint.types.segments_response

        out["SegmentsResponse"] = (
            aws_sdk_pinpoint.types.segments_response.serialize_json(
                value["segments_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSegmentsResponse:
    out: GetSegmentsResponse = {}  # type: ignore[typeddict-item]
    if "SegmentsResponse" in data:
        import aws_sdk_pinpoint.types.segments_response

        out["segments_response"] = (
            aws_sdk_pinpoint.types.segments_response.deserialize_json(
                data["SegmentsResponse"]
            )
        )
    return out
