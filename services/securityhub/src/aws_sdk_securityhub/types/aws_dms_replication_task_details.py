"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDmsReplicationTaskDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsDmsReplicationTaskDetails(TypedDict, closed=True):
    cdc_start_position: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Indicates when you want a change data capture (CDC) operation to start. <code>CCdcStartPosition</code> or <code>CCdcStartTime</code> specifies when you want a CDC operation to start. Only a value for one of these fields is included.</p>"""
    cdc_start_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Indicates the start time for a CDC operation. <code>CdcStartPosition</code> or <code>CCdcStartTime</code> specifies when you want a CDC operation to start. Only a value for one of these fields is included.</p>"""
    cdc_stop_position: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Indicates when you want a CDC operation to stop. The value can be either server time or commit time.</p>"""
    migration_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The migration type. </p>"""
    id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The identifier of the replication task.</p>"""
    resource_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A display name for the resource identifier at the end of the <code>EndpointArn</code> response parameter. If you don't specify a <code>ResourceIdentifier</code> value, DMS generates a default identifier value for the end of <code>EndpointArn</code>.</p>"""
    replication_instance_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of a replication instance. </p>"""
    replication_task_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The user-defined replication task identifier or name.</p>"""
    replication_task_settings: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The settings for the replication task.</p>"""
    source_endpoint_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ARN of the source endpoint.</p>"""
    table_mappings: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The table mappings for the replication task, in JSON format.</p>"""
    target_endpoint_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ARN of the target endpoint.</p>"""
    task_data: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Supplemental information that the task requires to migrate the data for certain source and target endpoints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDmsReplicationTaskDetails) -> dict:
    out: dict = {}
    if "cdc_start_position" in value:
        out["CdcStartPosition"] = value["cdc_start_position"]
    if "cdc_start_time" in value:
        out["CdcStartTime"] = value["cdc_start_time"]
    if "cdc_stop_position" in value:
        out["CdcStopPosition"] = value["cdc_stop_position"]
    if "migration_type" in value:
        out["MigrationType"] = value["migration_type"]
    if "id" in value:
        out["Id"] = value["id"]
    if "resource_identifier" in value:
        out["ResourceIdentifier"] = value["resource_identifier"]
    if "replication_instance_arn" in value:
        out["ReplicationInstanceArn"] = value["replication_instance_arn"]
    if "replication_task_identifier" in value:
        out["ReplicationTaskIdentifier"] = value["replication_task_identifier"]
    if "replication_task_settings" in value:
        out["ReplicationTaskSettings"] = value["replication_task_settings"]
    if "source_endpoint_arn" in value:
        out["SourceEndpointArn"] = value["source_endpoint_arn"]
    if "table_mappings" in value:
        out["TableMappings"] = value["table_mappings"]
    if "target_endpoint_arn" in value:
        out["TargetEndpointArn"] = value["target_endpoint_arn"]
    if "task_data" in value:
        out["TaskData"] = value["task_data"]
    return out


def deserialize_json(data: dict) -> AwsDmsReplicationTaskDetails:
    out: AwsDmsReplicationTaskDetails = {}  # type: ignore[typeddict-item]
    if "CdcStartPosition" in data:
        out["cdc_start_position"] = data["CdcStartPosition"]
    if "CdcStartTime" in data:
        out["cdc_start_time"] = data["CdcStartTime"]
    if "CdcStopPosition" in data:
        out["cdc_stop_position"] = data["CdcStopPosition"]
    if "MigrationType" in data:
        out["migration_type"] = data["MigrationType"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ResourceIdentifier" in data:
        out["resource_identifier"] = data["ResourceIdentifier"]
    if "ReplicationInstanceArn" in data:
        out["replication_instance_arn"] = data["ReplicationInstanceArn"]
    if "ReplicationTaskIdentifier" in data:
        out["replication_task_identifier"] = data["ReplicationTaskIdentifier"]
    if "ReplicationTaskSettings" in data:
        out["replication_task_settings"] = data["ReplicationTaskSettings"]
    if "SourceEndpointArn" in data:
        out["source_endpoint_arn"] = data["SourceEndpointArn"]
    if "TableMappings" in data:
        out["table_mappings"] = data["TableMappings"]
    if "TargetEndpointArn" in data:
        out["target_endpoint_arn"] = data["TargetEndpointArn"]
    if "TaskData" in data:
        out["task_data"] = data["TaskData"]
    return out
