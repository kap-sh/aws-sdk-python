"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeFleetAdvisorSchemaObjectSummaryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.fleet_advisor_schema_object_list
    import aws_sdk_database_migration_service.types.string


class DescribeFleetAdvisorSchemaObjectSummaryResponse(TypedDict):
    fleet_advisor_schema_objects: NotRequired[
        "aws_sdk_database_migration_service.types.fleet_advisor_schema_object_list.FleetAdvisorSchemaObjectList"
    ]
    """<p>A collection of <code>FleetAdvisorSchemaObjectResponse</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeFleetAdvisorSchemaObjectSummaryResponse,
) -> dict:
    out: dict = {}
    if "fleet_advisor_schema_objects" in value:
        import aws_sdk_database_migration_service.types.fleet_advisor_schema_object_list

        out["FleetAdvisorSchemaObjects"] = (
            aws_sdk_database_migration_service.types.fleet_advisor_schema_object_list.serialize_aws_json_1_1(
                value["fleet_advisor_schema_objects"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeFleetAdvisorSchemaObjectSummaryResponse:
    out: DescribeFleetAdvisorSchemaObjectSummaryResponse = {}  # type: ignore[typeddict-item]
    if "FleetAdvisorSchemaObjects" in data:
        import aws_sdk_database_migration_service.types.fleet_advisor_schema_object_list

        out["fleet_advisor_schema_objects"] = (
            aws_sdk_database_migration_service.types.fleet_advisor_schema_object_list.deserialize_aws_json_1_1(
                data["FleetAdvisorSchemaObjects"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
