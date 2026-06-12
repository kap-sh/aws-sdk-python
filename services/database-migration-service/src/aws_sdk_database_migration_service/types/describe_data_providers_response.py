"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeDataProvidersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.data_provider_list
    import aws_sdk_database_migration_service.types.string


class DescribeDataProvidersResponse(TypedDict):
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>Marker</code> is returned by a previous response, there are more results available. The value of <code>Marker</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>"""
    data_providers: NotRequired[
        "aws_sdk_database_migration_service.types.data_provider_list.DataProviderList"
    ]
    """<p>A description of data providers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDataProvidersResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "data_providers" in value:
        import aws_sdk_database_migration_service.types.data_provider_list

        out["DataProviders"] = (
            aws_sdk_database_migration_service.types.data_provider_list.serialize_aws_json_1_1(
                value["data_providers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDataProvidersResponse:
    out: DescribeDataProvidersResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "DataProviders" in data:
        import aws_sdk_database_migration_service.types.data_provider_list

        out["data_providers"] = (
            aws_sdk_database_migration_service.types.data_provider_list.deserialize_aws_json_1_1(
                data["DataProviders"]
            )
        )
    return out
