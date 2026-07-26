"""Generated from Smithy shape ``com.amazonaws.rds#RevokeDBSecurityGroupIngressMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class RevokeDBSecurityGroupIngressMessage(TypedDict, closed=True):
    db_security_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB security group to revoke ingress from.</p>"""
    cidrip: NotRequired["capo_rds.types.string.String"]
    """<p>The IP range to revoke access from. Must be a valid CIDR range. If <code>CIDRIP</code> is specified, <code>EC2SecurityGroupName</code>, <code>EC2SecurityGroupId</code> and <code>EC2SecurityGroupOwnerId</code> can't be provided.</p>"""
    ec2_security_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the EC2 security group to revoke access from. For VPC DB security groups, <code>EC2SecurityGroupId</code> must be provided. Otherwise, EC2SecurityGroupOwnerId and either <code>EC2SecurityGroupName</code> or <code>EC2SecurityGroupId</code> must be provided.</p>"""
    ec2_security_group_id: NotRequired["capo_rds.types.string.String"]
    """<p>The id of the EC2 security group to revoke access from. For VPC DB security groups, <code>EC2SecurityGroupId</code> must be provided. Otherwise, EC2SecurityGroupOwnerId and either <code>EC2SecurityGroupName</code> or <code>EC2SecurityGroupId</code> must be provided.</p>"""
    ec2_security_group_owner_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services account number of the owner of the EC2 security group specified in the <code>EC2SecurityGroupName</code> parameter. The Amazon Web Services access key ID isn't an acceptable value. For VPC DB security groups, <code>EC2SecurityGroupId</code> must be provided. Otherwise, EC2SecurityGroupOwnerId and either <code>EC2SecurityGroupName</code> or <code>EC2SecurityGroupId</code> must be provided.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RevokeDBSecurityGroupIngressMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_security_group_name" in value:
        pairs.append(
            (f"{prefix}.DBSecurityGroupName", str(value["db_security_group_name"]))
        )
    if "cidrip" in value:
        pairs.append((f"{prefix}.CIDRIP", str(value["cidrip"])))
    if "ec2_security_group_name" in value:
        pairs.append(
            (f"{prefix}.EC2SecurityGroupName", str(value["ec2_security_group_name"]))
        )
    if "ec2_security_group_id" in value:
        pairs.append(
            (f"{prefix}.EC2SecurityGroupId", str(value["ec2_security_group_id"]))
        )
    if "ec2_security_group_owner_id" in value:
        pairs.append(
            (
                f"{prefix}.EC2SecurityGroupOwnerId",
                str(value["ec2_security_group_owner_id"]),
            )
        )


def deserialize_query(el: Element) -> RevokeDBSecurityGroupIngressMessage:
    out: RevokeDBSecurityGroupIngressMessage = {}  # type: ignore[typeddict-item]
    child_db_security_group_name = el.find("DBSecurityGroupName")
    if child_db_security_group_name is not None:
        out["db_security_group_name"] = str(child_db_security_group_name.text or "")
    child_cidrip = el.find("CIDRIP")
    if child_cidrip is not None:
        out["cidrip"] = str(child_cidrip.text or "")
    child_ec2_security_group_name = el.find("EC2SecurityGroupName")
    if child_ec2_security_group_name is not None:
        out["ec2_security_group_name"] = str(child_ec2_security_group_name.text or "")
    child_ec2_security_group_id = el.find("EC2SecurityGroupId")
    if child_ec2_security_group_id is not None:
        out["ec2_security_group_id"] = str(child_ec2_security_group_id.text or "")
    child_ec2_security_group_owner_id = el.find("EC2SecurityGroupOwnerId")
    if child_ec2_security_group_owner_id is not None:
        out["ec2_security_group_owner_id"] = str(
            child_ec2_security_group_owner_id.text or ""
        )
    return out
