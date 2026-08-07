"""Generated from Smithy shape ``com.amazonaws.elasticache#SecurityGroupMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class SecurityGroupMembership(TypedDict, closed=True):
    security_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The identifier of the cache security group.</p>"""
    status: NotRequired["capo_elasticache.types.string.String"]
    """<p>The status of the cache security group membership. The status changes whenever a cache security group is modified, or when the cache security groups assigned to a cluster are modified.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SecurityGroupMembership, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "security_group_id" in value:
        pairs.append((f"{key_prefix}SecurityGroupId", str(value["security_group_id"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))


def deserialize_query(el: Element) -> SecurityGroupMembership:
    out: SecurityGroupMembership = {}  # type: ignore[typeddict-item]
    child_security_group_id = el.find("SecurityGroupId")
    if child_security_group_id is not None:
        out["security_group_id"] = str(child_security_group_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
