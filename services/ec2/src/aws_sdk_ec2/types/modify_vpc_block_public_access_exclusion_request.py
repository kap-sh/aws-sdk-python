"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcBlockPublicAccessExclusionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.internet_gateway_exclusion_mode
    import aws_sdk_ec2.types.vpc_block_public_access_exclusion_id


class ModifyVpcBlockPublicAccessExclusionRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    exclusion_id: NotRequired[
        "aws_sdk_ec2.types.vpc_block_public_access_exclusion_id.VpcBlockPublicAccessExclusionId"
    ]
    """<p>The ID of an exclusion.</p>"""
    internet_gateway_exclusion_mode: NotRequired[
        "aws_sdk_ec2.types.internet_gateway_exclusion_mode.InternetGatewayExclusionMode"
    ]
    """<p>The exclusion mode for internet gateway traffic.</p> <ul> <li> <p> <code>allow-bidirectional</code>: Allow all internet traffic to and from the excluded VPCs and subnets.</p> </li> <li> <p> <code>allow-egress</code>: Allow outbound internet traffic from the excluded VPCs and subnets. Block inbound internet traffic to the excluded VPCs and subnets. Only applies when VPC Block Public Access is set to Bidirectional.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcBlockPublicAccessExclusionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "exclusion_id" in value:
        pairs.append((f"{prefix}.ExclusionId", str(value["exclusion_id"])))
    if "internet_gateway_exclusion_mode" in value:
        import aws_sdk_ec2.types.internet_gateway_exclusion_mode

        aws_sdk_ec2.types.internet_gateway_exclusion_mode.serialize_ec2_query(
            value["internet_gateway_exclusion_mode"],
            pairs,
            f"{prefix}.InternetGatewayExclusionMode",
        )


def deserialize_ec2_query(el: Element) -> ModifyVpcBlockPublicAccessExclusionRequest:
    out: ModifyVpcBlockPublicAccessExclusionRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_exclusion_id = el.find("ExclusionId")
    if child_exclusion_id is not None:
        out["exclusion_id"] = str(child_exclusion_id.text or "")
    child_internet_gateway_exclusion_mode = el.find("InternetGatewayExclusionMode")
    if child_internet_gateway_exclusion_mode is not None:
        import aws_sdk_ec2.types.internet_gateway_exclusion_mode

        out["internet_gateway_exclusion_mode"] = (
            aws_sdk_ec2.types.internet_gateway_exclusion_mode.deserialize_ec2_query(
                child_internet_gateway_exclusion_mode
            )
        )
    return out
