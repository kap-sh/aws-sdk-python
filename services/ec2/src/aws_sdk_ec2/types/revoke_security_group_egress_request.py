"""Generated from Smithy shape ``com.amazonaws.ec2#RevokeSecurityGroupEgressRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ip_permission_list
    import aws_sdk_ec2.types.security_group_id
    import aws_sdk_ec2.types.security_group_rule_id_list
    import aws_sdk_ec2.types.string


class RevokeSecurityGroupEgressRequest(TypedDict):
    security_group_rule_ids: NotRequired[
        "aws_sdk_ec2.types.security_group_rule_id_list.SecurityGroupRuleIdList"
    ]
    """<p>The IDs of the security group rules.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.security_group_id.SecurityGroupId"]
    """<p>The ID of the security group.</p>"""
    source_security_group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Not supported. Use a set of IP permissions to specify a destination security group.</p>"""
    source_security_group_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Not supported. Use a set of IP permissions to specify a destination security group.</p>"""
    ip_protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Not supported. Use a set of IP permissions to specify the protocol name or number.</p>"""
    from_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>Not supported. Use a set of IP permissions to specify the port.</p>"""
    to_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>Not supported. Use a set of IP permissions to specify the port.</p>"""
    cidr_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Not supported. Use a set of IP permissions to specify the CIDR.</p>"""
    ip_permissions: NotRequired["aws_sdk_ec2.types.ip_permission_list.IpPermissionList"]
    """<p>The sets of IP permissions. You can't specify a destination security group and a CIDR IP address range in the same set of permissions.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RevokeSecurityGroupEgressRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "security_group_rule_ids" in value:
        import aws_sdk_ec2.types.security_group_rule_id_list

        aws_sdk_ec2.types.security_group_rule_id_list.serialize_ec2_query(
            value["security_group_rule_ids"], pairs, f"{prefix}.SecurityGroupRuleIds"
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
        import aws_sdk_ec2.types.ip_permission_list

        aws_sdk_ec2.types.ip_permission_list.serialize_ec2_query(
            value["ip_permissions"], pairs, f"{prefix}.IpPermissions"
        )


def deserialize_ec2_query(el: Element) -> RevokeSecurityGroupEgressRequest:
    out: RevokeSecurityGroupEgressRequest = {}  # type: ignore[typeddict-item]
    if el.find("SecurityGroupRuleIds") is not None:
        import aws_sdk_ec2.types.security_group_rule_id_list

        out["security_group_rule_ids"] = (
            aws_sdk_ec2.types.security_group_rule_id_list.deserialize_ec2_query(
                el, "SecurityGroupRuleIds"
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
        import aws_sdk_ec2.types.ip_permission_list

        out["ip_permissions"] = (
            aws_sdk_ec2.types.ip_permission_list.deserialize_ec2_query(
                el, "IpPermissions"
            )
        )
    return out
