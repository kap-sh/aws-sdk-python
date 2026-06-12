"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeEndpointsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.endpoint_list
    import aws_sdk_database_migration_service.types.string


class DescribeEndpointsResponse(TypedDict):
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    endpoints: NotRequired[
        "aws_sdk_database_migration_service.types.endpoint_list.EndpointList"
    ]
    """<p>Endpoint description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEndpointsResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "endpoints" in value:
        import aws_sdk_database_migration_service.types.endpoint_list

        out["Endpoints"] = (
            aws_sdk_database_migration_service.types.endpoint_list.serialize_aws_json_1_1(
                value["endpoints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEndpointsResponse:
    out: DescribeEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Endpoints" in data:
        import aws_sdk_database_migration_service.types.endpoint_list

        out["endpoints"] = (
            aws_sdk_database_migration_service.types.endpoint_list.deserialize_aws_json_1_1(
                data["Endpoints"]
            )
        )
    return out
