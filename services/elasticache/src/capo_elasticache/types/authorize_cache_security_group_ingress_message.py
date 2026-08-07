"""Generated from Smithy shape ``com.amazonaws.elasticache#AuthorizeCacheSecurityGroupIngressMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class AuthorizeCacheSecurityGroupIngressMessage(TypedDict, closed=True):
    cache_security_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The cache security group that allows network ingress.</p>"""
    ec2_security_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Amazon EC2 security group to be authorized for ingress to the cache security group.</p>"""
    ec2_security_group_owner_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Amazon account number of the Amazon EC2 security group owner. Note that this is not the same thing as an Amazon access key ID - you must provide a valid Amazon account number for this parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthorizeCacheSecurityGroupIngressMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cache_security_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}CacheSecurityGroupName",
                str(value["cache_security_group_name"]),
            )
        )
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


def deserialize_query(el: Element) -> AuthorizeCacheSecurityGroupIngressMessage:
    out: AuthorizeCacheSecurityGroupIngressMessage = {}  # type: ignore[typeddict-item]
    child_cache_security_group_name = el.find("CacheSecurityGroupName")
    if child_cache_security_group_name is not None:
        out["cache_security_group_name"] = str(
            child_cache_security_group_name.text or ""
        )
    child_ec2_security_group_name = el.find("EC2SecurityGroupName")
    if child_ec2_security_group_name is not None:
        out["ec2_security_group_name"] = str(child_ec2_security_group_name.text or "")
    child_ec2_security_group_owner_id = el.find("EC2SecurityGroupOwnerId")
    if child_ec2_security_group_owner_id is not None:
        out["ec2_security_group_owner_id"] = str(
            child_ec2_security_group_owner_id.text or ""
        )
    return out
