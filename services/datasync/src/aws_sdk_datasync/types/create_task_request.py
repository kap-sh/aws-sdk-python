"""Generated from Smithy shape ``com.amazonaws.datasync#CreateTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.filter_list
    import aws_sdk_datasync.types.input_tag_list
    import aws_sdk_datasync.types.location_arn
    import aws_sdk_datasync.types.log_group_arn
    import aws_sdk_datasync.types.manifest_config
    import aws_sdk_datasync.types.options
    import aws_sdk_datasync.types.tag_value
    import aws_sdk_datasync.types.task_mode
    import aws_sdk_datasync.types.task_report_config
    import aws_sdk_datasync.types.task_schedule


class CreateTaskRequest(TypedDict, closed=True):
    source_location_arn: "aws_sdk_datasync.types.location_arn.LocationArn"
    """<p>Specifies the ARN of your transfer's source location.</p>"""
    destination_location_arn: "aws_sdk_datasync.types.location_arn.LocationArn"
    """<p>Specifies the ARN of your transfer's destination location. </p>"""
    cloud_watch_log_group_arn: NotRequired[
        "aws_sdk_datasync.types.log_group_arn.LogGroupArn"
    ]
    """<p>Specifies the Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your task.</p> <p>For Enhanced mode tasks, you don't need to specify anything. DataSync automatically sends logs to a CloudWatch log group named <code>/aws/datasync</code>.</p>"""
    name: NotRequired["aws_sdk_datasync.types.tag_value.TagValue"]
    """<p>Specifies the name of your task.</p>"""
    options: NotRequired["aws_sdk_datasync.types.options.Options"]
    """<p>Specifies your task's settings, such as preserving file metadata, verifying data integrity, among other options.</p>"""
    excludes: NotRequired["aws_sdk_datasync.types.filter_list.FilterList"]
    r"""<p>Specifies exclude filters that define the files, objects, and folders in your source location that you don't want DataSync to transfer. For more information and examples, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html\">Specifying what DataSync transfers by using filters</a>.</p>"""
    schedule: NotRequired["aws_sdk_datasync.types.task_schedule.TaskSchedule"]
    r"""<p>Specifies a schedule for when you want your task to run. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html\">Scheduling your task</a>.</p>"""
    tags: NotRequired["aws_sdk_datasync.types.input_tag_list.InputTagList"]
    """<p>Specifies the tags that you want to apply to your task.</p> <p> <i>Tags</i> are key-value pairs that help you manage, filter, and search for your DataSync resources.</p>"""
    includes: NotRequired["aws_sdk_datasync.types.filter_list.FilterList"]
    r"""<p>Specifies include filters that define the files, objects, and folders in your source location that you want DataSync to transfer. For more information and examples, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html\">Specifying what DataSync transfers by using filters</a>.</p>"""
    manifest_config: NotRequired[
        "aws_sdk_datasync.types.manifest_config.ManifestConfig"
    ]
    r"""<p>Configures a manifest, which is a list of files or objects that you want DataSync to transfer. For more information and configuration examples, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html\">Specifying what DataSync transfers by using a manifest</a>.</p> <p>When using this parameter, your caller identity (the role that you're using DataSync with) must have the <code>iam:PassRole</code> permission. The <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess\">AWSDataSyncFullAccess</a> policy includes this permission.</p>"""
    task_report_config: NotRequired[
        "aws_sdk_datasync.types.task_report_config.TaskReportConfig"
    ]
    r"""<p>Specifies how you want to configure a task report, which provides detailed information about your DataSync transfer. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html\">Monitoring your DataSync transfers with task reports</a>.</p> <p>When using this parameter, your caller identity (the role that you're using DataSync with) must have the <code>iam:PassRole</code> permission. The <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess\">AWSDataSyncFullAccess</a> policy includes this permission.</p>"""
    task_mode: NotRequired["aws_sdk_datasync.types.task_mode.TaskMode"]
    r"""<p>Specifies one of the following task modes for your data transfer:</p> <ul> <li> <p> <code>ENHANCED</code> - Transfer virtually unlimited numbers of objects with higher performance than Basic mode. Enhanced mode tasks optimize the data transfer process by listing, preparing, transferring, and verifying data in parallel. Enhanced mode is currently available for transfers between Amazon S3 locations, transfers between Azure Blob and Amazon S3 without an agent, and transfers between other clouds and Amazon S3 without an agent.</p> <note> <p>To create an Enhanced mode task, the IAM role that you use to call the <code>CreateTask</code> operation must have the <code>iam:CreateServiceLinkedRole</code> permission.</p> </note> </li> <li> <p> <code>BASIC</code> (default) - Transfer files or objects between Amazon Web Services storage and all other supported DataSync locations. Basic mode tasks are subject to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/datasync-limits.html\">quotas</a> on the number of files, objects, and directories in a dataset. Basic mode sequentially prepares, transfers, and verifies data, making it slower than Enhanced mode for most workloads.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html#task-mode-differences\">Understanding task mode differences</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTaskRequest) -> dict:
    out: dict = {}
    out["SourceLocationArn"] = value["source_location_arn"]
    out["DestinationLocationArn"] = value["destination_location_arn"]
    if "cloud_watch_log_group_arn" in value:
        out["CloudWatchLogGroupArn"] = value["cloud_watch_log_group_arn"]
    if "name" in value:
        out["Name"] = value["name"]
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
    if "tags" in value:
        import aws_sdk_datasync.types.input_tag_list

        out["Tags"] = aws_sdk_datasync.types.input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
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
    if "task_mode" in value:
        import aws_sdk_datasync.types.task_mode

        out["TaskMode"] = aws_sdk_datasync.types.task_mode.serialize_aws_json_1_1(
            value["task_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTaskRequest:
    out: CreateTaskRequest = {}  # type: ignore[typeddict-item]
    if "SourceLocationArn" in data:
        out["source_location_arn"] = data["SourceLocationArn"]
    else:
        raise DeserializationError("CreateTaskRequest.source_location_arn required")
    if "DestinationLocationArn" in data:
        out["destination_location_arn"] = data["DestinationLocationArn"]
    else:
        raise DeserializationError(
            "CreateTaskRequest.destination_location_arn required"
        )
    if "CloudWatchLogGroupArn" in data:
        out["cloud_watch_log_group_arn"] = data["CloudWatchLogGroupArn"]
    if "Name" in data:
        out["name"] = data["Name"]
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
    if "Tags" in data:
        import aws_sdk_datasync.types.input_tag_list

        out["tags"] = aws_sdk_datasync.types.input_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
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
    if "TaskMode" in data:
        import aws_sdk_datasync.types.task_mode

        out["task_mode"] = aws_sdk_datasync.types.task_mode.deserialize_aws_json_1_1(
            data["TaskMode"]
        )
    return out
