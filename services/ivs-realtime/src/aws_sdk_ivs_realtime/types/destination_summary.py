"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DestinationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.destination_state
    import aws_sdk_ivs_realtime.types.string
    import aws_sdk_ivs_realtime.types.time


class DestinationSummary(TypedDict, closed=True):
    id: "aws_sdk_ivs_realtime.types.string.String"
    """<p>Unique identifier for this destination, assigned by IVS.</p>"""
    state: "aws_sdk_ivs_realtime.types.destination_state.DestinationState"
    """<p>State of the Composition Destination.</p>"""
    start_time: NotRequired["aws_sdk_ivs_realtime.types.time.Time"]
    """<p>UTC time of the destination start. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>.</p>"""
    end_time: NotRequired["aws_sdk_ivs_realtime.types.time.Time"]
    """<p>UTC time of the destination end. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["state"] = value["state"]
    if "start_time" in value:
        import aws_sdk_ivs_realtime.types.time

        out["startTime"] = aws_sdk_ivs_realtime.types.time.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_ivs_realtime.types.time

        out["endTime"] = aws_sdk_ivs_realtime.types.time.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> DestinationSummary:
    out: DestinationSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DestinationSummary.id required")
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("DestinationSummary.state required")
    if "startTime" in data:
        import aws_sdk_ivs_realtime.types.time

        out["start_time"] = aws_sdk_ivs_realtime.types.time.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_ivs_realtime.types.time

        out["end_time"] = aws_sdk_ivs_realtime.types.time.deserialize_json(
            data["endTime"]
        )
    return out
