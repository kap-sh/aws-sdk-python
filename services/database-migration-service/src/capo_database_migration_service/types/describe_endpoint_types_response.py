"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeEndpointTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.supported_endpoint_type_list


class DescribeEndpointTypesResponse(TypedDict, closed=True):
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    supported_endpoint_types: NotRequired[
        "capo_database_migration_service.types.supported_endpoint_type_list.SupportedEndpointTypeList"
    ]
    """<p>The types of endpoints that are supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEndpointTypesResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "supported_endpoint_types" in value:
        import capo_database_migration_service.types.supported_endpoint_type_list

        out["SupportedEndpointTypes"] = (
            capo_database_migration_service.types.supported_endpoint_type_list.serialize_aws_json_1_1(
                value["supported_endpoint_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEndpointTypesResponse:
    out: DescribeEndpointTypesResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "SupportedEndpointTypes" in data:
        import capo_database_migration_service.types.supported_endpoint_type_list

        out["supported_endpoint_types"] = (
            capo_database_migration_service.types.supported_endpoint_type_list.deserialize_aws_json_1_1(
                data["SupportedEndpointTypes"]
            )
        )
    return out
