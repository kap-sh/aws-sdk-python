"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#BatchLoadTaskDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.batch_load_progress_report
    import capo_timestream_write.types.batch_load_status
    import capo_timestream_write.types.batch_load_task_id
    import capo_timestream_write.types.data_model_configuration
    import capo_timestream_write.types.data_source_configuration
    import capo_timestream_write.types.date
    import capo_timestream_write.types.record_version
    import capo_timestream_write.types.report_configuration
    import capo_timestream_write.types.resource_name
    import capo_timestream_write.types.string_value2048


class BatchLoadTaskDescription(TypedDict, closed=True):
    task_id: NotRequired[
        "capo_timestream_write.types.batch_load_task_id.BatchLoadTaskId"
    ]
    """<p>The ID of the batch load task.</p>"""
    error_message: NotRequired[
        "capo_timestream_write.types.string_value2048.StringValue2048"
    ]
    """<p></p>"""
    data_source_configuration: NotRequired[
        "capo_timestream_write.types.data_source_configuration.DataSourceConfiguration"
    ]
    """<p>Configuration details about the data source for a batch load task.</p>"""
    progress_report: NotRequired[
        "capo_timestream_write.types.batch_load_progress_report.BatchLoadProgressReport"
    ]
    """<p></p>"""
    report_configuration: NotRequired[
        "capo_timestream_write.types.report_configuration.ReportConfiguration"
    ]
    """<p>Report configuration for a batch load task. This contains details about where error reports are stored.</p>"""
    data_model_configuration: NotRequired[
        "capo_timestream_write.types.data_model_configuration.DataModelConfiguration"
    ]
    """<p>Data model configuration for a batch load task. This contains details about where a data model for a batch load task is stored.</p>"""
    target_database_name: NotRequired[
        "capo_timestream_write.types.resource_name.ResourceName"
    ]
    """<p></p>"""
    target_table_name: NotRequired[
        "capo_timestream_write.types.resource_name.ResourceName"
    ]
    """<p></p>"""
    task_status: NotRequired[
        "capo_timestream_write.types.batch_load_status.BatchLoadStatus"
    ]
    """<p>Status of the batch load task.</p>"""
    record_version: "capo_timestream_write.types.record_version.RecordVersion"
    """<p></p>"""
    creation_time: NotRequired["capo_timestream_write.types.date.Date"]
    """<p>The time when the Timestream batch load task was created.</p>"""
    last_updated_time: NotRequired["capo_timestream_write.types.date.Date"]
    """<p>The time when the Timestream batch load task was last updated.</p>"""
    resumable_until: NotRequired["capo_timestream_write.types.date.Date"]
    """<p> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchLoadTaskDescription) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "data_source_configuration" in value:
        import capo_timestream_write.types.data_source_configuration

        out["DataSourceConfiguration"] = (
            capo_timestream_write.types.data_source_configuration.serialize_aws_json_1_0(
                value["data_source_configuration"]
            )
        )
    if "progress_report" in value:
        import capo_timestream_write.types.batch_load_progress_report

        out["ProgressReport"] = (
            capo_timestream_write.types.batch_load_progress_report.serialize_aws_json_1_0(
                value["progress_report"]
            )
        )
    if "report_configuration" in value:
        import capo_timestream_write.types.report_configuration

        out["ReportConfiguration"] = (
            capo_timestream_write.types.report_configuration.serialize_aws_json_1_0(
                value["report_configuration"]
            )
        )
    if "data_model_configuration" in value:
        import capo_timestream_write.types.data_model_configuration

        out["DataModelConfiguration"] = (
            capo_timestream_write.types.data_model_configuration.serialize_aws_json_1_0(
                value["data_model_configuration"]
            )
        )
    if "target_database_name" in value:
        out["TargetDatabaseName"] = value["target_database_name"]
    if "target_table_name" in value:
        out["TargetTableName"] = value["target_table_name"]
    if "task_status" in value:
        import capo_timestream_write.types.batch_load_status

        out["TaskStatus"] = (
            capo_timestream_write.types.batch_load_status.serialize_aws_json_1_0(
                value["task_status"]
            )
        )
    out["RecordVersion"] = value.get("record_version", 0)
    if "creation_time" in value:
        import capo_timestream_write.types.date

        out["CreationTime"] = capo_timestream_write.types.date.serialize_aws_json_1_0(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import capo_timestream_write.types.date

        out["LastUpdatedTime"] = (
            capo_timestream_write.types.date.serialize_aws_json_1_0(
                value["last_updated_time"]
            )
        )
    if "resumable_until" in value:
        import capo_timestream_write.types.date

        out["ResumableUntil"] = capo_timestream_write.types.date.serialize_aws_json_1_0(
            value["resumable_until"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchLoadTaskDescription:
    out: BatchLoadTaskDescription = {}  # type: ignore[typeddict-item]
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "DataSourceConfiguration" in data:
        import capo_timestream_write.types.data_source_configuration

        out["data_source_configuration"] = (
            capo_timestream_write.types.data_source_configuration.deserialize_aws_json_1_0(
                data["DataSourceConfiguration"]
            )
        )
    if "ProgressReport" in data:
        import capo_timestream_write.types.batch_load_progress_report

        out["progress_report"] = (
            capo_timestream_write.types.batch_load_progress_report.deserialize_aws_json_1_0(
                data["ProgressReport"]
            )
        )
    if "ReportConfiguration" in data:
        import capo_timestream_write.types.report_configuration

        out["report_configuration"] = (
            capo_timestream_write.types.report_configuration.deserialize_aws_json_1_0(
                data["ReportConfiguration"]
            )
        )
    if "DataModelConfiguration" in data:
        import capo_timestream_write.types.data_model_configuration

        out["data_model_configuration"] = (
            capo_timestream_write.types.data_model_configuration.deserialize_aws_json_1_0(
                data["DataModelConfiguration"]
            )
        )
    if "TargetDatabaseName" in data:
        out["target_database_name"] = data["TargetDatabaseName"]
    if "TargetTableName" in data:
        out["target_table_name"] = data["TargetTableName"]
    if "TaskStatus" in data:
        import capo_timestream_write.types.batch_load_status

        out["task_status"] = (
            capo_timestream_write.types.batch_load_status.deserialize_aws_json_1_0(
                data["TaskStatus"]
            )
        )
    if "RecordVersion" in data:
        out["record_version"] = data["RecordVersion"]
    else:
        out["record_version"] = 0
    if "CreationTime" in data:
        import capo_timestream_write.types.date

        out["creation_time"] = (
            capo_timestream_write.types.date.deserialize_aws_json_1_0(
                data["CreationTime"]
            )
        )
    if "LastUpdatedTime" in data:
        import capo_timestream_write.types.date

        out["last_updated_time"] = (
            capo_timestream_write.types.date.deserialize_aws_json_1_0(
                data["LastUpdatedTime"]
            )
        )
    if "ResumableUntil" in data:
        import capo_timestream_write.types.date

        out["resumable_until"] = (
            capo_timestream_write.types.date.deserialize_aws_json_1_0(
                data["ResumableUntil"]
            )
        )
    return out
