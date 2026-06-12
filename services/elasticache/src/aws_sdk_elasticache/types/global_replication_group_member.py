"""Generated from Smithy shape ``com.amazonaws.elasticache#GlobalReplicationGroupMember``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.automatic_failover_status
    import aws_sdk_elasticache.types.string


class GlobalReplicationGroupMember(TypedDict):
    replication_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The replication group id of the Global datastore member.</p>"""
    replication_group_region: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The Amazon region of the Global datastore member.</p>"""
    role: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>Indicates the role of the replication group, primary or secondary.</p>"""
    automatic_failover: NotRequired[
        "aws_sdk_elasticache.types.automatic_failover_status.AutomaticFailoverStatus"
    ]
    """<p>Indicates whether automatic failover is enabled for the replication group.</p>"""
    status: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The status of the membership of the replication group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalReplicationGroupMember, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "replication_group_id" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "replication_group_region" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupRegion", str(value["replication_group_region"]))
        )
    if "role" in value:
        pairs.append((f"{prefix}.Role", str(value["role"])))
    if "automatic_failover" in value:
        import aws_sdk_elasticache.types.automatic_failover_status

        aws_sdk_elasticache.types.automatic_failover_status.serialize_query(
            value["automatic_failover"], pairs, f"{prefix}.AutomaticFailover"
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_query(el: Element) -> GlobalReplicationGroupMember:
    out: GlobalReplicationGroupMember = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_replication_group_region = el.find("ReplicationGroupRegion")
    if child_replication_group_region is not None:
        out["replication_group_region"] = str(child_replication_group_region.text or "")
    child_role = el.find("Role")
    if child_role is not None:
        out["role"] = str(child_role.text or "")
    child_automatic_failover = el.find("AutomaticFailover")
    if child_automatic_failover is not None:
        import aws_sdk_elasticache.types.automatic_failover_status

        out["automatic_failover"] = (
            aws_sdk_elasticache.types.automatic_failover_status.deserialize_query(
                child_automatic_failover
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
