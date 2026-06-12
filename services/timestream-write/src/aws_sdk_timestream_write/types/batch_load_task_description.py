"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#BatchLoadTaskDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.batch_load_progress_report
    import aws_sdk_timestream_write.types.batch_load_status
    import aws_sdk_timestream_write.types.batch_load_task_id
    import aws_sdk_timestream_write.types.data_model_configuration
    import aws_sdk_timestream_write.types.data_source_configuration
    import aws_sdk_timestream_write.types.date
    import aws_sdk_timestream_write.types.record_version
    import aws_sdk_timestream_write.types.report_configuration
    import aws_sdk_timestream_write.types.resource_name
    import aws_sdk_timestream_write.types.string_value2048


class BatchLoadTaskDescription(TypedDict):
    task_id: NotRequired[
        "aws_sdk_timestream_write.types.batch_load_task_id.BatchLoadTaskId"
    ]
    """<p>The ID of the batch load task.</p>"""
    error_message: NotRequired[
        "aws_sdk_timestream_write.types.string_value2048.StringValue2048"
    ]
    """<p></p>"""
    data_source_configuration: NotRequired[
        "aws_sdk_timestream_write.types.data_source_configuration.DataSourceConfiguration"
    ]
    """<p>Configuration details about the data source for a batch load task.</p>"""
    progress_report: NotRequired[
        "aws_sdk_timestream_write.types.batch_load_progress_report.BatchLoadProgressReport"
    ]
    """<p></p>"""
    report_configuration: NotRequired[
        "aws_sdk_timestream_write.types.report_configuration.ReportConfiguration"
    ]
    """<p>Report configuration for a batch load task. This contains details about where error reports are stored.</p>"""
    data_model_configuration: NotRequired[
        "aws_sdk_timestream_write.types.data_model_configuration.DataModelConfiguration"
    ]
    """<p>Data model configuration for a batch load task. This contains details about where a data model for a batch load task is stored.</p>"""
    target_database_name: NotRequired[
        "aws_sdk_timestream_write.types.resource_name.ResourceName"
    ]
    """<p></p>"""
    target_table_name: NotRequired[
        "aws_sdk_timestream_write.types.resource_name.ResourceName"
    ]
    """<p></p>"""
    task_status: NotRequired[
        "aws_sdk_timestream_write.types.batch_load_status.BatchLoadStatus"
    ]
    """<p>Status of the batch load task.</p>"""
    record_version: "aws_sdk_timestream_write.types.record_version.RecordVersion"
    """<p></p>"""
    creation_time: NotRequired["aws_sdk_timestream_write.types.date.Date"]
    """<p>The time when the Timestream batch load task was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_timestream_write.types.date.Date"]
    """<p>The time when the Timestream batch load task was last updated.</p>"""
    resumable_until: NotRequired["aws_sdk_timestream_write.types.date.Date"]
    """<p> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchLoadTaskDescription) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "data_source_configuration" in value:
        import aws_sdk_timestream_write.types.data_source_configuration

        out["DataSourceConfiguration"] = (
            aws_sdk_timestream_write.types.data_source_configuration.serialize_aws_json_1_0(
                value["data_source_configuration"]
            )
        )
    if "progress_report" in value:
        import aws_sdk_timestream_write.types.batch_load_progress_report

        out["ProgressReport"] = (
            aws_sdk_timestream_write.types.batch_load_progress_report.serialize_aws_json_1_0(
                value["progress_report"]
            )
        )
    if "report_configuration" in value:
        import aws_sdk_timestream_write.types.report_configuration

        out["ReportConfiguration"] = (
            aws_sdk_timestream_write.types.report_configuration.serialize_aws_json_1_0(
                value["report_configuration"]
            )
        )
    if "data_model_configuration" in value:
        import aws_sdk_timestream_write.types.data_model_configuration

        out["DataModelConfiguration"] = (
            aws_sdk_timestream_write.types.data_model_configuration.serialize_aws_json_1_0(
                value["data_model_configuration"]
            )
        )
    if "target_database_name" in value:
        out["TargetDatabaseName"] = value["target_database_name"]
    if "target_table_name" in value:
        out["TargetTableName"] = value["target_table_name"]
    if "task_status" in value:
        import aws_sdk_timestream_write.types.batch_load_status

        out["TaskStatus"] = (
            aws_sdk_timestream_write.types.batch_load_status.serialize_aws_json_1_0(
                value["task_status"]
            )
        )
    out["RecordVersion"] = value.get("record_version", 0)
    if "creation_time" in value:
        import aws_sdk_timestream_write.types.date

        out["CreationTime"] = (
            aws_sdk_timestream_write.types.date.serialize_aws_json_1_0(
                value["creation_time"]
            )
        )
    if "last_updated_time" in value:
        import aws_sdk_timestream_write.types.date

        out["LastUpdatedTime"] = (
            aws_sdk_timestream_write.types.date.serialize_aws_json_1_0(
                value["last_updated_time"]
            )
        )
    if "resumable_until" in value:
        import aws_sdk_timestream_write.types.date

        out["ResumableUntil"] = (
            aws_sdk_timestream_write.types.date.serialize_aws_json_1_0(
                value["resumable_until"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchLoadTaskDescription:
    out: BatchLoadTaskDescription = {}  # type: ignore[typeddict-item]
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "DataSourceConfiguration" in data:
        import aws_sdk_timestream_write.types.data_source_configuration

        out["data_source_configuration"] = (
            aws_sdk_timestream_write.types.data_source_configuration.deserialize_aws_json_1_0(
                data["DataSourceConfiguration"]
            )
        )
    if "ProgressReport" in data:
        import aws_sdk_timestream_write.types.batch_load_progress_report

        out["progress_report"] = (
            aws_sdk_timestream_write.types.batch_load_progress_report.deserialize_aws_json_1_0(
                data["ProgressReport"]
            )
        )
    if "ReportConfiguration" in data:
        import aws_sdk_timestream_write.types.report_configuration

        out["report_configuration"] = (
            aws_sdk_timestream_write.types.report_configuration.deserialize_aws_json_1_0(
                data["ReportConfiguration"]
            )
        )
    if "DataModelConfiguration" in data:
        import aws_sdk_timestream_write.types.data_model_configuration

        out["data_model_configuration"] = (
            aws_sdk_timestream_write.types.data_model_configuration.deserialize_aws_json_1_0(
                data["DataModelConfiguration"]
            )
        )
    if "TargetDatabaseName" in data:
        out["target_database_name"] = data["TargetDatabaseName"]
    if "TargetTableName" in data:
        out["target_table_name"] = data["TargetTableName"]
    if "TaskStatus" in data:
        import aws_sdk_timestream_write.types.batch_load_status

        out["task_status"] = (
            aws_sdk_timestream_write.types.batch_load_status.deserialize_aws_json_1_0(
                data["TaskStatus"]
            )
        )
    if "RecordVersion" in data:
        out["record_version"] = data["RecordVersion"]
    else:
        out["record_version"] = 0
    if "CreationTime" in data:
        import aws_sdk_timestream_write.types.date

        out["creation_time"] = (
            aws_sdk_timestream_write.types.date.deserialize_aws_json_1_0(
                data["CreationTime"]
            )
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_timestream_write.types.date

        out["last_updated_time"] = (
            aws_sdk_timestream_write.types.date.deserialize_aws_json_1_0(
                data["LastUpdatedTime"]
            )
        )
    if "ResumableUntil" in data:
        import aws_sdk_timestream_write.types.date

        out["resumable_until"] = (
            aws_sdk_timestream_write.types.date.deserialize_aws_json_1_0(
                data["ResumableUntil"]
            )
        )
    return out
