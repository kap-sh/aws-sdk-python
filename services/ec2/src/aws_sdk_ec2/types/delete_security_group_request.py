"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteSecurityGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.security_group_id
    import aws_sdk_ec2.types.security_group_name


class DeleteSecurityGroupRequest(TypedDict):
    group_id: NotRequired["aws_sdk_ec2.types.security_group_id.SecurityGroupId"]
    """<p>The ID of the security group.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.security_group_name.SecurityGroupName"]
    """<p>[Default VPC] The name of the security group. You can specify either the security group name or the security group ID. For security groups in a nondefault VPC, you must specify the security group ID.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteSecurityGroupRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "group_id" in value:
        pairs.append((f"{prefix}.GroupId", str(value["group_id"])))
    if "group_name" in value:
        pairs.append((f"{prefix}.GroupName", str(value["group_name"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteSecurityGroupRequest:
    out: DeleteSecurityGroupRequest = {}  # type: ignore[typeddict-item]
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
