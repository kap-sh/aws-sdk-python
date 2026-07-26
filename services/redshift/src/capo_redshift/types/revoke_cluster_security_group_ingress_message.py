"""Generated from Smithy shape ``com.amazonaws.redshift#RevokeClusterSecurityGroupIngressMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class RevokeClusterSecurityGroupIngressMessage(TypedDict, closed=True):
    cluster_security_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the security Group from which to revoke the ingress rule.</p>"""
    cidrip: NotRequired["capo_redshift.types.string.String"]
    """<p>The IP range for which to revoke access. This range must be a valid Classless Inter-Domain Routing (CIDR) block of IP addresses. If <code>CIDRIP</code> is specified, <code>EC2SecurityGroupName</code> and <code>EC2SecurityGroupOwnerId</code> cannot be provided. </p>"""
    ec2_security_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the EC2 Security Group whose access is to be revoked. If <code>EC2SecurityGroupName</code> is specified, <code>EC2SecurityGroupOwnerId</code> must also be provided and <code>CIDRIP</code> cannot be provided. </p>"""
    ec2_security_group_owner_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Web Services account number of the owner of the security group specified in the <code>EC2SecurityGroupName</code> parameter. The Amazon Web Services access key ID is not an acceptable value. If <code>EC2SecurityGroupOwnerId</code> is specified, <code>EC2SecurityGroupName</code> must also be provided. and <code>CIDRIP</code> cannot be provided. </p> <p>Example: <code>111122223333</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RevokeClusterSecurityGroupIngressMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "cluster_security_group_name" in value:
        pairs.append(
            (
                f"{prefix}.ClusterSecurityGroupName",
                str(value["cluster_security_group_name"]),
            )
        )
    if "cidrip" in value:
        pairs.append((f"{prefix}.CIDRIP", str(value["cidrip"])))
    if "ec2_security_group_name" in value:
        pairs.append(
            (f"{prefix}.EC2SecurityGroupName", str(value["ec2_security_group_name"]))
        )
    if "ec2_security_group_owner_id" in value:
        pairs.append(
            (
                f"{prefix}.EC2SecurityGroupOwnerId",
                str(value["ec2_security_group_owner_id"]),
            )
        )


def deserialize_query(el: Element) -> RevokeClusterSecurityGroupIngressMessage:
    out: RevokeClusterSecurityGroupIngressMessage = {}  # type: ignore[typeddict-item]
    child_cluster_security_group_name = el.find("ClusterSecurityGroupName")
    if child_cluster_security_group_name is not None:
        out["cluster_security_group_name"] = str(
            child_cluster_security_group_name.text or ""
        )
    child_cidrip = el.find("CIDRIP")
    if child_cidrip is not None:
        out["cidrip"] = str(child_cidrip.text or "")
    child_ec2_security_group_name = el.find("EC2SecurityGroupName")
    if child_ec2_security_group_name is not None:
        out["ec2_security_group_name"] = str(child_ec2_security_group_name.text or "")
    child_ec2_security_group_owner_id = el.find("EC2SecurityGroupOwnerId")
    if child_ec2_security_group_owner_id is not None:
        out["ec2_security_group_owner_id"] = str(
            child_ec2_security_group_owner_id.text or ""
        )
    return out
