"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#Recommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.recommendation_data
    import aws_sdk_database_migration_service.types.recommendation_settings
    import aws_sdk_database_migration_service.types.string


class Recommendation(TypedDict):
    database_id: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The identifier of the source database for which Fleet Advisor provided this recommendation.</p>"""
    engine_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The name of the target engine. Valid values include <code>\"rds-aurora-mysql\"</code>, <code>\"rds-aurora-postgresql\"</code>, <code>\"rds-mysql\"</code>, <code>\"rds-oracle\"</code>, <code>\"rds-sql-server\"</code>, and <code>\"rds-postgresql\"</code>.</p>"""
    created_date: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The date when Fleet Advisor created the target engine recommendation.</p>"""
    status: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The status of the target engine recommendation. Valid values include <code>\"alternate\"</code>, <code>\"in-progress\"</code>, <code>\"not-viable\"</code>, and <code>\"recommended\"</code>.</p>"""
    preferred: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates that this target is the rightsized migration destination.</p>"""
    settings: NotRequired[
        "aws_sdk_database_migration_service.types.recommendation_settings.RecommendationSettings"
    ]
    """<p>The settings in JSON format for the preferred target engine parameters. These parameters include capacity, resource utilization, and the usage type (production, development, or testing).</p>"""
    data: NotRequired[
        "aws_sdk_database_migration_service.types.recommendation_data.RecommendationData"
    ]
    """<p>The recommendation of a target engine for the specified source database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Recommendation) -> dict:
    out: dict = {}
    if "database_id" in value:
        out["DatabaseId"] = value["database_id"]
    if "engine_name" in value:
        out["EngineName"] = value["engine_name"]
    if "created_date" in value:
        out["CreatedDate"] = value["created_date"]
    if "status" in value:
        out["Status"] = value["status"]
    if "preferred" in value:
        out["Preferred"] = value["preferred"]
    if "settings" in value:
        import aws_sdk_database_migration_service.types.recommendation_settings

        out["Settings"] = (
            aws_sdk_database_migration_service.types.recommendation_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    if "data" in value:
        import aws_sdk_database_migration_service.types.recommendation_data

        out["Data"] = (
            aws_sdk_database_migration_service.types.recommendation_data.serialize_aws_json_1_1(
                value["data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if "DatabaseId" in data:
        out["database_id"] = data["DatabaseId"]
    if "EngineName" in data:
        out["engine_name"] = data["EngineName"]
    if "CreatedDate" in data:
        out["created_date"] = data["CreatedDate"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "Preferred" in data:
        out["preferred"] = data["Preferred"]
    if "Settings" in data:
        import aws_sdk_database_migration_service.types.recommendation_settings

        out["settings"] = (
            aws_sdk_database_migration_service.types.recommendation_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    if "Data" in data:
        import aws_sdk_database_migration_service.types.recommendation_data

        out["data"] = (
            aws_sdk_database_migration_service.types.recommendation_data.deserialize_aws_json_1_1(
                data["Data"]
            )
        )
    return out
