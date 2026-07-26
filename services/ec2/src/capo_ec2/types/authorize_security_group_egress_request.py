"""Generated from Smithy shape ``com.amazonaws.ec2#AuthorizeSecurityGroupEgressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.ip_permission_list
    import capo_ec2.types.security_group_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class AuthorizeSecurityGroupEgressRequest(TypedDict, closed=True):
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags applied to the security group rule.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    group_id: NotRequired["capo_ec2.types.security_group_id.SecurityGroupId"]
    """<p>The ID of the security group.</p>"""
    source_security_group_name: NotRequired["capo_ec2.types.string.String"]
    """<p>Not supported. Use IP permissions instead.</p>"""
    source_security_group_owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>Not supported. Use IP permissions instead.</p>"""
    ip_protocol: NotRequired["capo_ec2.types.string.String"]
    """<p>Not supported. Use IP permissions instead.</p>"""
    from_port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>Not supported. Use IP permissions instead.</p>"""
    to_port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>Not supported. Use IP permissions instead.</p>"""
    cidr_ip: NotRequired["capo_ec2.types.string.String"]
    """<p>Not supported. Use IP permissions instead.</p>"""
    ip_permissions: NotRequired["capo_ec2.types.ip_permission_list.IpPermissionList"]
    """<p>The permissions for the security group rules.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AuthorizeSecurityGroupEgressRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "group_id" in value:
        pairs.append((f"{prefix}.GroupId", str(value["group_id"])))
    if "source_security_group_name" in value:
        pairs.append(
            (
                f"{prefix}.SourceSecurityGroupName",
                str(value["source_security_group_name"]),
            )
        )
    if "source_security_group_owner_id" in value:
        pairs.append(
            (
                f"{prefix}.SourceSecurityGroupOwnerId",
                str(value["source_security_group_owner_id"]),
            )
        )
    if "ip_protocol" in value:
        pairs.append((f"{prefix}.IpProtocol", str(value["ip_protocol"])))
    if "from_port" in value:
        pairs.append((f"{prefix}.FromPort", str(value["from_port"])))
    if "to_port" in value:
        pairs.append((f"{prefix}.ToPort", str(value["to_port"])))
    if "cidr_ip" in value:
        pairs.append((f"{prefix}.CidrIp", str(value["cidr_ip"])))
    if "ip_permissions" in value:
        import capo_ec2.types.ip_permission_list

        capo_ec2.types.ip_permission_list.serialize_ec2_query(
            value["ip_permissions"], pairs, f"{prefix}.IpPermissions"
        )


def deserialize_ec2_query(el: Element) -> AuthorizeSecurityGroupEgressRequest:
    out: AuthorizeSecurityGroupEgressRequest = {}  # type: ignore[typeddict-item]
    if el.find("TagSpecifications") is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_source_security_group_name = el.find("SourceSecurityGroupName")
    if child_source_security_group_name is not None:
        out["source_security_group_name"] = str(
            child_source_security_group_name.text or ""
        )
    child_source_security_group_owner_id = el.find("SourceSecurityGroupOwnerId")
    if child_source_security_group_owner_id is not None:
        out["source_security_group_owner_id"] = str(
            child_source_security_group_owner_id.text or ""
        )
    child_ip_protocol = el.find("IpProtocol")
    if child_ip_protocol is not None:
        out["ip_protocol"] = str(child_ip_protocol.text or "")
    child_from_port = el.find("FromPort")
    if child_from_port is not None:
        out["from_port"] = int(child_from_port.text or "")
    child_to_port = el.find("ToPort")
    if child_to_port is not None:
        out["to_port"] = int(child_to_port.text or "")
    child_cidr_ip = el.find("CidrIp")
    if child_cidr_ip is not None:
        out["cidr_ip"] = str(child_cidr_ip.text or "")
    if el.find("IpPermissions") is not None:
        import capo_ec2.types.ip_permission_list

        out["ip_permissions"] = capo_ec2.types.ip_permission_list.deserialize_ec2_query(
            el, "IpPermissions"
        )
    return out
