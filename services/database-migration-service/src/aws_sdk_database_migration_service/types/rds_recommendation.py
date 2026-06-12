"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RdsRecommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.rds_configuration
    import aws_sdk_database_migration_service.types.rds_requirements


class RdsRecommendation(TypedDict):
    requirements_to_target: NotRequired[
        "aws_sdk_database_migration_service.types.rds_requirements.RdsRequirements"
    ]
    """<p>Supplemental information about the requirements to the recommended target database on Amazon RDS.</p>"""
    target_configuration: NotRequired[
        "aws_sdk_database_migration_service.types.rds_configuration.RdsConfiguration"
    ]
    """<p>Supplemental information about the configuration of the recommended target database on Amazon RDS.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RdsRecommendation) -> dict:
    out: dict = {}
    if "requirements_to_target" in value:
        import aws_sdk_database_migration_service.types.rds_requirements

        out["RequirementsToTarget"] = (
            aws_sdk_database_migration_service.types.rds_requirements.serialize_aws_json_1_1(
                value["requirements_to_target"]
            )
        )
    if "target_configuration" in value:
        import aws_sdk_database_migration_service.types.rds_configuration

        out["TargetConfiguration"] = (
            aws_sdk_database_migration_service.types.rds_configuration.serialize_aws_json_1_1(
                value["target_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RdsRecommendation:
    out: RdsRecommendation = {}  # type: ignore[typeddict-item]
    if "RequirementsToTarget" in data:
        import aws_sdk_database_migration_service.types.rds_requirements

        out["requirements_to_target"] = (
            aws_sdk_database_migration_service.types.rds_requirements.deserialize_aws_json_1_1(
                data["RequirementsToTarget"]
            )
        )
    if "TargetConfiguration" in data:
        import aws_sdk_database_migration_service.types.rds_configuration

        out["target_configuration"] = (
            aws_sdk_database_migration_service.types.rds_configuration.deserialize_aws_json_1_1(
                data["TargetConfiguration"]
            )
        )
    return out
