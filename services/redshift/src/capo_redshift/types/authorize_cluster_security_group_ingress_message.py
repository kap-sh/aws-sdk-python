"""Generated from Smithy shape ``com.amazonaws.redshift#AuthorizeClusterSecurityGroupIngressMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class AuthorizeClusterSecurityGroupIngressMessage(TypedDict, closed=True):
    cluster_security_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the security group to which the ingress rule is added.</p>"""
    cidrip: NotRequired["capo_redshift.types.string.String"]
    """<p>The IP range to be added the Amazon Redshift security group.</p>"""
    ec2_security_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The EC2 security group to be added the Amazon Redshift security group.</p>"""
    ec2_security_group_owner_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Web Services account number of the owner of the security group specified by the <i>EC2SecurityGroupName</i> parameter. The Amazon Web Services Access Key ID is not an acceptable value. </p> <p>Example: <code>111122223333</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthorizeClusterSecurityGroupIngressMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster_security_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}ClusterSecurityGroupName",
                str(value["cluster_security_group_name"]),
            )
        )
    if "cidrip" in value:
        pairs.append((f"{key_prefix}CIDRIP", str(value["cidrip"])))
    if "ec2_security_group_name" in value:
        pairs.append(
            (f"{key_prefix}EC2SecurityGroupName", str(value["ec2_security_group_name"]))
        )
    if "ec2_security_group_owner_id" in value:
        pairs.append(
            (
                f"{key_prefix}EC2SecurityGroupOwnerId",
                str(value["ec2_security_group_owner_id"]),
            )
        )


def deserialize_query(el: Element) -> AuthorizeClusterSecurityGroupIngressMessage:
    out: AuthorizeClusterSecurityGroupIngressMessage = {}  # type: ignore[typeddict-item]
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
