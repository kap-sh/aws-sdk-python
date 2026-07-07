"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.interface_request


class DestinationConfigurationRequest(TypedDict, closed=True):
    destination_ip: NotRequired["str"]
    """<p>The IP address where you want MediaConnect to send contents of the media stream.</p>"""
    destination_port: NotRequired["int"]
    """<p> The port that you want MediaConnect to use when it distributes the media stream to the output.</p>"""
    interface: NotRequired[
        "aws_sdk_mediaconnect.types.interface_request.InterfaceRequest"
    ]
    """<p> The VPC interface that you want to use for the media stream associated with the output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationConfigurationRequest) -> dict:
    out: dict = {}
    if "destination_ip" in value:
        out["destinationIp"] = value["destination_ip"]
    if "destination_port" in value:
        out["destinationPort"] = value["destination_port"]
    if "interface" in value:
        import aws_sdk_mediaconnect.types.interface_request

        out["interface"] = aws_sdk_mediaconnect.types.interface_request.serialize_json(
            value["interface"]
        )
    return out


def deserialize_json(data: dict) -> DestinationConfigurationRequest:
    out: DestinationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "destinationIp" in data:
        out["destination_ip"] = data["destinationIp"]
    if "destinationPort" in data:
        out["destination_port"] = data["destinationPort"]
    if "interface" in data:
        import aws_sdk_mediaconnect.types.interface_request

        out["interface"] = (
            aws_sdk_mediaconnect.types.interface_request.deserialize_json(
                data["interface"]
            )
        )
    return out
