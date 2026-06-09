"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateSecurityGroupVpcRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.disassociate_security_group_vpc_security_group_id
    import aws_sdk_ec2.types.string


class DisassociateSecurityGroupVpcRequest(TypedDict):
    group_id: NotRequired[
        "aws_sdk_ec2.types.disassociate_security_group_vpc_security_group_id.DisassociateSecurityGroupVpcSecurityGroupId"
    ]
    """<p>A security group ID.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A VPC ID.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateSecurityGroupVpcRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "group_id" in value:
        pairs.append((f"{prefix}.GroupId", str(value["group_id"])))
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DisassociateSecurityGroupVpcRequest:
    out: DisassociateSecurityGroupVpcRequest = {}  # type: ignore[typeddict-item]
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
