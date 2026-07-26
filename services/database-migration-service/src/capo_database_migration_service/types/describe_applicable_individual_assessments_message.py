"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeApplicableIndividualAssessmentsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.migration_type_value
    import capo_database_migration_service.types.string


class DescribeApplicableIndividualAssessmentsMessage(TypedDict, closed=True):
    replication_task_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Amazon Resource Name (ARN) of a migration task on which you want to base the default list of individual assessments.</p>"""
    replication_instance_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>ARN of a replication instance on which you want to base the default list of individual assessments.</p>"""
    replication_config_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Amazon Resource Name (ARN) of a serverless replication on which you want to base the default list of individual assessments.</p>"""
    source_engine_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Name of a database engine that the specified replication instance supports as a source.</p>"""
    target_engine_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Name of a database engine that the specified replication instance supports as a target.</p>"""
    migration_type: NotRequired[
        "capo_database_migration_service.types.migration_type_value.MigrationTypeValue"
    ]
    """<p>Name of the migration type that each provided individual assessment must support.</p>"""
    max_records: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p>"""
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeApplicableIndividualAssessmentsMessage,
) -> dict:
    out: dict = {}
    if "replication_task_arn" in value:
        out["ReplicationTaskArn"] = value["replication_task_arn"]
    if "replication_instance_arn" in value:
        out["ReplicationInstanceArn"] = value["replication_instance_arn"]
    if "replication_config_arn" in value:
        out["ReplicationConfigArn"] = value["replication_config_arn"]
    if "source_engine_name" in value:
        out["SourceEngineName"] = value["source_engine_name"]
    if "target_engine_name" in value:
        out["TargetEngineName"] = value["target_engine_name"]
    if "migration_type" in value:
        import capo_database_migration_service.types.migration_type_value

        out["MigrationType"] = (
            capo_database_migration_service.types.migration_type_value.serialize_aws_json_1_1(
                value["migration_type"]
            )
        )
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeApplicableIndividualAssessmentsMessage:
    out: DescribeApplicableIndividualAssessmentsMessage = {}  # type: ignore[typeddict-item]
    if "ReplicationTaskArn" in data:
        out["replication_task_arn"] = data["ReplicationTaskArn"]
    if "ReplicationInstanceArn" in data:
        out["replication_instance_arn"] = data["ReplicationInstanceArn"]
    if "ReplicationConfigArn" in data:
        out["replication_config_arn"] = data["ReplicationConfigArn"]
    if "SourceEngineName" in data:
        out["source_engine_name"] = data["SourceEngineName"]
    if "TargetEngineName" in data:
        out["target_engine_name"] = data["TargetEngineName"]
    if "MigrationType" in data:
        import capo_database_migration_service.types.migration_type_value

        out["migration_type"] = (
            capo_database_migration_service.types.migration_type_value.deserialize_aws_json_1_1(
                data["MigrationType"]
            )
        )
    if "MaxRecords" in data:
        out["max_records"] = data["MaxRecords"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
