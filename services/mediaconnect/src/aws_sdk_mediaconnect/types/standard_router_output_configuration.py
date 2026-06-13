"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StandardRouterOutputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_network_interface_arn
    import aws_sdk_mediaconnect.types.router_output_protocol
    import aws_sdk_mediaconnect.types.router_output_protocol_configuration


class StandardRouterOutputConfiguration(TypedDict):
    network_interface_arn: "aws_sdk_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    """<p>The Amazon Resource Name (ARN) of the network interface associated with the standard router output.</p>"""
    protocol_configuration: "aws_sdk_mediaconnect.types.router_output_protocol_configuration.RouterOutputProtocolConfiguration"
    """<p>The configuration settings for the protocol used by the standard router output.</p>"""
    protocol: NotRequired[
        "aws_sdk_mediaconnect.types.router_output_protocol.RouterOutputProtocol"
    ]
    """<p>The protocol used by the standard router output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardRouterOutputConfiguration) -> dict:
    out: dict = {}
    out["networkInterfaceArn"] = value["network_interface_arn"]
    import aws_sdk_mediaconnect.types.router_output_protocol_configuration

    out["protocolConfiguration"] = (
        aws_sdk_mediaconnect.types.router_output_protocol_configuration.serialize_json(
            value["protocol_configuration"]
        )
    )
    if "protocol" in value:
        import aws_sdk_mediaconnect.types.router_output_protocol

        out["protocol"] = (
            aws_sdk_mediaconnect.types.router_output_protocol.serialize_json(
                value["protocol"]
            )
        )
    return out


def deserialize_json(data: dict) -> StandardRouterOutputConfiguration:
    out: StandardRouterOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "networkInterfaceArn" in data:
        out["network_interface_arn"] = data["networkInterfaceArn"]
    else:
        raise DeserializationError(
            "StandardRouterOutputConfiguration.network_interface_arn required"
        )
    if "protocolConfiguration" in data:
        import aws_sdk_mediaconnect.types.router_output_protocol_configuration

        out["protocol_configuration"] = (
            aws_sdk_mediaconnect.types.router_output_protocol_configuration.deserialize_json(
                data["protocolConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "StandardRouterOutputConfiguration.protocol_configuration required"
        )
    if "protocol" in data:
        import aws_sdk_mediaconnect.types.router_output_protocol

        out["protocol"] = (
            aws_sdk_mediaconnect.types.router_output_protocol.deserialize_json(
                data["protocol"]
            )
        )
    return out
