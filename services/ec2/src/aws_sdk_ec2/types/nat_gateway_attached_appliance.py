"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayAttachedAppliance``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.nat_gateway_appliance_modify_state
    import aws_sdk_ec2.types.nat_gateway_appliance_state
    import aws_sdk_ec2.types.nat_gateway_appliance_type
    import aws_sdk_ec2.types.string


class NatGatewayAttachedAppliance(TypedDict):
    type: NotRequired[
        "aws_sdk_ec2.types.nat_gateway_appliance_type.NatGatewayApplianceType"
    ]
    """<p>The type of appliance attached to the NAT Gateway. For network firewall proxy functionality, this will be \"network-firewall-proxy\".</p>"""
    appliance_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the attached appliance, identifying the specific proxy or security appliance resource.</p>"""
    vpc_endpoint_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The VPC endpoint ID used to route traffic from application VPCs to the proxy for inspection and filtering.</p>"""
    attachment_state: NotRequired[
        "aws_sdk_ec2.types.nat_gateway_appliance_state.NatGatewayApplianceState"
    ]
    """<p>The current attachment state of the appliance.</p>"""
    modification_state: NotRequired[
        "aws_sdk_ec2.types.nat_gateway_appliance_modify_state.NatGatewayApplianceModifyState"
    ]
    """<p>The current modification state of the appliance.</p>"""
    failure_code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The failure code if the appliance attachment or modification operation failed.</p>"""
    failure_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A descriptive message explaining the failure if the appliance attachment or modification operation failed.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NatGatewayAttachedAppliance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "type" in value:
        import aws_sdk_ec2.types.nat_gateway_appliance_type

        aws_sdk_ec2.types.nat_gateway_appliance_type.serialize_ec2_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "appliance_arn" in value:
        pairs.append((f"{prefix}.ApplianceArn", str(value["appliance_arn"])))
    if "vpc_endpoint_id" in value:
        pairs.append((f"{prefix}.VpcEndpointId", str(value["vpc_endpoint_id"])))
    if "attachment_state" in value:
        import aws_sdk_ec2.types.nat_gateway_appliance_state

        aws_sdk_ec2.types.nat_gateway_appliance_state.serialize_ec2_query(
            value["attachment_state"], pairs, f"{prefix}.AttachmentState"
        )
    if "modification_state" in value:
        import aws_sdk_ec2.types.nat_gateway_appliance_modify_state

        aws_sdk_ec2.types.nat_gateway_appliance_modify_state.serialize_ec2_query(
            value["modification_state"], pairs, f"{prefix}.ModificationState"
        )
    if "failure_code" in value:
        pairs.append((f"{prefix}.FailureCode", str(value["failure_code"])))
    if "failure_message" in value:
        pairs.append((f"{prefix}.FailureMessage", str(value["failure_message"])))


def deserialize_ec2_query(el: Element) -> NatGatewayAttachedAppliance:
    out: NatGatewayAttachedAppliance = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_ec2.types.nat_gateway_appliance_type

        out["type"] = (
            aws_sdk_ec2.types.nat_gateway_appliance_type.deserialize_ec2_query(
                child_type
            )
        )
    child_appliance_arn = el.find("ApplianceArn")
    if child_appliance_arn is not None:
        out["appliance_arn"] = str(child_appliance_arn.text or "")
    child_vpc_endpoint_id = el.find("VpcEndpointId")
    if child_vpc_endpoint_id is not None:
        out["vpc_endpoint_id"] = str(child_vpc_endpoint_id.text or "")
    child_attachment_state = el.find("AttachmentState")
    if child_attachment_state is not None:
        import aws_sdk_ec2.types.nat_gateway_appliance_state

        out["attachment_state"] = (
            aws_sdk_ec2.types.nat_gateway_appliance_state.deserialize_ec2_query(
                child_attachment_state
            )
        )
    child_modification_state = el.find("ModificationState")
    if child_modification_state is not None:
        import aws_sdk_ec2.types.nat_gateway_appliance_modify_state

        out["modification_state"] = (
            aws_sdk_ec2.types.nat_gateway_appliance_modify_state.deserialize_ec2_query(
                child_modification_state
            )
        )
    child_failure_code = el.find("FailureCode")
    if child_failure_code is not None:
        out["failure_code"] = str(child_failure_code.text or "")
    child_failure_message = el.find("FailureMessage")
    if child_failure_message is not None:
        out["failure_message"] = str(child_failure_message.text or "")
    return out
