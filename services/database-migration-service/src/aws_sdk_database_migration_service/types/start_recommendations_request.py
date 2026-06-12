"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartRecommendationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.recommendation_settings
    import aws_sdk_database_migration_service.types.string


class StartRecommendationsRequest(TypedDict):
    database_id: "aws_sdk_database_migration_service.types.string.String"
    """<p>The identifier of the source database to analyze and provide recommendations for.</p>"""
    settings: "aws_sdk_database_migration_service.types.recommendation_settings.RecommendationSettings"
    """<p>The settings in JSON format that Fleet Advisor uses to determine target engine recommendations. These parameters include target instance sizing and availability and durability settings. For target instance sizing, Fleet Advisor supports the following two options: total capacity and resource utilization. For availability and durability, Fleet Advisor supports the following two options: production (Multi-AZ deployments) and Dev/Test (Single-AZ deployments).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRecommendationsRequest) -> dict:
    out: dict = {}
    out["DatabaseId"] = value["database_id"]
    import aws_sdk_database_migration_service.types.recommendation_settings

    out["Settings"] = (
        aws_sdk_database_migration_service.types.recommendation_settings.serialize_aws_json_1_1(
            value["settings"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartRecommendationsRequest:
    out: StartRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if "DatabaseId" in data:
        out["database_id"] = data["DatabaseId"]
    else:
        raise DeserializationError("StartRecommendationsRequest.database_id required")
    if "Settings" in data:
        import aws_sdk_database_migration_service.types.recommendation_settings

        out["settings"] = (
            aws_sdk_database_migration_service.types.recommendation_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    else:
        raise DeserializationError("StartRecommendationsRequest.settings required")
    return out
