"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataMigrationSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.secret_string


class DataMigrationSettings(TypedDict):
    number_of_jobs: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of parallel jobs that trigger parallel threads to unload the tables from the source, and then load them to the target.</p>"""
    cloudwatch_logs_enabled: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Whether to enable CloudWatch logging for the data migration.</p>"""
    selection_rules: NotRequired[
        "aws_sdk_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>A JSON-formatted string that defines what objects to include and exclude from the migration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataMigrationSettings) -> dict:
    out: dict = {}
    if "number_of_jobs" in value:
        out["NumberOfJobs"] = value["number_of_jobs"]
    if "cloudwatch_logs_enabled" in value:
        out["CloudwatchLogsEnabled"] = value["cloudwatch_logs_enabled"]
    if "selection_rules" in value:
        out["SelectionRules"] = value["selection_rules"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataMigrationSettings:
    out: DataMigrationSettings = {}  # type: ignore[typeddict-item]
    if "NumberOfJobs" in data:
        out["number_of_jobs"] = data["NumberOfJobs"]
    if "CloudwatchLogsEnabled" in data:
        out["cloudwatch_logs_enabled"] = data["CloudwatchLogsEnabled"]
    if "SelectionRules" in data:
        out["selection_rules"] = data["SelectionRules"]
    return out
