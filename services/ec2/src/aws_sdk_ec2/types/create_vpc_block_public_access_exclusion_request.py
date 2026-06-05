"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcBlockPublicAccessExclusionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.internet_gateway_exclusion_mode
    import aws_sdk_ec2.types.subnet_id
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.vpc_id


class CreateVpcBlockPublicAccessExclusionRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>A subnet ID.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>A VPC ID.</p>"""
    internet_gateway_exclusion_mode: NotRequired[
        "aws_sdk_ec2.types.internet_gateway_exclusion_mode.InternetGatewayExclusionMode"
    ]
    """<p>The exclusion mode for internet gateway traffic.</p> <ul> <li> <p> <code>allow-bidirectional</code>: Allow all internet traffic to and from the excluded VPCs and subnets.</p> </li> <li> <p> <code>allow-egress</code>: Allow outbound internet traffic from the excluded VPCs and subnets. Block inbound internet traffic to the excluded VPCs and subnets. Only applies when VPC Block Public Access is set to Bidirectional.</p> </li> </ul>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p> <code>tag</code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpcBlockPublicAccessExclusionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "internet_gateway_exclusion_mode" in value:
        import aws_sdk_ec2.types.internet_gateway_exclusion_mode

        aws_sdk_ec2.types.internet_gateway_exclusion_mode.serialize_ec2_query(
            value["internet_gateway_exclusion_mode"],
            pairs,
            f"{prefix}.InternetGatewayExclusionMode",
        )
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )


def deserialize_ec2_query(el: Element) -> CreateVpcBlockPublicAccessExclusionRequest:
    out: CreateVpcBlockPublicAccessExclusionRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_internet_gateway_exclusion_mode = el.find("InternetGatewayExclusionMode")
    if child_internet_gateway_exclusion_mode is not None:
        import aws_sdk_ec2.types.internet_gateway_exclusion_mode

        out["internet_gateway_exclusion_mode"] = (
            aws_sdk_ec2.types.internet_gateway_exclusion_mode.deserialize_ec2_query(
                child_internet_gateway_exclusion_mode
            )
        )
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    return out
