"""Generated from Smithy shape ``com.amazonaws.medialive#SrtListenerSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer
    import capo_medialive.types.__string
    import capo_medialive.types.srt_listener_decryption


class SrtListenerSettings(TypedDict, closed=True):
    decryption: NotRequired[
        "capo_medialive.types.srt_listener_decryption.SrtListenerDecryption"
    ]
    minimum_latency: NotRequired["capo_medialive.types.__integer.__integer"]
    """The preferred latency (in milliseconds) for implementing packet loss and recovery. Range 120-15000."""
    stream_id: NotRequired["capo_medialive.types.__string.__string"]
    """The stream ID, if the upstream system uses this identifier."""


# --- restJson1 ser/de ---
def serialize_json(value: SrtListenerSettings) -> dict:
    out: dict = {}
    if "decryption" in value:
        import capo_medialive.types.srt_listener_decryption

        out["decryption"] = capo_medialive.types.srt_listener_decryption.serialize_json(
            value["decryption"]
        )
    if "minimum_latency" in value:
        out["minimumLatency"] = value["minimum_latency"]
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    return out


def deserialize_json(data: dict) -> SrtListenerSettings:
    out: SrtListenerSettings = {}  # type: ignore[typeddict-item]
    if "decryption" in data:
        import capo_medialive.types.srt_listener_decryption

        out["decryption"] = (
            capo_medialive.types.srt_listener_decryption.deserialize_json(
                data["decryption"]
            )
        )
    if "minimumLatency" in data:
        out["minimum_latency"] = data["minimumLatency"]
    if "streamId" in data:
        out["stream_id"] = data["streamId"]
    return out
