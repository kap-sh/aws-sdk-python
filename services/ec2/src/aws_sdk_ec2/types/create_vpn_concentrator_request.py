"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpnConcentratorRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.transit_gateway_id
    import aws_sdk_ec2.types.vpn_concentrator_type


class CreateVpnConcentratorRequest(TypedDict):
    type: NotRequired["aws_sdk_ec2.types.vpn_concentrator_type.VpnConcentratorType"]
    """<p>The type of VPN concentrator to create.</p>"""
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway to attach the VPN concentrator to.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the VPN concentrator during creation.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpnConcentratorRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "type" in value:
        import aws_sdk_ec2.types.vpn_concentrator_type

        aws_sdk_ec2.types.vpn_concentrator_type.serialize_ec2_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateVpnConcentratorRequest:
    out: CreateVpnConcentratorRequest = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_ec2.types.vpn_concentrator_type

        out["type"] = aws_sdk_ec2.types.vpn_concentrator_type.deserialize_ec2_query(
            child_type
        )
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
