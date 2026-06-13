"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SrtListenerRouterInputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.srt_decryption_configuration


class SrtListenerRouterInputConfiguration(TypedDict):
    port: "int"
    """<p>The port number for the SRT protocol in listener mode.</p>"""
    minimum_latency_milliseconds: "int"
    """<p>The minimum latency in milliseconds for the SRT protocol in listener mode.</p>"""
    decryption_configuration: NotRequired[
        "aws_sdk_mediaconnect.types.srt_decryption_configuration.SrtDecryptionConfiguration"
    ]
    """<p>Specifies the decryption settings for an SRT listener input, including the encryption key configuration and associated parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SrtListenerRouterInputConfiguration) -> dict:
    out: dict = {}
    out["port"] = value["port"]
    out["minimumLatencyMilliseconds"] = value["minimum_latency_milliseconds"]
    if "decryption_configuration" in value:
        import aws_sdk_mediaconnect.types.srt_decryption_configuration

        out["decryptionConfiguration"] = (
            aws_sdk_mediaconnect.types.srt_decryption_configuration.serialize_json(
                value["decryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SrtListenerRouterInputConfiguration:
    out: SrtListenerRouterInputConfiguration = {}  # type: ignore[typeddict-item]
    if "port" in data:
        out["port"] = data["port"]
    else:
        raise DeserializationError("SrtListenerRouterInputConfiguration.port required")
    if "minimumLatencyMilliseconds" in data:
        out["minimum_latency_milliseconds"] = data["minimumLatencyMilliseconds"]
    else:
        raise DeserializationError(
            "SrtListenerRouterInputConfiguration.minimum_latency_milliseconds required"
        )
    if "decryptionConfiguration" in data:
        import aws_sdk_mediaconnect.types.srt_decryption_configuration

        out["decryption_configuration"] = (
            aws_sdk_mediaconnect.types.srt_decryption_configuration.deserialize_json(
                data["decryptionConfiguration"]
            )
        )
    return out
