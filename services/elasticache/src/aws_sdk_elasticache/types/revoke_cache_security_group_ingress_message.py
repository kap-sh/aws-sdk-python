"""Generated from Smithy shape ``com.amazonaws.elasticache#RevokeCacheSecurityGroupIngressMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class RevokeCacheSecurityGroupIngressMessage(TypedDict):
    cache_security_group_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the cache security group to revoke ingress from.</p>"""
    ec2_security_group_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the Amazon EC2 security group to revoke access from.</p>"""
    ec2_security_group_owner_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The Amazon account number of the Amazon EC2 security group owner. Note that this is not the same thing as an Amazon access key ID - you must provide a valid Amazon account number for this parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RevokeCacheSecurityGroupIngressMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "cache_security_group_name" in value:
        pairs.append(
            (
                f"{prefix}.CacheSecurityGroupName",
                str(value["cache_security_group_name"]),
            )
        )
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


def deserialize_query(el: Element) -> RevokeCacheSecurityGroupIngressMessage:
    out: RevokeCacheSecurityGroupIngressMessage = {}  # type: ignore[typeddict-item]
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
