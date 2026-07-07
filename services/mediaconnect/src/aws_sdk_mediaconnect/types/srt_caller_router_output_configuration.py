"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SrtCallerRouterOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.srt_encryption_configuration


class SrtCallerRouterOutputConfiguration(TypedDict, closed=True):
    destination_address: "str"
    """<p>The destination IP address for the SRT protocol in caller mode.</p>"""
    destination_port: "int"
    """<p>The destination port number for the SRT protocol in caller mode.</p>"""
    minimum_latency_milliseconds: "int"
    """<p>The minimum latency in milliseconds for the SRT protocol in caller mode.</p>"""
    stream_id: NotRequired["str"]
    """<p>The stream ID for the SRT protocol in caller mode.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_mediaconnect.types.srt_encryption_configuration.SrtEncryptionConfiguration"
    ]
    """<p>Defines the encryption settings for an SRT caller output, including the encryption key configuration and associated parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SrtCallerRouterOutputConfiguration) -> dict:
    out: dict = {}
    out["destinationAddress"] = value["destination_address"]
    out["destinationPort"] = value["destination_port"]
    out["minimumLatencyMilliseconds"] = value["minimum_latency_milliseconds"]
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "encryption_configuration" in value:
        import aws_sdk_mediaconnect.types.srt_encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_mediaconnect.types.srt_encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SrtCallerRouterOutputConfiguration:
    out: SrtCallerRouterOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "destinationAddress" in data:
        out["destination_address"] = data["destinationAddress"]
    else:
        raise DeserializationError(
            "SrtCallerRouterOutputConfiguration.destination_address required"
        )
    if "destinationPort" in data:
        out["destination_port"] = data["destinationPort"]
    else:
        raise DeserializationError(
            "SrtCallerRouterOutputConfiguration.destination_port required"
        )
    if "minimumLatencyMilliseconds" in data:
        out["minimum_latency_milliseconds"] = data["minimumLatencyMilliseconds"]
    else:
        raise DeserializationError(
            "SrtCallerRouterOutputConfiguration.minimum_latency_milliseconds required"
        )
    if "streamId" in data:
        out["stream_id"] = data["streamId"]
    if "encryptionConfiguration" in data:
        import aws_sdk_mediaconnect.types.srt_encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_mediaconnect.types.srt_encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    return out
