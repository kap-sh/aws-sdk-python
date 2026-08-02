"""Generated from Smithy shape ``com.amazonaws.ec2#AttachClassicLinkVpcRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.group_id_string_list
    import capo_ec2.types.instance_id
    import capo_ec2.types.vpc_id


class AttachClassicLinkVpcRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the EC2-Classic instance.</p>"""
    vpc_id: NotRequired["capo_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the ClassicLink-enabled VPC.</p>"""
    groups: NotRequired["capo_ec2.types.group_id_string_list.GroupIdStringList"]
    """<p>The IDs of the security groups. You cannot specify security groups from a different VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AttachClassicLinkVpcRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "groups" in value:
        import capo_ec2.types.group_id_string_list

        capo_ec2.types.group_id_string_list.serialize_ec2_query(
            value["groups"], pairs, f"{key_prefix}Groups"
        )


def deserialize_ec2_query(el: Element) -> AttachClassicLinkVpcRequest:
    out: AttachClassicLinkVpcRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    if el.find("Groups") is not None:
        import capo_ec2.types.group_id_string_list

        out["groups"] = capo_ec2.types.group_id_string_list.deserialize_ec2_query(
            el, "Groups"
        )
    return out
