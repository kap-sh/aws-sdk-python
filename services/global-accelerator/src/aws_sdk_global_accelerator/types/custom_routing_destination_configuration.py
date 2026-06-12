"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingDestinationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.custom_routing_protocols
    import aws_sdk_global_accelerator.types.port_number


class CustomRoutingDestinationConfiguration(TypedDict):
    from_port: "aws_sdk_global_accelerator.types.port_number.PortNumber"
    """<p>The first port, inclusive, in the range of ports for the endpoint group that is associated with a custom routing accelerator.</p>"""
    to_port: "aws_sdk_global_accelerator.types.port_number.PortNumber"
    """<p>The last port, inclusive, in the range of ports for the endpoint group that is associated with a custom routing accelerator.</p>"""
    protocols: "aws_sdk_global_accelerator.types.custom_routing_protocols.CustomRoutingProtocols"
    """<p>The protocol for the endpoint group that is associated with a custom routing accelerator. The protocol can be either TCP or UDP.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingDestinationConfiguration) -> dict:
    out: dict = {}
    out["FromPort"] = value["from_port"]
    out["ToPort"] = value["to_port"]
    import aws_sdk_global_accelerator.types.custom_routing_protocols

    out["Protocols"] = (
        aws_sdk_global_accelerator.types.custom_routing_protocols.serialize_aws_json_1_1(
            value["protocols"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomRoutingDestinationConfiguration:
    out: CustomRoutingDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if "FromPort" in data:
        out["from_port"] = data["FromPort"]
    else:
        raise DeserializationError(
            "CustomRoutingDestinationConfiguration.from_port required"
        )
    if "ToPort" in data:
        out["to_port"] = data["ToPort"]
    else:
        raise DeserializationError(
            "CustomRoutingDestinationConfiguration.to_port required"
        )
    if "Protocols" in data:
        import aws_sdk_global_accelerator.types.custom_routing_protocols

        out["protocols"] = (
            aws_sdk_global_accelerator.types.custom_routing_protocols.deserialize_aws_json_1_1(
                data["Protocols"]
            )
        )
    else:
        raise DeserializationError(
            "CustomRoutingDestinationConfiguration.protocols required"
        )
    return out
