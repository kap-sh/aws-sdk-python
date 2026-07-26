"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeEndpointSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.endpoint_settings_list
    import capo_database_migration_service.types.string


class DescribeEndpointSettingsResponse(TypedDict, closed=True):
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    endpoint_settings: NotRequired[
        "capo_database_migration_service.types.endpoint_settings_list.EndpointSettingsList"
    ]
    """<p>Descriptions of the endpoint settings available for your source or target database engine.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEndpointSettingsResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "endpoint_settings" in value:
        import capo_database_migration_service.types.endpoint_settings_list

        out["EndpointSettings"] = (
            capo_database_migration_service.types.endpoint_settings_list.serialize_aws_json_1_1(
                value["endpoint_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEndpointSettingsResponse:
    out: DescribeEndpointSettingsResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "EndpointSettings" in data:
        import capo_database_migration_service.types.endpoint_settings_list

        out["endpoint_settings"] = (
            capo_database_migration_service.types.endpoint_settings_list.deserialize_aws_json_1_1(
                data["EndpointSettings"]
            )
        )
    return out
