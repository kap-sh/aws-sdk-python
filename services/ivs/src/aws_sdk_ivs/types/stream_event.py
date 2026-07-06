"""Generated from Smithy shape ``com.amazonaws.ivs#StreamEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs.types.string
    import aws_sdk_ivs.types.time


class StreamEvent(TypedDict, closed=True):
    name: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p>Name that identifies the stream event within a <code>type</code>.</p>"""
    type: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p>Logical group for certain events.</p>"""
    event_time: NotRequired["aws_sdk_ivs.types.time.Time"]
    """<p>Time when the event occurred. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>.</p>"""
    code: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p>Provides additional details about the stream event. There are several values; the long descriptions are provided in the IVS console but not delivered through the IVS API or EventBridge. Multitrack-related codes are used only for certain Session Ended events.</p> <ul> <li> <p> <code>MultitrackInputNotAllowed</code> — The broadcast client attempted to connect with multitrack input, but multitrack input was not enabled on the channel. Check your broadcast software settings or set <code>MultitrackInputConfiguration.Policy</code> to <code>ALLOW</code> or <code>REQUIRE</code>.</p> </li> <li> <p> <code>MultitrackInputRequired</code> — The broadcast client attempted to connect with single-track video, but multitrack input is required on this channel. Enable multitrack video in your broadcast software or configure the channel’s <code>MultitrackInputConfiguration.Policy</code> to <code>ALLOW</code>.</p> </li> <li> <p> <code>InvalidGetClientConfigurationStreamKey</code> — The broadcast client attempted to connect with an invalid, expired, or corrupt stream key.</p> </li> <li> <p> <code>GetClientConfigurationStreamKeyRequired</code> — The broadcast client attempted to stream multitrack video without providing an authenticated stream key from GetClientConfiguration.</p> </li> <li> <p> <code>InvalidMultitrackInputTrackCount</code> — The multitrack input stream contained an invalid number of tracks.</p> </li> <li> <p> <code>InvalidMultitrackInputVideoTrackMediaProperties</code> — The multitrack input stream contained one or more tracks with an invalid codec, resolution, bitrate, or framerate.</p> </li> <li> <p> <code>StreamTakeoverMediaMismatch</code> — The broadcast client attempted to take over with different media properties (e.g., codec, resolution, or video track type) from the original stream.</p> </li> <li> <p> <code>StreamTakeoverInvalidPriority</code> — The broadcast client attempted a takeover with either a priority integer value equal to or lower than the original stream's value or a value outside the allowed range of 1 to 2,147,483,647.</p> <p> <code>StreamTakeoverLimitBreached</code> — The broadcast client reached the maximum allowed takeover attempts for this stream.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamEvent) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "event_time" in value:
        import aws_sdk_ivs.types.time

        out["eventTime"] = aws_sdk_ivs.types.time.serialize_json(value["event_time"])
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> StreamEvent:
    out: StreamEvent = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        out["type"] = data["type"]
    if "eventTime" in data:
        import aws_sdk_ivs.types.time

        out["event_time"] = aws_sdk_ivs.types.time.deserialize_json(data["eventTime"])
    if "code" in data:
        out["code"] = data["code"]
    return out
