"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_id
    import aws_sdk_ec2.types.ipam_policy_id
    import aws_sdk_ec2.types.ipam_policy_state
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class IpamPolicy(TypedDict):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The account ID that owns the IPAM policy.</p>"""
    ipam_policy_id: NotRequired["aws_sdk_ec2.types.ipam_policy_id.IpamPolicyId"]
    """<p>The ID of the IPAM policy.</p>"""
    ipam_policy_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the IPAM policy.</p>"""
    ipam_policy_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region of the IPAM policy.</p>"""
    state: NotRequired["aws_sdk_ec2.types.ipam_policy_state.IpamPolicyState"]
    """<p>The state of the IPAM policy.</p>"""
    state_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message about the state of the IPAM policy.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the IPAM policy.</p>"""
    ipam_id: NotRequired["aws_sdk_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM this policy belongs to.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "ipam_policy_id" in value:
        pairs.append((f"{prefix}.IpamPolicyId", str(value["ipam_policy_id"])))
    if "ipam_policy_arn" in value:
        pairs.append((f"{prefix}.IpamPolicyArn", str(value["ipam_policy_arn"])))
    if "ipam_policy_region" in value:
        pairs.append((f"{prefix}.IpamPolicyRegion", str(value["ipam_policy_region"])))
    if "state" in value:
        import aws_sdk_ec2.types.ipam_policy_state

        aws_sdk_ec2.types.ipam_policy_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "state_message" in value:
        pairs.append((f"{prefix}.StateMessage", str(value["state_message"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "ipam_id" in value:
        pairs.append((f"{prefix}.IpamId", str(value["ipam_id"])))


def deserialize_ec2_query(el: Element) -> IpamPolicy:
    out: IpamPolicy = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_ipam_policy_id = el.find("IpamPolicyId")
    if child_ipam_policy_id is not None:
        out["ipam_policy_id"] = str(child_ipam_policy_id.text or "")
    child_ipam_policy_arn = el.find("IpamPolicyArn")
    if child_ipam_policy_arn is not None:
        out["ipam_policy_arn"] = str(child_ipam_policy_arn.text or "")
    child_ipam_policy_region = el.find("IpamPolicyRegion")
    if child_ipam_policy_region is not None:
        out["ipam_policy_region"] = str(child_ipam_policy_region.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.ipam_policy_state

        out["state"] = aws_sdk_ec2.types.ipam_policy_state.deserialize_ec2_query(
            child_state
        )
    child_state_message = el.find("StateMessage")
    if child_state_message is not None:
        out["state_message"] = str(child_state_message.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_ipam_id = el.find("IpamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    return out
