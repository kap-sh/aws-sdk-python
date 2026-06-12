"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeUsersMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.engine_type
    import aws_sdk_elasticache.types.filter_list
    import aws_sdk_elasticache.types.integer_optional
    import aws_sdk_elasticache.types.string
    import aws_sdk_elasticache.types.user_id


class DescribeUsersMessage(TypedDict):
    engine: NotRequired["aws_sdk_elasticache.types.engine_type.EngineType"]
    """<p>The engine. </p>"""
    user_id: NotRequired["aws_sdk_elasticache.types.user_id.UserId"]
    """<p>The ID of the user.</p>"""
    filters: NotRequired["aws_sdk_elasticache.types.filter_list.FilterList"]
    """<p>Filter to determine the list of User IDs to return.</p>"""
    max_records: NotRequired[
        "aws_sdk_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved. </p>"""
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords. ></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeUsersMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "user_id" in value:
        pairs.append((f"{prefix}.UserId", str(value["user_id"])))
    if "filters" in value:
        import aws_sdk_elasticache.types.filter_list

        aws_sdk_elasticache.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeUsersMessage:
    out: DescribeUsersMessage = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_user_id = el.find("UserId")
    if child_user_id is not None:
        out["user_id"] = str(child_user_id.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import aws_sdk_elasticache.types.filter_list

        out["filters"] = aws_sdk_elasticache.types.filter_list.deserialize_query(
            child_filters
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
