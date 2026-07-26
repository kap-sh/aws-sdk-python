"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.recommendation

RecommendationList: TypeAlias = list[
    "capo_database_migration_service.types.recommendation.Recommendation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationList) -> list:
    import capo_database_migration_service.types.recommendation

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.recommendation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RecommendationList:
    import capo_database_migration_service.types.recommendation

    out: RecommendationList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.recommendation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
