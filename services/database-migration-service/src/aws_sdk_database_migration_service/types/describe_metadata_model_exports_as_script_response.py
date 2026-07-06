"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeMetadataModelExportsAsScriptResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.schema_conversion_request_list
    import aws_sdk_database_migration_service.types.string


class DescribeMetadataModelExportsAsScriptResponse(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>Marker</code> is returned by a previous response, there are more results available. The value of <code>Marker</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>"""
    requests: NotRequired[
        "aws_sdk_database_migration_service.types.schema_conversion_request_list.SchemaConversionRequestList"
    ]
    """<p>A paginated list of metadata model exports.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMetadataModelExportsAsScriptResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "requests" in value:
        import aws_sdk_database_migration_service.types.schema_conversion_request_list

        out["Requests"] = (
            aws_sdk_database_migration_service.types.schema_conversion_request_list.serialize_aws_json_1_1(
                value["requests"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeMetadataModelExportsAsScriptResponse:
    out: DescribeMetadataModelExportsAsScriptResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Requests" in data:
        import aws_sdk_database_migration_service.types.schema_conversion_request_list

        out["requests"] = (
            aws_sdk_database_migration_service.types.schema_conversion_request_list.deserialize_aws_json_1_1(
                data["Requests"]
            )
        )
    return out
