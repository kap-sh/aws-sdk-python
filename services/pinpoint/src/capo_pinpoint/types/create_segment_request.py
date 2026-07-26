"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreateSegmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.write_segment_request


class CreateSegmentRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    write_segment_request: NotRequired[
        "capo_pinpoint.types.write_segment_request.WriteSegmentRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateSegmentRequest) -> dict:
    out: dict = {}
    if "write_segment_request" in value:
        import capo_pinpoint.types.write_segment_request

        out["WriteSegmentRequest"] = (
            capo_pinpoint.types.write_segment_request.serialize_json(
                value["write_segment_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSegmentRequest:
    out: CreateSegmentRequest = {}  # type: ignore[typeddict-item]
    if "WriteSegmentRequest" in data:
        import capo_pinpoint.types.write_segment_request

        out["write_segment_request"] = (
            capo_pinpoint.types.write_segment_request.deserialize_json(
                data["WriteSegmentRequest"]
            )
        )
    return out
