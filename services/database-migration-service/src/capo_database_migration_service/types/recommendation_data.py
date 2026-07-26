"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RecommendationData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.rds_recommendation


class RecommendationData(TypedDict, closed=True):
    rds_engine: NotRequired[
        "capo_database_migration_service.types.rds_recommendation.RdsRecommendation"
    ]
    """<p>The recommendation of a target Amazon RDS database engine.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationData) -> dict:
    out: dict = {}
    if "rds_engine" in value:
        import capo_database_migration_service.types.rds_recommendation

        out["RdsEngine"] = (
            capo_database_migration_service.types.rds_recommendation.serialize_aws_json_1_1(
                value["rds_engine"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommendationData:
    out: RecommendationData = {}  # type: ignore[typeddict-item]
    if "RdsEngine" in data:
        import capo_database_migration_service.types.rds_recommendation

        out["rds_engine"] = (
            capo_database_migration_service.types.rds_recommendation.deserialize_aws_json_1_1(
                data["RdsEngine"]
            )
        )
    return out
