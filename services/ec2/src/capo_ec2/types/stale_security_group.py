"""Generated from Smithy shape ``com.amazonaws.ec2#StaleSecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.stale_ip_permission_set
    import capo_ec2.types.string


class StaleSecurityGroup(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the security group.</p>"""
    group_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the security group.</p>"""
    group_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the security group.</p>"""
    stale_ip_permissions: NotRequired[
        "capo_ec2.types.stale_ip_permission_set.StaleIpPermissionSet"
    ]
    """<p>Information about the stale inbound rules in the security group.</p>"""
    stale_ip_permissions_egress: NotRequired[
        "capo_ec2.types.stale_ip_permission_set.StaleIpPermissionSet"
    ]
    """<p>Information about the stale outbound rules in the security group.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC for the security group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StaleSecurityGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "group_id" in value:
        pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "stale_ip_permissions" in value:
        import capo_ec2.types.stale_ip_permission_set

        capo_ec2.types.stale_ip_permission_set.serialize_ec2_query(
            value["stale_ip_permissions"], pairs, f"{key_prefix}StaleIpPermissions"
        )
    if "stale_ip_permissions_egress" in value:
        import capo_ec2.types.stale_ip_permission_set

        capo_ec2.types.stale_ip_permission_set.serialize_ec2_query(
            value["stale_ip_permissions_egress"],
            pairs,
            f"{key_prefix}StaleIpPermissionsEgress",
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))


def deserialize_ec2_query(el: Element) -> StaleSecurityGroup:
    out: StaleSecurityGroup = {}  # type: ignore[typeddict-item]
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_group_id = el.find("groupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_group_name = el.find("groupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_stale_ip_permissions = el.find("staleIpPermissions")
    if child_stale_ip_permissions is not None:
        import capo_ec2.types.stale_ip_permission_set

        out["stale_ip_permissions"] = (
            capo_ec2.types.stale_ip_permission_set.deserialize_ec2_query(
                child_stale_ip_permissions
            )
        )
    child_stale_ip_permissions_egress = el.find("staleIpPermissionsEgress")
    if child_stale_ip_permissions_egress is not None:
        import capo_ec2.types.stale_ip_permission_set

        out["stale_ip_permissions_egress"] = (
            capo_ec2.types.stale_ip_permission_set.deserialize_ec2_query(
                child_stale_ip_permissions_egress
            )
        )
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    return out
