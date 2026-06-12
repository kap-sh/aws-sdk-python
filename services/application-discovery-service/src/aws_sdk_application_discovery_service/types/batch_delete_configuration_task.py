"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#BatchDeleteConfigurationTask``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.batch_delete_configuration_task_status
    import aws_sdk_application_discovery_service.types.configuration_id_list
    import aws_sdk_application_discovery_service.types.deletion_configuration_item_type
    import aws_sdk_application_discovery_service.types.deletion_warnings_list
    import aws_sdk_application_discovery_service.types.failed_configuration_list
    import aws_sdk_application_discovery_service.types.time_stamp
    import aws_sdk_application_discovery_service.types.uuid


class BatchDeleteConfigurationTask(TypedDict):
    task_id: NotRequired["aws_sdk_application_discovery_service.types.uuid.UUID"]
    """<p> The deletion task's unique identifier. </p>"""
    status: NotRequired[
        "aws_sdk_application_discovery_service.types.batch_delete_configuration_task_status.BatchDeleteConfigurationTaskStatus"
    ]
    """<p> The current execution status of the deletion task. Valid status are: INITIALIZING | VALIDATING | DELETING | COMPLETED | FAILED. </p>"""
    start_time: NotRequired[
        "aws_sdk_application_discovery_service.types.time_stamp.TimeStamp"
    ]
    """<p> An epoch seconds timestamp (UTC) of when the deletion task was started. </p>"""
    end_time: NotRequired[
        "aws_sdk_application_discovery_service.types.time_stamp.TimeStamp"
    ]
    """<p> An epoch seconds timestamp (UTC) of when the deletion task was completed or failed. </p>"""
    configuration_type: NotRequired[
        "aws_sdk_application_discovery_service.types.deletion_configuration_item_type.DeletionConfigurationItemType"
    ]
    """<p> The type of configuration item to delete. Supported types are: SERVER. </p>"""
    requested_configurations: NotRequired[
        "aws_sdk_application_discovery_service.types.configuration_id_list.ConfigurationIdList"
    ]
    """<p> The list of configuration IDs that were originally requested to be deleted by the deletion task. </p>"""
    deleted_configurations: NotRequired[
        "aws_sdk_application_discovery_service.types.configuration_id_list.ConfigurationIdList"
    ]
    """<p> The list of configuration IDs that were successfully deleted by the deletion task. </p>"""
    failed_configurations: NotRequired[
        "aws_sdk_application_discovery_service.types.failed_configuration_list.FailedConfigurationList"
    ]
    """<p> A list of configuration IDs that failed to delete during the deletion task, each paired with an error message. </p>"""
    deletion_warnings: NotRequired[
        "aws_sdk_application_discovery_service.types.deletion_warnings_list.DeletionWarningsList"
    ]
    """<p> A list of configuration IDs that produced warnings regarding their deletion, paired with a warning message. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteConfigurationTask) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "status" in value:
        import aws_sdk_application_discovery_service.types.batch_delete_configuration_task_status

        out["status"] = (
            aws_sdk_application_discovery_service.types.batch_delete_configuration_task_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "start_time" in value:
        import aws_sdk_application_discovery_service.types.time_stamp

        out["startTime"] = (
            aws_sdk_application_discovery_service.types.time_stamp.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_application_discovery_service.types.time_stamp

        out["endTime"] = (
            aws_sdk_application_discovery_service.types.time_stamp.serialize_aws_json_1_1(
                value["end_time"]
            )
        )
    if "configuration_type" in value:
        import aws_sdk_application_discovery_service.types.deletion_configuration_item_type

        out["configurationType"] = (
            aws_sdk_application_discovery_service.types.deletion_configuration_item_type.serialize_aws_json_1_1(
                value["configuration_type"]
            )
        )
    if "requested_configurations" in value:
        import aws_sdk_application_discovery_service.types.configuration_id_list

        out["requestedConfigurations"] = (
            aws_sdk_application_discovery_service.types.configuration_id_list.serialize_aws_json_1_1(
                value["requested_configurations"]
            )
        )
    if "deleted_configurations" in value:
        import aws_sdk_application_discovery_service.types.configuration_id_list

        out["deletedConfigurations"] = (
            aws_sdk_application_discovery_service.types.configuration_id_list.serialize_aws_json_1_1(
                value["deleted_configurations"]
            )
        )
    if "failed_configurations" in value:
        import aws_sdk_application_discovery_service.types.failed_configuration_list

        out["failedConfigurations"] = (
            aws_sdk_application_discovery_service.types.failed_configuration_list.serialize_aws_json_1_1(
                value["failed_configurations"]
            )
        )
    if "deletion_warnings" in value:
        import aws_sdk_application_discovery_service.types.deletion_warnings_list

        out["deletionWarnings"] = (
            aws_sdk_application_discovery_service.types.deletion_warnings_list.serialize_aws_json_1_1(
                value["deletion_warnings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteConfigurationTask:
    out: BatchDeleteConfigurationTask = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "status" in data:
        import aws_sdk_application_discovery_service.types.batch_delete_configuration_task_status

        out["status"] = (
            aws_sdk_application_discovery_service.types.batch_delete_configuration_task_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "startTime" in data:
        import aws_sdk_application_discovery_service.types.time_stamp

        out["start_time"] = (
            aws_sdk_application_discovery_service.types.time_stamp.deserialize_aws_json_1_1(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_application_discovery_service.types.time_stamp

        out["end_time"] = (
            aws_sdk_application_discovery_service.types.time_stamp.deserialize_aws_json_1_1(
                data["endTime"]
            )
        )
    if "configurationType" in data:
        import aws_sdk_application_discovery_service.types.deletion_configuration_item_type

        out["configuration_type"] = (
            aws_sdk_application_discovery_service.types.deletion_configuration_item_type.deserialize_aws_json_1_1(
                data["configurationType"]
            )
        )
    if "requestedConfigurations" in data:
        import aws_sdk_application_discovery_service.types.configuration_id_list

        out["requested_configurations"] = (
            aws_sdk_application_discovery_service.types.configuration_id_list.deserialize_aws_json_1_1(
                data["requestedConfigurations"]
            )
        )
    if "deletedConfigurations" in data:
        import aws_sdk_application_discovery_service.types.configuration_id_list

        out["deleted_configurations"] = (
            aws_sdk_application_discovery_service.types.configuration_id_list.deserialize_aws_json_1_1(
                data["deletedConfigurations"]
            )
        )
    if "failedConfigurations" in data:
        import aws_sdk_application_discovery_service.types.failed_configuration_list

        out["failed_configurations"] = (
            aws_sdk_application_discovery_service.types.failed_configuration_list.deserialize_aws_json_1_1(
                data["failedConfigurations"]
            )
        )
    if "deletionWarnings" in data:
        import aws_sdk_application_discovery_service.types.deletion_warnings_list

        out["deletion_warnings"] = (
            aws_sdk_application_discovery_service.types.deletion_warnings_list.deserialize_aws_json_1_1(
                data["deletionWarnings"]
            )
        )
    return out
