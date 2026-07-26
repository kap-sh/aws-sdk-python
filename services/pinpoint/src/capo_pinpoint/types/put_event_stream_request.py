"""Generated from Smithy shape ``com.amazonaws.pinpoint#PutEventStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.write_event_stream


class PutEventStreamRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    write_event_stream: NotRequired[
        "capo_pinpoint.types.write_event_stream.WriteEventStream"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PutEventStreamRequest) -> dict:
    out: dict = {}
    if "write_event_stream" in value:
        import capo_pinpoint.types.write_event_stream

        out["WriteEventStream"] = capo_pinpoint.types.write_event_stream.serialize_json(
            value["write_event_stream"]
        )
    return out


def deserialize_json(data: dict) -> PutEventStreamRequest:
    out: PutEventStreamRequest = {}  # type: ignore[typeddict-item]
    if "WriteEventStream" in data:
        import capo_pinpoint.types.write_event_stream

        out["write_event_stream"] = (
            capo_pinpoint.types.write_event_stream.deserialize_json(
                data["WriteEventStream"]
            )
        )
    return out
