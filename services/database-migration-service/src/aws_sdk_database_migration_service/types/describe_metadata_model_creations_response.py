"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeMetadataModelCreationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.schema_conversion_request_list
    import aws_sdk_database_migration_service.types.string


class DescribeMetadataModelCreationsResponse(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Specifies the unique pagination token that makes it possible to display the next page of metadata model creation requests. If Marker is returned, there are more metadata model creation requests available.</p>"""
    requests: NotRequired[
        "aws_sdk_database_migration_service.types.schema_conversion_request_list.SchemaConversionRequestList"
    ]
    """<p>A list of metadata model creation requests. The ExportSqlDetails field will never be populated for the DescribeMetadataModelCreations operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMetadataModelCreationsResponse) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> DescribeMetadataModelCreationsResponse:
    out: DescribeMetadataModelCreationsResponse = {}  # type: ignore[typeddict-item]
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
