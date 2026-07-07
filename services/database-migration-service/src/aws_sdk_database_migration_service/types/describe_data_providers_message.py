"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeDataProvidersMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.filter_list
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.string


class DescribeDataProvidersMessage(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_database_migration_service.types.filter_list.FilterList"
    ]
    """<p>Filters applied to the data providers described in the form of key-value pairs.</p> <p>Valid filter names and values: data-provider-identifier, data provider arn or name</p>"""
    max_records: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, DMS includes a pagination token in the response so that you can retrieve the remaining results.</p>"""
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>Marker</code> is returned by a previous response, there are more results available. The value of <code>Marker</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDataProvidersMessage) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_database_migration_service.types.filter_list

        out["Filters"] = (
            aws_sdk_database_migration_service.types.filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDataProvidersMessage:
    out: DescribeDataProvidersMessage = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_database_migration_service.types.filter_list

        out["filters"] = (
            aws_sdk_database_migration_service.types.filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxRecords" in data:
        out["max_records"] = data["MaxRecords"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
