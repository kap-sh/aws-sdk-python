"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeGlobalReplicationGroupsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.global_replication_group_list
    import capo_elasticache.types.string


class DescribeGlobalReplicationGroupsResult(TypedDict, closed=True):
    marker: NotRequired["capo_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords. ></p>"""
    global_replication_groups: NotRequired[
        "capo_elasticache.types.global_replication_group_list.GlobalReplicationGroupList"
    ]
    """<p>Indicates the slot configuration and global identifier for each slice group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeGlobalReplicationGroupsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "global_replication_groups" in value:
        import capo_elasticache.types.global_replication_group_list

        capo_elasticache.types.global_replication_group_list.serialize_query(
            value["global_replication_groups"],
            pairs,
            f"{key_prefix}GlobalReplicationGroups",
        )


def deserialize_query(el: Element) -> DescribeGlobalReplicationGroupsResult:
    out: DescribeGlobalReplicationGroupsResult = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_global_replication_groups = el.find("GlobalReplicationGroups")
    if child_global_replication_groups is not None:
        import capo_elasticache.types.global_replication_group_list

        out["global_replication_groups"] = (
            capo_elasticache.types.global_replication_group_list.deserialize_query(
                child_global_replication_groups
            )
        )
    return out
