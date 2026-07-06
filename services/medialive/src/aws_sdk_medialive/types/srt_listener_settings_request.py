"""Generated from Smithy shape ``com.amazonaws.medialive#SrtListenerSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.srt_listener_decryption_request


class SrtListenerSettingsRequest(TypedDict, closed=True):
    decryption: NotRequired[
        "aws_sdk_medialive.types.srt_listener_decryption_request.SrtListenerDecryptionRequest"
    ]
    minimum_latency: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """Required. The preferred latency in milliseconds for packet loss and recovery. Range 120-15000."""
    stream_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Optional. The stream ID if the upstream system uses this identifier."""


# --- restJson1 ser/de ---
def serialize_json(value: SrtListenerSettingsRequest) -> dict:
    out: dict = {}
    if "decryption" in value:
        import aws_sdk_medialive.types.srt_listener_decryption_request

        out["decryption"] = (
            aws_sdk_medialive.types.srt_listener_decryption_request.serialize_json(
                value["decryption"]
            )
        )
    if "minimum_latency" in value:
        out["minimumLatency"] = value["minimum_latency"]
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    return out


def deserialize_json(data: dict) -> SrtListenerSettingsRequest:
    out: SrtListenerSettingsRequest = {}  # type: ignore[typeddict-item]
    if "decryption" in data:
        import aws_sdk_medialive.types.srt_listener_decryption_request

        out["decryption"] = (
            aws_sdk_medialive.types.srt_listener_decryption_request.deserialize_json(
                data["decryption"]
            )
        )
    if "minimumLatency" in data:
        out["minimum_latency"] = data["minimumLatency"]
    if "streamId" in data:
        out["stream_id"] = data["streamId"]
    return out
