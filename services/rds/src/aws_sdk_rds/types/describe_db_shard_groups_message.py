"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBShardGroupsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_shard_group_identifier
    import aws_sdk_rds.types.filter_list
    import aws_sdk_rds.types.max_records
    import aws_sdk_rds.types.string


class DescribeDBShardGroupsMessage(TypedDict):
    db_shard_group_identifier: NotRequired[
        "aws_sdk_rds.types.db_shard_group_identifier.DBShardGroupIdentifier"
    ]
    """<p>The user-supplied DB shard group identifier. If this parameter is specified, information for only the specific DB shard group is returned. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match an existing DB shard group identifier.</p> </li> </ul>"""
    filters: NotRequired["aws_sdk_rds.types.filter_list.FilterList"]
    """<p>A filter that specifies one or more DB shard groups to describe.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeDBShardGroups</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    max_records: NotRequired["aws_sdk_rds.types.max_records.MaxRecords"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBShardGroupsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_shard_group_identifier" in value:
        pairs.append(
            (
                f"{prefix}.DBShardGroupIdentifier",
                str(value["db_shard_group_identifier"]),
            )
        )
    if "filters" in value:
        import aws_sdk_rds.types.filter_list

        aws_sdk_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribeDBShardGroupsMessage:
    out: DescribeDBShardGroupsMessage = {}  # type: ignore[typeddict-item]
    child_db_shard_group_identifier = el.find("DBShardGroupIdentifier")
    if child_db_shard_group_identifier is not None:
        out["db_shard_group_identifier"] = str(
            child_db_shard_group_identifier.text or ""
        )
    child_filters = el.find("Filters")
    if child_filters is not None:
        import aws_sdk_rds.types.filter_list

        out["filters"] = aws_sdk_rds.types.filter_list.deserialize_query(child_filters)
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out
