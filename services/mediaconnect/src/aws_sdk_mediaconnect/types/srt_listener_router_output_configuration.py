"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SrtListenerRouterOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.srt_encryption_configuration


class SrtListenerRouterOutputConfiguration(TypedDict, closed=True):
    port: "int"
    """<p>The port number for the SRT protocol in listener mode.</p>"""
    minimum_latency_milliseconds: "int"
    """<p>The minimum latency in milliseconds for the SRT protocol in listener mode.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_mediaconnect.types.srt_encryption_configuration.SrtEncryptionConfiguration"
    ]
    """<p>Defines the encryption settings for an SRT listener output, including the encryption key configuration and associated parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SrtListenerRouterOutputConfiguration) -> dict:
    out: dict = {}
    out["port"] = value["port"]
    out["minimumLatencyMilliseconds"] = value["minimum_latency_milliseconds"]
    if "encryption_configuration" in value:
        import aws_sdk_mediaconnect.types.srt_encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_mediaconnect.types.srt_encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SrtListenerRouterOutputConfiguration:
    out: SrtListenerRouterOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "port" in data:
        out["port"] = data["port"]
    else:
        raise DeserializationError("SrtListenerRouterOutputConfiguration.port required")
    if "minimumLatencyMilliseconds" in data:
        out["minimum_latency_milliseconds"] = data["minimumLatencyMilliseconds"]
    else:
        raise DeserializationError(
            "SrtListenerRouterOutputConfiguration.minimum_latency_milliseconds required"
        )
    if "encryptionConfiguration" in data:
        import aws_sdk_mediaconnect.types.srt_encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_mediaconnect.types.srt_encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    return out
