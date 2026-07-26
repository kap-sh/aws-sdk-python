"""Generated from Smithy shape ``com.amazonaws.elasticache#DisassociateGlobalReplicationGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class DisassociateGlobalReplicationGroupMessage(TypedDict, closed=True):
    global_replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the Global datastore</p>"""
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the secondary cluster you wish to remove from the Global datastore</p>"""
    replication_group_region: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Amazon region of secondary cluster you wish to remove from the Global datastore</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DisassociateGlobalReplicationGroupMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "global_replication_group_id" in value:
        pairs.append(
            (
                f"{prefix}.GlobalReplicationGroupId",
                str(value["global_replication_group_id"]),
            )
        )
    if "replication_group_id" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "replication_group_region" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupRegion", str(value["replication_group_region"]))
        )


def deserialize_query(el: Element) -> DisassociateGlobalReplicationGroupMessage:
    out: DisassociateGlobalReplicationGroupMessage = {}  # type: ignore[typeddict-item]
    child_global_replication_group_id = el.find("GlobalReplicationGroupId")
    if child_global_replication_group_id is not None:
        out["global_replication_group_id"] = str(
            child_global_replication_group_id.text or ""
        )
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_replication_group_region = el.find("ReplicationGroupRegion")
    if child_replication_group_region is not None:
        out["replication_group_region"] = str(child_replication_group_region.text or "")
    return out
