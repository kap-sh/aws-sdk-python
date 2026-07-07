"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeOrderableReplicationInstancesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.string


class DescribeOrderableReplicationInstancesMessage(TypedDict, closed=True):
    max_records: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeOrderableReplicationInstancesMessage) -> dict:
    out: dict = {}
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeOrderableReplicationInstancesMessage:
    out: DescribeOrderableReplicationInstancesMessage = {}  # type: ignore[typeddict-item]
    if "MaxRecords" in data:
        out["max_records"] = data["MaxRecords"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
