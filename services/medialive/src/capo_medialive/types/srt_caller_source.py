"""Generated from Smithy shape ``com.amazonaws.medialive#SrtCallerSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer
    import capo_medialive.types.__string
    import capo_medialive.types.srt_caller_decryption


class SrtCallerSource(TypedDict, closed=True):
    decryption: NotRequired[
        "capo_medialive.types.srt_caller_decryption.SrtCallerDecryption"
    ]
    minimum_latency: NotRequired["capo_medialive.types.__integer.__integer"]
    """The preferred latency (in milliseconds) for implementing packet loss and recovery. Packet recovery is a key feature of SRT."""
    srt_listener_address: NotRequired["capo_medialive.types.__string.__string"]
    """The IP address at the upstream system (the listener) that MediaLive (the caller) connects to."""
    srt_listener_port: NotRequired["capo_medialive.types.__string.__string"]
    """The port at the upstream system (the listener) that MediaLive (the caller) connects to."""
    stream_id: NotRequired["capo_medialive.types.__string.__string"]
    """The stream ID, if the upstream system uses this identifier."""


# --- restJson1 ser/de ---
def serialize_json(value: SrtCallerSource) -> dict:
    out: dict = {}
    if "decryption" in value:
        import capo_medialive.types.srt_caller_decryption

        out["decryption"] = capo_medialive.types.srt_caller_decryption.serialize_json(
            value["decryption"]
        )
    if "minimum_latency" in value:
        out["minimumLatency"] = value["minimum_latency"]
    if "srt_listener_address" in value:
        out["srtListenerAddress"] = value["srt_listener_address"]
    if "srt_listener_port" in value:
        out["srtListenerPort"] = value["srt_listener_port"]
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    return out


def deserialize_json(data: dict) -> SrtCallerSource:
    out: SrtCallerSource = {}  # type: ignore[typeddict-item]
    if "decryption" in data:
        import capo_medialive.types.srt_caller_decryption

        out["decryption"] = capo_medialive.types.srt_caller_decryption.deserialize_json(
            data["decryption"]
        )
    if "minimumLatency" in data:
        out["minimum_latency"] = data["minimumLatency"]
    if "srtListenerAddress" in data:
        out["srt_listener_address"] = data["srtListenerAddress"]
    if "srtListenerPort" in data:
        out["srt_listener_port"] = data["srtListenerPort"]
    if "streamId" in data:
        out["stream_id"] = data["streamId"]
    return out
