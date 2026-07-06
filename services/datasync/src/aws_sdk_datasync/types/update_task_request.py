"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.filter_list
    import aws_sdk_datasync.types.log_group_arn
    import aws_sdk_datasync.types.manifest_config
    import aws_sdk_datasync.types.options
    import aws_sdk_datasync.types.tag_value
    import aws_sdk_datasync.types.task_arn
    import aws_sdk_datasync.types.task_report_config
    import aws_sdk_datasync.types.task_schedule


class UpdateTaskRequest(TypedDict, closed=True):
    task_arn: "aws_sdk_datasync.types.task_arn.TaskArn"
    """<p>Specifies the ARN of the task that you want to update.</p>"""
    options: NotRequired["aws_sdk_datasync.types.options.Options"]
    excludes: NotRequired["aws_sdk_datasync.types.filter_list.FilterList"]
    r"""<p>Specifies exclude filters that define the files, objects, and folders in your source location that you don't want DataSync to transfer. For more information and examples, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html\">Specifying what DataSync transfers by using filters</a>.</p>"""
    schedule: NotRequired["aws_sdk_datasync.types.task_schedule.TaskSchedule"]
    r"""<p>Specifies a schedule for when you want your task to run. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html\">Scheduling your task</a>.</p>"""
    name: NotRequired["aws_sdk_datasync.types.tag_value.TagValue"]
    """<p>Specifies the name of your task.</p>"""
    cloud_watch_log_group_arn: NotRequired[
        "aws_sdk_datasync.types.log_group_arn.LogGroupArn"
    ]
    r"""<p>Specifies the Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your task.</p> <p>For Enhanced mode tasks, you must use <code>/aws/datasync</code> as your log group name. For example:</p> <p> <code>arn:aws:logs:us-east-1:111222333444:log-group:/aws/datasync:*</code> </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/configure-logging.html\">Monitoring data transfers with CloudWatch Logs</a>.</p>"""
    includes: NotRequired["aws_sdk_datasync.types.filter_list.FilterList"]
    r"""<p>Specifies include filters define the files, objects, and folders in your source location that you want DataSync to transfer. For more information and examples, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html\">Specifying what DataSync transfers by using filters</a>.</p>"""
    manifest_config: NotRequired[
        "aws_sdk_datasync.types.manifest_config.ManifestConfig"
    ]
    r"""<p>Configures a manifest, which is a list of files or objects that you want DataSync to transfer. For more information and configuration examples, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html\">Specifying what DataSync transfers by using a manifest</a>.</p> <p>When using this parameter, your caller identity (the IAM role that you're using DataSync with) must have the <code>iam:PassRole</code> permission. The <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess\">AWSDataSyncFullAccess</a> policy includes this permission.</p> <p>To remove a manifest configuration, specify this parameter as empty.</p>"""
    task_report_config: NotRequired[
        "aws_sdk_datasync.types.task_report_config.TaskReportConfig"
    ]
    r"""<p>Specifies how you want to configure a task report, which provides detailed information about your DataSync transfer. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html\">Monitoring your DataSync transfers with task reports</a>.</p> <p>When using this parameter, your caller identity (the IAM role that you're using DataSync with) must have the <code>iam:PassRole</code> permission. The <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess\">AWSDataSyncFullAccess</a> policy includes this permission.</p> <p>To remove a task report configuration, specify this parameter as empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTaskRequest) -> dict:
    out: dict = {}
    out["TaskArn"] = value["task_arn"]
    if "options" in value:
        import aws_sdk_datasync.types.options

        out["Options"] = aws_sdk_datasync.types.options.serialize_aws_json_1_1(
            value["options"]
        )
    if "excludes" in value:
        import aws_sdk_datasync.types.filter_list

        out["Excludes"] = aws_sdk_datasync.types.filter_list.serialize_aws_json_1_1(
            value["excludes"]
        )
    if "schedule" in value:
        import aws_sdk_datasync.types.task_schedule

        out["Schedule"] = aws_sdk_datasync.types.task_schedule.serialize_aws_json_1_1(
            value["schedule"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "cloud_watch_log_group_arn" in value:
        out["CloudWatchLogGroupArn"] = value["cloud_watch_log_group_arn"]
    if "includes" in value:
        import aws_sdk_datasync.types.filter_list

        out["Includes"] = aws_sdk_datasync.types.filter_list.serialize_aws_json_1_1(
            value["includes"]
        )
    if "manifest_config" in value:
        import aws_sdk_datasync.types.manifest_config

        out["ManifestConfig"] = (
            aws_sdk_datasync.types.manifest_config.serialize_aws_json_1_1(
                value["manifest_config"]
            )
        )
    if "task_report_config" in value:
        import aws_sdk_datasync.types.task_report_config

        out["TaskReportConfig"] = (
            aws_sdk_datasync.types.task_report_config.serialize_aws_json_1_1(
                value["task_report_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTaskRequest:
    out: UpdateTaskRequest = {}  # type: ignore[typeddict-item]
    if "TaskArn" in data:
        out["task_arn"] = data["TaskArn"]
    else:
        raise DeserializationError("UpdateTaskRequest.task_arn required")
    if "Options" in data:
        import aws_sdk_datasync.types.options

        out["options"] = aws_sdk_datasync.types.options.deserialize_aws_json_1_1(
            data["Options"]
        )
    if "Excludes" in data:
        import aws_sdk_datasync.types.filter_list

        out["excludes"] = aws_sdk_datasync.types.filter_list.deserialize_aws_json_1_1(
            data["Excludes"]
        )
    if "Schedule" in data:
        import aws_sdk_datasync.types.task_schedule

        out["schedule"] = aws_sdk_datasync.types.task_schedule.deserialize_aws_json_1_1(
            data["Schedule"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "CloudWatchLogGroupArn" in data:
        out["cloud_watch_log_group_arn"] = data["CloudWatchLogGroupArn"]
    if "Includes" in data:
        import aws_sdk_datasync.types.filter_list

        out["includes"] = aws_sdk_datasync.types.filter_list.deserialize_aws_json_1_1(
            data["Includes"]
        )
    if "ManifestConfig" in data:
        import aws_sdk_datasync.types.manifest_config

        out["manifest_config"] = (
            aws_sdk_datasync.types.manifest_config.deserialize_aws_json_1_1(
                data["ManifestConfig"]
            )
        )
    if "TaskReportConfig" in data:
        import aws_sdk_datasync.types.task_report_config

        out["task_report_config"] = (
            aws_sdk_datasync.types.task_report_config.deserialize_aws_json_1_1(
                data["TaskReportConfig"]
            )
        )
    return out
