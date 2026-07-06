"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBShardGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_shard_groups_list
    import aws_sdk_rds.types.string


class DescribeDBShardGroupsResponse(TypedDict, closed=True):
    db_shard_groups: NotRequired[
        "aws_sdk_rds.types.db_shard_groups_list.DBShardGroupsList"
    ]
    """<p>Contains a list of DB shard groups for the user.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A pagination token that can be used in a later <code>DescribeDBClusters</code> request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBShardGroupsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_shard_groups" in value:
        import aws_sdk_rds.types.db_shard_groups_list

        aws_sdk_rds.types.db_shard_groups_list.serialize_query(
            value["db_shard_groups"], pairs, f"{prefix}.DBShardGroups"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDBShardGroupsResponse:
    out: DescribeDBShardGroupsResponse = {}  # type: ignore[typeddict-item]
    child_db_shard_groups = el.find("DBShardGroups")
    if child_db_shard_groups is not None:
        import aws_sdk_rds.types.db_shard_groups_list

        out["db_shard_groups"] = (
            aws_sdk_rds.types.db_shard_groups_list.deserialize_query(
                child_db_shard_groups
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
