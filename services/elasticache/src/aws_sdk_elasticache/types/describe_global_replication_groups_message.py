"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeGlobalReplicationGroupsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.boolean_optional
    import aws_sdk_elasticache.types.integer_optional
    import aws_sdk_elasticache.types.string


class DescribeGlobalReplicationGroupsMessage(TypedDict):
    global_replication_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the Global datastore</p>"""
    max_records: NotRequired[
        "aws_sdk_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved. </p>"""
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    show_member_info: NotRequired[
        "aws_sdk_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>Returns the list of members that comprise the Global datastore.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeGlobalReplicationGroupsMessage,
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
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "show_member_info" in value:
        pairs.append(
            (
                f"{prefix}.ShowMemberInfo",
                "true" if value["show_member_info"] else "false",
            )
        )


def deserialize_query(el: Element) -> DescribeGlobalReplicationGroupsMessage:
    out: DescribeGlobalReplicationGroupsMessage = {}  # type: ignore[typeddict-item]
    child_global_replication_group_id = el.find("GlobalReplicationGroupId")
    if child_global_replication_group_id is not None:
        out["global_replication_group_id"] = str(
            child_global_replication_group_id.text or ""
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_show_member_info = el.find("ShowMemberInfo")
    if child_show_member_info is not None:
        out["show_member_info"] = (child_show_member_info.text or "").lower() == "true"
    return out
