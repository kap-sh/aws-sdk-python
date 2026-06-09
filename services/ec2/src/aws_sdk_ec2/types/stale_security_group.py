"""Generated from Smithy shape ``com.amazonaws.ec2#StaleSecurityGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.stale_ip_permission_set
    import aws_sdk_ec2.types.string


class StaleSecurityGroup(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the security group.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the security group.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the security group.</p>"""
    stale_ip_permissions: NotRequired[
        "aws_sdk_ec2.types.stale_ip_permission_set.StaleIpPermissionSet"
    ]
    """<p>Information about the stale inbound rules in the security group.</p>"""
    stale_ip_permissions_egress: NotRequired[
        "aws_sdk_ec2.types.stale_ip_permission_set.StaleIpPermissionSet"
    ]
    """<p>Information about the stale outbound rules in the security group.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC for the security group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StaleSecurityGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "group_id" in value:
        pairs.append((f"{prefix}.GroupId", str(value["group_id"])))
    if "group_name" in value:
        pairs.append((f"{prefix}.GroupName", str(value["group_name"])))
    if "stale_ip_permissions" in value:
        import aws_sdk_ec2.types.stale_ip_permission_set

        aws_sdk_ec2.types.stale_ip_permission_set.serialize_ec2_query(
            value["stale_ip_permissions"], pairs, f"{prefix}.StaleIpPermissions"
        )
    if "stale_ip_permissions_egress" in value:
        import aws_sdk_ec2.types.stale_ip_permission_set

        aws_sdk_ec2.types.stale_ip_permission_set.serialize_ec2_query(
            value["stale_ip_permissions_egress"],
            pairs,
            f"{prefix}.StaleIpPermissionsEgress",
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))


def deserialize_ec2_query(el: Element) -> StaleSecurityGroup:
    out: StaleSecurityGroup = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    if el.find("StaleIpPermissions") is not None:
        import aws_sdk_ec2.types.stale_ip_permission_set

        out["stale_ip_permissions"] = (
            aws_sdk_ec2.types.stale_ip_permission_set.deserialize_ec2_query(
                el, "StaleIpPermissions"
            )
        )
    if el.find("StaleIpPermissionsEgress") is not None:
        import aws_sdk_ec2.types.stale_ip_permission_set

        out["stale_ip_permissions_egress"] = (
            aws_sdk_ec2.types.stale_ip_permission_set.deserialize_ec2_query(
                el, "StaleIpPermissionsEgress"
            )
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    return out
