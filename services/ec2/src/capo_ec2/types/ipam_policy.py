"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_id
    import capo_ec2.types.ipam_policy_id
    import capo_ec2.types.ipam_policy_state
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class IpamPolicy(TypedDict, closed=True):
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The account ID that owns the IPAM policy.</p>"""
    ipam_policy_id: NotRequired["capo_ec2.types.ipam_policy_id.IpamPolicyId"]
    """<p>The ID of the IPAM policy.</p>"""
    ipam_policy_arn: NotRequired["capo_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the IPAM policy.</p>"""
    ipam_policy_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region of the IPAM policy.</p>"""
    state: NotRequired["capo_ec2.types.ipam_policy_state.IpamPolicyState"]
    """<p>The state of the IPAM policy.</p>"""
    state_message: NotRequired["capo_ec2.types.string.String"]
    """<p>A message about the state of the IPAM policy.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the IPAM policy.</p>"""
    ipam_id: NotRequired["capo_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM this policy belongs to.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "ipam_policy_id" in value:
        pairs.append((f"{key_prefix}IpamPolicyId", str(value["ipam_policy_id"])))
    if "ipam_policy_arn" in value:
        pairs.append((f"{key_prefix}IpamPolicyArn", str(value["ipam_policy_arn"])))
    if "ipam_policy_region" in value:
        pairs.append(
            (f"{key_prefix}IpamPolicyRegion", str(value["ipam_policy_region"]))
        )
    if "state" in value:
        import capo_ec2.types.ipam_policy_state

        capo_ec2.types.ipam_policy_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "state_message" in value:
        pairs.append((f"{key_prefix}StateMessage", str(value["state_message"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "ipam_id" in value:
        pairs.append((f"{key_prefix}IpamId", str(value["ipam_id"])))


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
        import capo_ec2.types.ipam_policy_state

        out["state"] = capo_ec2.types.ipam_policy_state.deserialize_ec2_query(
            child_state
        )
    child_state_message = el.find("StateMessage")
    if child_state_message is not None:
        out["state_message"] = str(child_state_message.text or "")
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_ipam_id = el.find("IpamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    return out
