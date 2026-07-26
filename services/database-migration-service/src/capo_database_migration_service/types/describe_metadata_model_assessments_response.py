"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeMetadataModelAssessmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.schema_conversion_request_list
    import capo_database_migration_service.types.string


class DescribeMetadataModelAssessmentsResponse(TypedDict, closed=True):
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>Marker</code> is returned by a previous response, there are more results available. The value of <code>Marker</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>"""
    requests: NotRequired[
        "capo_database_migration_service.types.schema_conversion_request_list.SchemaConversionRequestList"
    ]
    """<p>A paginated list of metadata model assessments for the specified migration project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMetadataModelAssessmentsResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "requests" in value:
        import capo_database_migration_service.types.schema_conversion_request_list

        out["Requests"] = (
            capo_database_migration_service.types.schema_conversion_request_list.serialize_aws_json_1_1(
                value["requests"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMetadataModelAssessmentsResponse:
    out: DescribeMetadataModelAssessmentsResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Requests" in data:
        import capo_database_migration_service.types.schema_conversion_request_list

        out["requests"] = (
            capo_database_migration_service.types.schema_conversion_request_list.deserialize_aws_json_1_1(
                data["Requests"]
            )
        )
    return out
