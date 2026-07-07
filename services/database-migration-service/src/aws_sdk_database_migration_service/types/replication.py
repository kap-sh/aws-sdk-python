"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#Replication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.migration_type_value
    import aws_sdk_database_migration_service.types.premigration_assessment_status_list
    import aws_sdk_database_migration_service.types.provision_data
    import aws_sdk_database_migration_service.types.replication_stats
    import aws_sdk_database_migration_service.types.string
    import aws_sdk_database_migration_service.types.string_list
    import aws_sdk_database_migration_service.types.t_stamp


class Replication(TypedDict, closed=True):
    replication_config_identifier: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The identifier for the <code>ReplicationConfig</code> associated with the replication.</p>"""
    replication_config_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name for the <code>ReplicationConfig</code> associated with the replication.</p>"""
    source_endpoint_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name for an existing <code>Endpoint</code> the serverless replication uses for its data source.</p>"""
    target_endpoint_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name for an existing <code>Endpoint</code> the serverless replication uses for its data target.</p>"""
    replication_type: NotRequired[
        "aws_sdk_database_migration_service.types.migration_type_value.MigrationTypeValue"
    ]
    """<p>The type of the serverless replication.</p>"""
    status: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The current status of the serverless replication.</p>"""
    provision_data: NotRequired[
        "aws_sdk_database_migration_service.types.provision_data.ProvisionData"
    ]
    """<p>Information about provisioning resources for an DMS serverless replication.</p>"""
    premigration_assessment_statuses: NotRequired[
        "aws_sdk_database_migration_service.types.premigration_assessment_status_list.PremigrationAssessmentStatusList"
    ]
    """<p>The status output of premigration assessment in describe-replications.</p>"""
    stop_reason: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    r"""<p>The reason the replication task was stopped. This response parameter can return one of the following values:</p> <ul> <li> <p> <code>\"Stop Reason NORMAL\"</code> </p> </li> <li> <p> <code>\"Stop Reason RECOVERABLE_ERROR\"</code> </p> </li> <li> <p> <code>\"Stop Reason FATAL_ERROR\"</code> </p> </li> <li> <p> <code>\"Stop Reason FULL_LOAD_ONLY_FINISHED\"</code> </p> </li> <li> <p> <code>\"Stop Reason STOPPED_AFTER_FULL_LOAD\"</code> – Full load completed, with cached changes not applied</p> </li> <li> <p> <code>\"Stop Reason STOPPED_AFTER_CACHED_EVENTS\"</code> – Full load completed, with cached changes applied</p> </li> <li> <p> <code>\"Stop Reason EXPRESS_LICENSE_LIMITS_REACHED\"</code> </p> </li> <li> <p> <code>\"Stop Reason STOPPED_AFTER_DDL_APPLY\"</code> – User-defined stop task after DDL applied</p> </li> <li> <p> <code>\"Stop Reason STOPPED_DUE_TO_LOW_MEMORY\"</code> </p> </li> <li> <p> <code>\"Stop Reason STOPPED_DUE_TO_LOW_DISK\"</code> </p> </li> <li> <p> <code>\"Stop Reason STOPPED_AT_SERVER_TIME\"</code> – User-defined server time for stopping task</p> </li> <li> <p> <code>\"Stop Reason STOPPED_AT_COMMIT_TIME\"</code> – User-defined commit time for stopping task</p> </li> <li> <p> <code>\"Stop Reason RECONFIGURATION_RESTART\"</code> </p> </li> <li> <p> <code>\"Stop Reason RECYCLE_TASK\"</code> </p> </li> </ul>"""
    failure_messages: NotRequired[
        "aws_sdk_database_migration_service.types.string_list.StringList"
    ]
    """<p>Error and other information about why a serverless replication failed.</p>"""
    replication_stats: NotRequired[
        "aws_sdk_database_migration_service.types.replication_stats.ReplicationStats"
    ]
    """<p>This object provides a collection of statistics about a serverless replication.</p>"""
    start_replication_type: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The type of replication to start.</p>"""
    cdc_start_time: NotRequired[
        "aws_sdk_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>Indicates the start time for a change data capture (CDC) operation. Use either <code>CdcStartTime</code> or <code>CdcStartPosition</code> to specify when you want a CDC operation to start. Specifying both values results in an error.</p>"""
    cdc_start_position: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>Indicates the start time for a change data capture (CDC) operation. Use either <code>CdcStartTime</code> or <code>CdcStartPosition</code> to specify when you want a CDC operation to start. Specifying both values results in an error.</p>"""
    cdc_stop_position: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.</p>"""
    recovery_checkpoint: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>Indicates the last checkpoint that occurred during a change data capture (CDC) operation. You can provide this value to the <code>CdcStartPosition</code> parameter to start a CDC operation that begins at that checkpoint.</p>"""
    replication_create_time: NotRequired[
        "aws_sdk_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The time the serverless replication was created.</p>"""
    replication_update_time: NotRequired[
        "aws_sdk_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The time the serverless replication was updated.</p>"""
    replication_last_stop_time: NotRequired[
        "aws_sdk_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The timestamp when replication was last stopped.</p>"""
    replication_deprovision_time: NotRequired[
        "aws_sdk_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The timestamp when DMS will deprovision the replication.</p>"""
    is_read_only: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the serverless replication is read-only. When set to <code>true</code>, this replication is managed by DMS as part of a zero-ETL integration and cannot be modified or deleted directly. You can only modify or delete read-only replications through their associated zero-ETL integration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Replication) -> dict:
    out: dict = {}
    if "replication_config_identifier" in value:
        out["ReplicationConfigIdentifier"] = value["replication_config_identifier"]
    if "replication_config_arn" in value:
        out["ReplicationConfigArn"] = value["replication_config_arn"]
    if "source_endpoint_arn" in value:
        out["SourceEndpointArn"] = value["source_endpoint_arn"]
    if "target_endpoint_arn" in value:
        out["TargetEndpointArn"] = value["target_endpoint_arn"]
    if "replication_type" in value:
        import aws_sdk_database_migration_service.types.migration_type_value

        out["ReplicationType"] = (
            aws_sdk_database_migration_service.types.migration_type_value.serialize_aws_json_1_1(
                value["replication_type"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "provision_data" in value:
        import aws_sdk_database_migration_service.types.provision_data

        out["ProvisionData"] = (
            aws_sdk_database_migration_service.types.provision_data.serialize_aws_json_1_1(
                value["provision_data"]
            )
        )
    if "premigration_assessment_statuses" in value:
        import aws_sdk_database_migration_service.types.premigration_assessment_status_list

        out["PremigrationAssessmentStatuses"] = (
            aws_sdk_database_migration_service.types.premigration_assessment_status_list.serialize_aws_json_1_1(
                value["premigration_assessment_statuses"]
            )
        )
    if "stop_reason" in value:
        out["StopReason"] = value["stop_reason"]
    if "failure_messages" in value:
        import aws_sdk_database_migration_service.types.string_list

        out["FailureMessages"] = (
            aws_sdk_database_migration_service.types.string_list.serialize_aws_json_1_1(
                value["failure_messages"]
            )
        )
    if "replication_stats" in value:
        import aws_sdk_database_migration_service.types.replication_stats

        out["ReplicationStats"] = (
            aws_sdk_database_migration_service.types.replication_stats.serialize_aws_json_1_1(
                value["replication_stats"]
            )
        )
    if "start_replication_type" in value:
        out["StartReplicationType"] = value["start_replication_type"]
    if "cdc_start_time" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["CdcStartTime"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["cdc_start_time"]
            )
        )
    if "cdc_start_position" in value:
        out["CdcStartPosition"] = value["cdc_start_position"]
    if "cdc_stop_position" in value:
        out["CdcStopPosition"] = value["cdc_stop_position"]
    if "recovery_checkpoint" in value:
        out["RecoveryCheckpoint"] = value["recovery_checkpoint"]
    if "replication_create_time" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["ReplicationCreateTime"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["replication_create_time"]
            )
        )
    if "replication_update_time" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["ReplicationUpdateTime"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["replication_update_time"]
            )
        )
    if "replication_last_stop_time" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["ReplicationLastStopTime"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["replication_last_stop_time"]
            )
        )
    if "replication_deprovision_time" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["ReplicationDeprovisionTime"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["replication_deprovision_time"]
            )
        )
    if "is_read_only" in value:
        out["IsReadOnly"] = value["is_read_only"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Replication:
    out: Replication = {}  # type: ignore[typeddict-item]
    if "ReplicationConfigIdentifier" in data:
        out["replication_config_identifier"] = data["ReplicationConfigIdentifier"]
    if "ReplicationConfigArn" in data:
        out["replication_config_arn"] = data["ReplicationConfigArn"]
    if "SourceEndpointArn" in data:
        out["source_endpoint_arn"] = data["SourceEndpointArn"]
    if "TargetEndpointArn" in data:
        out["target_endpoint_arn"] = data["TargetEndpointArn"]
    if "ReplicationType" in data:
        import aws_sdk_database_migration_service.types.migration_type_value

        out["replication_type"] = (
            aws_sdk_database_migration_service.types.migration_type_value.deserialize_aws_json_1_1(
                data["ReplicationType"]
            )
        )
    if "Status" in data:
        out["status"] = data["Status"]
    if "ProvisionData" in data:
        import aws_sdk_database_migration_service.types.provision_data

        out["provision_data"] = (
            aws_sdk_database_migration_service.types.provision_data.deserialize_aws_json_1_1(
                data["ProvisionData"]
            )
        )
    if "PremigrationAssessmentStatuses" in data:
        import aws_sdk_database_migration_service.types.premigration_assessment_status_list

        out["premigration_assessment_statuses"] = (
            aws_sdk_database_migration_service.types.premigration_assessment_status_list.deserialize_aws_json_1_1(
                data["PremigrationAssessmentStatuses"]
            )
        )
    if "StopReason" in data:
        out["stop_reason"] = data["StopReason"]
    if "FailureMessages" in data:
        import aws_sdk_database_migration_service.types.string_list

        out["failure_messages"] = (
            aws_sdk_database_migration_service.types.string_list.deserialize_aws_json_1_1(
                data["FailureMessages"]
            )
        )
    if "ReplicationStats" in data:
        import aws_sdk_database_migration_service.types.replication_stats

        out["replication_stats"] = (
            aws_sdk_database_migration_service.types.replication_stats.deserialize_aws_json_1_1(
                data["ReplicationStats"]
            )
        )
    if "StartReplicationType" in data:
        out["start_replication_type"] = data["StartReplicationType"]
    if "CdcStartTime" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["cdc_start_time"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["CdcStartTime"]
            )
        )
    if "CdcStartPosition" in data:
        out["cdc_start_position"] = data["CdcStartPosition"]
    if "CdcStopPosition" in data:
        out["cdc_stop_position"] = data["CdcStopPosition"]
    if "RecoveryCheckpoint" in data:
        out["recovery_checkpoint"] = data["RecoveryCheckpoint"]
    if "ReplicationCreateTime" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["replication_create_time"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ReplicationCreateTime"]
            )
        )
    if "ReplicationUpdateTime" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["replication_update_time"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ReplicationUpdateTime"]
            )
        )
    if "ReplicationLastStopTime" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["replication_last_stop_time"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ReplicationLastStopTime"]
            )
        )
    if "ReplicationDeprovisionTime" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["replication_deprovision_time"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ReplicationDeprovisionTime"]
            )
        )
    if "IsReadOnly" in data:
        out["is_read_only"] = data["IsReadOnly"]
    return out
