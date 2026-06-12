"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateSegmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.segment_response


class UpdateSegmentResponse(TypedDict):
    segment_response: NotRequired[
        "aws_sdk_pinpoint.types.segment_response.SegmentResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSegmentResponse) -> dict:
    out: dict = {}
    if "segment_response" in value:
        import aws_sdk_pinpoint.types.segment_response

        out["SegmentResponse"] = aws_sdk_pinpoint.types.segment_response.serialize_json(
            value["segment_response"]
        )
    return out


def deserialize_json(data: dict) -> UpdateSegmentResponse:
    out: UpdateSegmentResponse = {}  # type: ignore[typeddict-item]
    if "SegmentResponse" in data:
        import aws_sdk_pinpoint.types.segment_response

        out["segment_response"] = (
            aws_sdk_pinpoint.types.segment_response.deserialize_json(
                data["SegmentResponse"]
            )
        )
    return out
