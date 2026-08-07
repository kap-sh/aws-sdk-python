"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheSecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.ec2_security_group_list
    import capo_elasticache.types.string


class CacheSecurityGroup(TypedDict, closed=True):
    owner_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Amazon account ID of the cache security group owner.</p>"""
    cache_security_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache security group.</p>"""
    description: NotRequired["capo_elasticache.types.string.String"]
    """<p>The description of the cache security group.</p>"""
    ec2_security_groups: NotRequired[
        "capo_elasticache.types.ec2_security_group_list.EC2SecurityGroupList"
    ]
    """<p>A list of Amazon EC2 security groups that are associated with this cache security group.</p>"""
    arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ARN of the cache security group,</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheSecurityGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "cache_security_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}CacheSecurityGroupName",
                str(value["cache_security_group_name"]),
            )
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "ec2_security_groups" in value:
        import capo_elasticache.types.ec2_security_group_list

        capo_elasticache.types.ec2_security_group_list.serialize_query(
            value["ec2_security_groups"], pairs, f"{key_prefix}EC2SecurityGroups"
        )
    if "arn" in value:
        pairs.append((f"{key_prefix}ARN", str(value["arn"])))


def deserialize_query(el: Element) -> CacheSecurityGroup:
    out: CacheSecurityGroup = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_cache_security_group_name = el.find("CacheSecurityGroupName")
    if child_cache_security_group_name is not None:
        out["cache_security_group_name"] = str(
            child_cache_security_group_name.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_ec2_security_groups = el.find("EC2SecurityGroups")
    if child_ec2_security_groups is not None:
        import capo_elasticache.types.ec2_security_group_list

        out["ec2_security_groups"] = (
            capo_elasticache.types.ec2_security_group_list.deserialize_query(
                child_ec2_security_groups
            )
        )
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out
