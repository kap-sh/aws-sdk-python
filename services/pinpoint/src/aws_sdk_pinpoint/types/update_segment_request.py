"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateSegmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.write_segment_request


class UpdateSegmentRequest(TypedDict):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    segment_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the segment.</p>"""
    write_segment_request: NotRequired[
        "aws_sdk_pinpoint.types.write_segment_request.WriteSegmentRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSegmentRequest) -> dict:
    out: dict = {}
    if "write_segment_request" in value:
        import aws_sdk_pinpoint.types.write_segment_request

        out["WriteSegmentRequest"] = (
            aws_sdk_pinpoint.types.write_segment_request.serialize_json(
                value["write_segment_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSegmentRequest:
    out: UpdateSegmentRequest = {}  # type: ignore[typeddict-item]
    if "WriteSegmentRequest" in data:
        import aws_sdk_pinpoint.types.write_segment_request

        out["write_segment_request"] = (
            aws_sdk_pinpoint.types.write_segment_request.deserialize_json(
                data["WriteSegmentRequest"]
            )
        )
    return out
