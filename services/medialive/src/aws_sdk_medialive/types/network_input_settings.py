"""Generated from Smithy shape ``com.amazonaws.medialive#NetworkInputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.hls_input_settings
    import aws_sdk_medialive.types.multicast_input_settings
    import aws_sdk_medialive.types.network_input_server_validation


class NetworkInputSettings(TypedDict, closed=True):
    hls_input_settings: NotRequired[
        "aws_sdk_medialive.types.hls_input_settings.HlsInputSettings"
    ]
    """Specifies HLS input settings when the uri is for a HLS manifest."""
    server_validation: NotRequired[
        "aws_sdk_medialive.types.network_input_server_validation.NetworkInputServerValidation"
    ]
    """Check HTTPS server certificates. When set to checkCryptographyOnly, cryptography in the certificate will be checked, but not the server's name. Certain subdomains (notably S3 buckets that use dots in the bucket name) do not strictly match the corresponding certificate's wildcard pattern and would otherwise cause the event to error. This setting is ignored for protocols that do not use https."""
    multicast_input_settings: NotRequired[
        "aws_sdk_medialive.types.multicast_input_settings.MulticastInputSettings"
    ]
    """Specifies multicast input settings when the uri is for a multicast event."""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInputSettings) -> dict:
    out: dict = {}
    if "hls_input_settings" in value:
        import aws_sdk_medialive.types.hls_input_settings

        out["hlsInputSettings"] = (
            aws_sdk_medialive.types.hls_input_settings.serialize_json(
                value["hls_input_settings"]
            )
        )
    if "server_validation" in value:
        import aws_sdk_medialive.types.network_input_server_validation

        out["serverValidation"] = (
            aws_sdk_medialive.types.network_input_server_validation.serialize_json(
                value["server_validation"]
            )
        )
    if "multicast_input_settings" in value:
        import aws_sdk_medialive.types.multicast_input_settings

        out["multicastInputSettings"] = (
            aws_sdk_medialive.types.multicast_input_settings.serialize_json(
                value["multicast_input_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkInputSettings:
    out: NetworkInputSettings = {}  # type: ignore[typeddict-item]
    if "hlsInputSettings" in data:
        import aws_sdk_medialive.types.hls_input_settings

        out["hls_input_settings"] = (
            aws_sdk_medialive.types.hls_input_settings.deserialize_json(
                data["hlsInputSettings"]
            )
        )
    if "serverValidation" in data:
        import aws_sdk_medialive.types.network_input_server_validation

        out["server_validation"] = (
            aws_sdk_medialive.types.network_input_server_validation.deserialize_json(
                data["serverValidation"]
            )
        )
    if "multicastInputSettings" in data:
        import aws_sdk_medialive.types.multicast_input_settings

        out["multicast_input_settings"] = (
            aws_sdk_medialive.types.multicast_input_settings.deserialize_json(
                data["multicastInputSettings"]
            )
        )
    return out
