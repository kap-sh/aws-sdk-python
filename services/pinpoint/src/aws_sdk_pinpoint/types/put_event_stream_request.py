"""Generated from Smithy shape ``com.amazonaws.pinpoint#PutEventStreamRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.write_event_stream


class PutEventStreamRequest(TypedDict):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    write_event_stream: NotRequired[
        "aws_sdk_pinpoint.types.write_event_stream.WriteEventStream"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PutEventStreamRequest) -> dict:
    out: dict = {}
    if "write_event_stream" in value:
        import aws_sdk_pinpoint.types.write_event_stream

        out["WriteEventStream"] = (
            aws_sdk_pinpoint.types.write_event_stream.serialize_json(
                value["write_event_stream"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutEventStreamRequest:
    out: PutEventStreamRequest = {}  # type: ignore[typeddict-item]
    if "WriteEventStream" in data:
        import aws_sdk_pinpoint.types.write_event_stream

        out["write_event_stream"] = (
            aws_sdk_pinpoint.types.write_event_stream.deserialize_json(
                data["WriteEventStream"]
            )
        )
    return out
