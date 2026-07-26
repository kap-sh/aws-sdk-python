"""Generated from Smithy shape ``com.amazonaws.medialive#RtmpOutputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0
    import capo_medialive.types.__integer_min1
    import capo_medialive.types.output_location_ref
    import capo_medialive.types.rtmp_output_certificate_mode


class RtmpOutputSettings(TypedDict, closed=True):
    certificate_mode: NotRequired[
        "capo_medialive.types.rtmp_output_certificate_mode.RtmpOutputCertificateMode"
    ]
    """If set to verifyAuthenticity, verify the tls certificate chain to a trusted Certificate Authority (CA). This will cause rtmps outputs with self-signed certificates to fail."""
    connection_retry_interval: NotRequired[
        "capo_medialive.types.__integer_min1.__integerMin1"
    ]
    """Number of seconds to wait before retrying a connection to the Flash Media server if the connection is lost."""
    destination: NotRequired[
        "capo_medialive.types.output_location_ref.OutputLocationRef"
    ]
    """The RTMP endpoint excluding the stream name (eg. rtmp://host/appname). For connection to Akamai, a username and password must be supplied. URI fields accept format identifiers."""
    num_retries: NotRequired["capo_medialive.types.__integer_min0.__integerMin0"]
    """Number of retry attempts."""


# --- restJson1 ser/de ---
def serialize_json(value: RtmpOutputSettings) -> dict:
    out: dict = {}
    if "certificate_mode" in value:
        import capo_medialive.types.rtmp_output_certificate_mode

        out["certificateMode"] = (
            capo_medialive.types.rtmp_output_certificate_mode.serialize_json(
                value["certificate_mode"]
            )
        )
    if "connection_retry_interval" in value:
        out["connectionRetryInterval"] = value["connection_retry_interval"]
    if "destination" in value:
        import capo_medialive.types.output_location_ref

        out["destination"] = capo_medialive.types.output_location_ref.serialize_json(
            value["destination"]
        )
    if "num_retries" in value:
        out["numRetries"] = value["num_retries"]
    return out


def deserialize_json(data: dict) -> RtmpOutputSettings:
    out: RtmpOutputSettings = {}  # type: ignore[typeddict-item]
    if "certificateMode" in data:
        import capo_medialive.types.rtmp_output_certificate_mode

        out["certificate_mode"] = (
            capo_medialive.types.rtmp_output_certificate_mode.deserialize_json(
                data["certificateMode"]
            )
        )
    if "connectionRetryInterval" in data:
        out["connection_retry_interval"] = data["connectionRetryInterval"]
    if "destination" in data:
        import capo_medialive.types.output_location_ref

        out["destination"] = capo_medialive.types.output_location_ref.deserialize_json(
            data["destination"]
        )
    if "numRetries" in data:
        out["num_retries"] = data["numRetries"]
    return out
