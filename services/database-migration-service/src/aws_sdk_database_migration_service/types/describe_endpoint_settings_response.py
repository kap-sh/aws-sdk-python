"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeEndpointSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.endpoint_settings_list
    import aws_sdk_database_migration_service.types.string


class DescribeEndpointSettingsResponse(TypedDict):
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    endpoint_settings: NotRequired[
        "aws_sdk_database_migration_service.types.endpoint_settings_list.EndpointSettingsList"
    ]
    """<p>Descriptions of the endpoint settings available for your source or target database engine.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEndpointSettingsResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "endpoint_settings" in value:
        import aws_sdk_database_migration_service.types.endpoint_settings_list

        out["EndpointSettings"] = (
            aws_sdk_database_migration_service.types.endpoint_settings_list.serialize_aws_json_1_1(
                value["endpoint_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEndpointSettingsResponse:
    out: DescribeEndpointSettingsResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "EndpointSettings" in data:
        import aws_sdk_database_migration_service.types.endpoint_settings_list

        out["endpoint_settings"] = (
            aws_sdk_database_migration_service.types.endpoint_settings_list.deserialize_aws_json_1_1(
                data["EndpointSettings"]
            )
        )
    return out
