"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ip_permission_list
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class SecurityGroup(TypedDict, closed=True):
    group_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the security group.</p>"""
    ip_permissions_egress: NotRequired[
        "capo_ec2.types.ip_permission_list.IpPermissionList"
    ]
    """<p>The outbound rules associated with the security group.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the security group.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC for the security group.</p>"""
    security_group_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the security group.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the security group.</p>"""
    group_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the security group.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description of the security group.</p>"""
    ip_permissions: NotRequired["capo_ec2.types.ip_permission_list.IpPermissionList"]
    """<p>The inbound rules associated with the security group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "group_id" in value:
        pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))
    if "ip_permissions_egress" in value:
        import capo_ec2.types.ip_permission_list

        capo_ec2.types.ip_permission_list.serialize_ec2_query(
            value["ip_permissions_egress"], pairs, f"{key_prefix}IpPermissionsEgress"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "security_group_arn" in value:
        pairs.append(
            (f"{key_prefix}SecurityGroupArn", str(value["security_group_arn"]))
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "description" in value:
        pairs.append((f"{key_prefix}GroupDescription", str(value["description"])))
    if "ip_permissions" in value:
        import capo_ec2.types.ip_permission_list

        capo_ec2.types.ip_permission_list.serialize_ec2_query(
            value["ip_permissions"], pairs, f"{key_prefix}IpPermissions"
        )


def deserialize_ec2_query(el: Element) -> SecurityGroup:
    out: SecurityGroup = {}  # type: ignore[typeddict-item]
    child_group_id = el.find("groupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    if el.find("ipPermissionsEgress") is not None:
        import capo_ec2.types.ip_permission_list

        out["ip_permissions_egress"] = (
            capo_ec2.types.ip_permission_list.deserialize_ec2_query(
                el, "ipPermissionsEgress"
            )
        )
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_security_group_arn = el.find("securityGroupArn")
    if child_security_group_arn is not None:
        out["security_group_arn"] = str(child_security_group_arn.text or "")
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_group_name = el.find("groupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_description = el.find("groupDescription")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    if el.find("ipPermissions") is not None:
        import capo_ec2.types.ip_permission_list

        out["ip_permissions"] = capo_ec2.types.ip_permission_list.deserialize_ec2_query(
            el, "ipPermissions"
        )
    return out
