"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeFleetAdvisorSchemasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.fleet_advisor_schema_list
    import aws_sdk_database_migration_service.types.string


class DescribeFleetAdvisorSchemasResponse(TypedDict, closed=True):
    fleet_advisor_schemas: NotRequired[
        "aws_sdk_database_migration_service.types.fleet_advisor_schema_list.FleetAdvisorSchemaList"
    ]
    """<p>A collection of <code>SchemaResponse</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetAdvisorSchemasResponse) -> dict:
    out: dict = {}
    if "fleet_advisor_schemas" in value:
        import aws_sdk_database_migration_service.types.fleet_advisor_schema_list

        out["FleetAdvisorSchemas"] = (
            aws_sdk_database_migration_service.types.fleet_advisor_schema_list.serialize_aws_json_1_1(
                value["fleet_advisor_schemas"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetAdvisorSchemasResponse:
    out: DescribeFleetAdvisorSchemasResponse = {}  # type: ignore[typeddict-item]
    if "FleetAdvisorSchemas" in data:
        import aws_sdk_database_migration_service.types.fleet_advisor_schema_list

        out["fleet_advisor_schemas"] = (
            aws_sdk_database_migration_service.types.fleet_advisor_schema_list.deserialize_aws_json_1_1(
                data["FleetAdvisorSchemas"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
