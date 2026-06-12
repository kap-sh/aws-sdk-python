"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingDestinationDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.port_number
    import aws_sdk_global_accelerator.types.protocols


class CustomRoutingDestinationDescription(TypedDict):
    from_port: NotRequired["aws_sdk_global_accelerator.types.port_number.PortNumber"]
    """<p>The first port, inclusive, in the range of ports for the endpoint group that is associated with a custom routing accelerator.</p>"""
    to_port: NotRequired["aws_sdk_global_accelerator.types.port_number.PortNumber"]
    """<p>The last port, inclusive, in the range of ports for the endpoint group that is associated with a custom routing accelerator.</p>"""
    protocols: NotRequired["aws_sdk_global_accelerator.types.protocols.Protocols"]
    """<p>The protocol for the endpoint group that is associated with a custom routing accelerator. The protocol can be either TCP or UDP.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingDestinationDescription) -> dict:
    out: dict = {}
    if "from_port" in value:
        out["FromPort"] = value["from_port"]
    if "to_port" in value:
        out["ToPort"] = value["to_port"]
    if "protocols" in value:
        import aws_sdk_global_accelerator.types.protocols

        out["Protocols"] = (
            aws_sdk_global_accelerator.types.protocols.serialize_aws_json_1_1(
                value["protocols"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomRoutingDestinationDescription:
    out: CustomRoutingDestinationDescription = {}  # type: ignore[typeddict-item]
    if "FromPort" in data:
        out["from_port"] = data["FromPort"]
    if "ToPort" in data:
        out["to_port"] = data["ToPort"]
    if "Protocols" in data:
        import aws_sdk_global_accelerator.types.protocols

        out["protocols"] = (
            aws_sdk_global_accelerator.types.protocols.deserialize_aws_json_1_1(
                data["Protocols"]
            )
        )
    return out
