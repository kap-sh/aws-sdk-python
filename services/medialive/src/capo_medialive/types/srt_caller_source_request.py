"""Generated from Smithy shape ``com.amazonaws.medialive#SrtCallerSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer
    import capo_medialive.types.__string
    import capo_medialive.types.srt_caller_decryption_request


class SrtCallerSourceRequest(TypedDict, closed=True):
    decryption: NotRequired[
        "capo_medialive.types.srt_caller_decryption_request.SrtCallerDecryptionRequest"
    ]
    minimum_latency: NotRequired["capo_medialive.types.__integer.__integer"]
    """The preferred latency (in milliseconds) for implementing packet loss and recovery. Packet recovery is a key feature of SRT. Obtain this value from the operator at the upstream system."""
    srt_listener_address: NotRequired["capo_medialive.types.__string.__string"]
    """The IP address at the upstream system (the listener) that MediaLive (the caller) will connect to."""
    srt_listener_port: NotRequired["capo_medialive.types.__string.__string"]
    """The port at the upstream system (the listener) that MediaLive (the caller) will connect to."""
    stream_id: NotRequired["capo_medialive.types.__string.__string"]
    """This value is required if the upstream system uses this identifier because without it, the SRT handshake between MediaLive (the caller) and the upstream system (the listener) might fail."""


# --- restJson1 ser/de ---
def serialize_json(value: SrtCallerSourceRequest) -> dict:
    out: dict = {}
    if "decryption" in value:
        import capo_medialive.types.srt_caller_decryption_request

        out["decryption"] = (
            capo_medialive.types.srt_caller_decryption_request.serialize_json(
                value["decryption"]
            )
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


def deserialize_json(data: dict) -> SrtCallerSourceRequest:
    out: SrtCallerSourceRequest = {}  # type: ignore[typeddict-item]
    if "decryption" in data:
        import capo_medialive.types.srt_caller_decryption_request

        out["decryption"] = (
            capo_medialive.types.srt_caller_decryption_request.deserialize_json(
                data["decryption"]
            )
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
