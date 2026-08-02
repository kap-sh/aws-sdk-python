"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBShardGroupsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_shard_group_identifier
    import capo_rds.types.filter_list
    import capo_rds.types.max_records
    import capo_rds.types.string


class DescribeDBShardGroupsMessage(TypedDict, closed=True):
    db_shard_group_identifier: NotRequired[
        "capo_rds.types.db_shard_group_identifier.DBShardGroupIdentifier"
    ]
    """<p>The user-supplied DB shard group identifier. If this parameter is specified, information for only the specific DB shard group is returned. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match an existing DB shard group identifier.</p> </li> </ul>"""
    filters: NotRequired["capo_rds.types.filter_list.FilterList"]
    """<p>A filter that specifies one or more DB shard groups to describe.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeDBShardGroups</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    max_records: NotRequired["capo_rds.types.max_records.MaxRecords"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBShardGroupsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_shard_group_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}DBShardGroupIdentifier",
                str(value["db_shard_group_identifier"]),
            )
        )
    if "filters" in value:
        import capo_rds.types.filter_list

        capo_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribeDBShardGroupsMessage:
    out: DescribeDBShardGroupsMessage = {}  # type: ignore[typeddict-item]
    child_db_shard_group_identifier = el.find("DBShardGroupIdentifier")
    if child_db_shard_group_identifier is not None:
        out["db_shard_group_identifier"] = str(
            child_db_shard_group_identifier.text or ""
        )
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_rds.types.filter_list

        out["filters"] = capo_rds.types.filter_list.deserialize_query(child_filters)
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out
