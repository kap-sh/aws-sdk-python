"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StandardRouterInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_protocol
    import aws_sdk_mediaconnect.types.router_input_protocol_configuration
    import aws_sdk_mediaconnect.types.router_network_interface_arn


class StandardRouterInputConfiguration(TypedDict, closed=True):
    network_interface_arn: "aws_sdk_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    """<p>The Amazon Resource Name (ARN) of the network interface associated with the standard router input.</p>"""
    protocol_configuration: "aws_sdk_mediaconnect.types.router_input_protocol_configuration.RouterInputProtocolConfiguration"
    """<p>The configuration settings for the protocol used by the standard router input.</p>"""
    protocol: NotRequired[
        "aws_sdk_mediaconnect.types.router_input_protocol.RouterInputProtocol"
    ]
    """<p>The protocol used by the standard router input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardRouterInputConfiguration) -> dict:
    out: dict = {}
    out["networkInterfaceArn"] = value["network_interface_arn"]
    import aws_sdk_mediaconnect.types.router_input_protocol_configuration

    out["protocolConfiguration"] = (
        aws_sdk_mediaconnect.types.router_input_protocol_configuration.serialize_json(
            value["protocol_configuration"]
        )
    )
    if "protocol" in value:
        import aws_sdk_mediaconnect.types.router_input_protocol

        out["protocol"] = (
            aws_sdk_mediaconnect.types.router_input_protocol.serialize_json(
                value["protocol"]
            )
        )
    return out


def deserialize_json(data: dict) -> StandardRouterInputConfiguration:
    out: StandardRouterInputConfiguration = {}  # type: ignore[typeddict-item]
    if "networkInterfaceArn" in data:
        out["network_interface_arn"] = data["networkInterfaceArn"]
    else:
        raise DeserializationError(
            "StandardRouterInputConfiguration.network_interface_arn required"
        )
    if "protocolConfiguration" in data:
        import aws_sdk_mediaconnect.types.router_input_protocol_configuration

        out["protocol_configuration"] = (
            aws_sdk_mediaconnect.types.router_input_protocol_configuration.deserialize_json(
                data["protocolConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "StandardRouterInputConfiguration.protocol_configuration required"
        )
    if "protocol" in data:
        import aws_sdk_mediaconnect.types.router_input_protocol

        out["protocol"] = (
            aws_sdk_mediaconnect.types.router_input_protocol.deserialize_json(
                data["protocol"]
            )
        )
    return out
