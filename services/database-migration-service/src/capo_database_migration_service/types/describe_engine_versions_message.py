"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeEngineVersionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class DescribeEngineVersionsMessage(TypedDict, closed=True):
    max_records: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p>"""
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEngineVersionsMessage) -> dict:
    out: dict = {}
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEngineVersionsMessage:
    out: DescribeEngineVersionsMessage = {}  # type: ignore[typeddict-item]
    if "MaxRecords" in data:
        out["max_records"] = data["MaxRecords"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
