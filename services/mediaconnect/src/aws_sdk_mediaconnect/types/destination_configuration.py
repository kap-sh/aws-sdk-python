"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.interface


class DestinationConfiguration(TypedDict, closed=True):
    destination_ip: NotRequired["str"]
    """<p>The IP address where you want MediaConnect to send contents of the media stream.</p>"""
    destination_port: NotRequired["int"]
    """<p> The port that you want MediaConnect to use when it distributes the media stream to the output.</p>"""
    interface: NotRequired["aws_sdk_mediaconnect.types.interface.Interface"]
    """<p> The VPC interface that you want to use for the media stream associated with the output.</p>"""
    outbound_ip: NotRequired["str"]
    """<p>The IP address that the receiver requires in order to establish a connection with the flow. This value is represented by the elastic network interface IP address of the VPC. This field applies only to outputs that use the CDI or ST 2110 JPEG XS or protocol. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationConfiguration) -> dict:
    out: dict = {}
    if "destination_ip" in value:
        out["destinationIp"] = value["destination_ip"]
    if "destination_port" in value:
        out["destinationPort"] = value["destination_port"]
    if "interface" in value:
        import aws_sdk_mediaconnect.types.interface

        out["interface"] = aws_sdk_mediaconnect.types.interface.serialize_json(
            value["interface"]
        )
    if "outbound_ip" in value:
        out["outboundIp"] = value["outbound_ip"]
    return out


def deserialize_json(data: dict) -> DestinationConfiguration:
    out: DestinationConfiguration = {}  # type: ignore[typeddict-item]
    if "destinationIp" in data:
        out["destination_ip"] = data["destinationIp"]
    if "destinationPort" in data:
        out["destination_port"] = data["destinationPort"]
    if "interface" in data:
        import aws_sdk_mediaconnect.types.interface

        out["interface"] = aws_sdk_mediaconnect.types.interface.deserialize_json(
            data["interface"]
        )
    if "outboundIp" in data:
        out["outbound_ip"] = data["outboundIp"]
    return out
