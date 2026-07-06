"""Generated from Smithy shape ``com.amazonaws.elasticache#FailoverGlobalReplicationGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class FailoverGlobalReplicationGroupMessage(TypedDict, closed=True):
    global_replication_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the Global datastore</p>"""
    primary_region: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The Amazon region of the primary cluster of the Global datastore</p>"""
    primary_replication_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the primary replication group</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: FailoverGlobalReplicationGroupMessage,
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
    if "primary_region" in value:
        pairs.append((f"{prefix}.PrimaryRegion", str(value["primary_region"])))
    if "primary_replication_group_id" in value:
        pairs.append(
            (
                f"{prefix}.PrimaryReplicationGroupId",
                str(value["primary_replication_group_id"]),
            )
        )


def deserialize_query(el: Element) -> FailoverGlobalReplicationGroupMessage:
    out: FailoverGlobalReplicationGroupMessage = {}  # type: ignore[typeddict-item]
    child_global_replication_group_id = el.find("GlobalReplicationGroupId")
    if child_global_replication_group_id is not None:
        out["global_replication_group_id"] = str(
            child_global_replication_group_id.text or ""
        )
    child_primary_region = el.find("PrimaryRegion")
    if child_primary_region is not None:
        out["primary_region"] = str(child_primary_region.text or "")
    child_primary_replication_group_id = el.find("PrimaryReplicationGroupId")
    if child_primary_replication_group_id is not None:
        out["primary_replication_group_id"] = str(
            child_primary_replication_group_id.text or ""
        )
    return out
