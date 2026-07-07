"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheSecurityGroupMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class CacheSecurityGroupMembership(TypedDict, closed=True):
    cache_security_group_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the cache security group.</p>"""
    status: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The membership status in the cache security group. The status changes when a cache security group is modified, or when the cache security groups assigned to a cluster are modified.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheSecurityGroupMembership, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_security_group_name" in value:
        pairs.append(
            (
                f"{prefix}.CacheSecurityGroupName",
                str(value["cache_security_group_name"]),
            )
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_query(el: Element) -> CacheSecurityGroupMembership:
    out: CacheSecurityGroupMembership = {}  # type: ignore[typeddict-item]
    child_cache_security_group_name = el.find("CacheSecurityGroupName")
    if child_cache_security_group_name is not None:
        out["cache_security_group_name"] = str(
            child_cache_security_group_name.text or ""
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
