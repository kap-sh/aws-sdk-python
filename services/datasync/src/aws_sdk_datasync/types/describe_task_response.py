"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.destination_network_interface_arns
    import aws_sdk_datasync.types.filter_list
    import aws_sdk_datasync.types.location_arn
    import aws_sdk_datasync.types.log_group_arn
    import aws_sdk_datasync.types.manifest_config
    import aws_sdk_datasync.types.options
    import aws_sdk_datasync.types.source_network_interface_arns
    import aws_sdk_datasync.types.string
    import aws_sdk_datasync.types.tag_value
    import aws_sdk_datasync.types.task_arn
    import aws_sdk_datasync.types.task_execution_arn
    import aws_sdk_datasync.types.task_mode
    import aws_sdk_datasync.types.task_report_config
    import aws_sdk_datasync.types.task_schedule
    import aws_sdk_datasync.types.task_schedule_details
    import aws_sdk_datasync.types.task_status
    import aws_sdk_datasync.types.time


class DescribeTaskResponse(TypedDict):
    task_arn: NotRequired["aws_sdk_datasync.types.task_arn.TaskArn"]
    """<p>The ARN of your task.</p>"""
    status: NotRequired["aws_sdk_datasync.types.task_status.TaskStatus"]
    """<p>The status of your task. For information about what each status means, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/create-task-how-to.html#understand-task-creation-statuses\">Task statuses</a>.</p>"""
    name: NotRequired["aws_sdk_datasync.types.tag_value.TagValue"]
    """<p>The name of your task.</p>"""
    current_task_execution_arn: NotRequired[
        "aws_sdk_datasync.types.task_execution_arn.TaskExecutionArn"
    ]
    """<p>The ARN of the most recent task execution.</p>"""
    source_location_arn: NotRequired["aws_sdk_datasync.types.location_arn.LocationArn"]
    """<p>The ARN of your transfer's source location.</p>"""
    destination_location_arn: NotRequired[
        "aws_sdk_datasync.types.location_arn.LocationArn"
    ]
    """<p>The ARN of your transfer's destination location.</p>"""
    cloud_watch_log_group_arn: NotRequired[
        "aws_sdk_datasync.types.log_group_arn.LogGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your task.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/configure-logging.html\">Monitoring data transfers with CloudWatch Logs</a>.</p>"""
    source_network_interface_arns: NotRequired[
        "aws_sdk_datasync.types.source_network_interface_arns.SourceNetworkInterfaceArns"
    ]
    """<p>The ARNs of the <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/datasync-network.html#required-network-interfaces\">network interfaces</a> that DataSync created for your source location.</p>"""
    destination_network_interface_arns: NotRequired[
        "aws_sdk_datasync.types.destination_network_interface_arns.DestinationNetworkInterfaceArns"
    ]
    """<p>The ARNs of the <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/datasync-network.html#required-network-interfaces\">network interfaces</a> that DataSync created for your destination location.</p>"""
    options: NotRequired["aws_sdk_datasync.types.options.Options"]
    """<p>The task's settings. For example, what file metadata gets preserved, how data integrity gets verified at the end of your transfer, bandwidth limits, among other options.</p>"""
    excludes: NotRequired["aws_sdk_datasync.types.filter_list.FilterList"]
    """<p>The exclude filters that define the files, objects, and folders in your source location that you don't want DataSync to transfer. For more information and examples, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html\">Specifying what DataSync transfers by using filters</a>.</p>"""
    schedule: NotRequired["aws_sdk_datasync.types.task_schedule.TaskSchedule"]
    """<p>The schedule for when you want your task to run. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html\">Scheduling your task</a>.</p>"""
    error_code: NotRequired["aws_sdk_datasync.types.string.string"]
    """<p>If there's an issue with your task, you can use the error code to help you troubleshoot the problem. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html\">Troubleshooting issues with DataSync transfers</a>.</p>"""
    error_detail: NotRequired["aws_sdk_datasync.types.string.string"]
    """<p>If there's an issue with your task, you can use the error details to help you troubleshoot the problem. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html\">Troubleshooting issues with DataSync transfers</a>.</p>"""
    creation_time: NotRequired["aws_sdk_datasync.types.time.Time"]
    """<p>The time that the task was created.</p>"""
    includes: NotRequired["aws_sdk_datasync.types.filter_list.FilterList"]
    """<p>The include filters that define the files, objects, and folders in your source location that you want DataSync to transfer. For more information and examples, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html\">Specifying what DataSync transfers by using filters</a>.</p>"""
    manifest_config: NotRequired[
        "aws_sdk_datasync.types.manifest_config.ManifestConfig"
    ]
    """<p>The configuration of the manifest that lists the files or objects that you want DataSync to transfer. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html\">Specifying what DataSync transfers by using a manifest</a>.</p>"""
    task_report_config: NotRequired[
        "aws_sdk_datasync.types.task_report_config.TaskReportConfig"
    ]
    """<p>The configuration of your task report, which provides detailed information about your DataSync transfer. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html\">Monitoring your DataSync transfers with task reports</a>.</p>"""
    schedule_details: NotRequired[
        "aws_sdk_datasync.types.task_schedule_details.TaskScheduleDetails"
    ]
    """<p>The details about your <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html\">task schedule</a>.</p>"""
    task_mode: NotRequired["aws_sdk_datasync.types.task_mode.TaskMode"]
    """<p>The task mode that you're using. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Choosing a task mode for your data transfer</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTaskResponse) -> dict:
    out: dict = {}
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "status" in value:
        import aws_sdk_datasync.types.task_status

        out["Status"] = aws_sdk_datasync.types.task_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "current_task_execution_arn" in value:
        out["CurrentTaskExecutionArn"] = value["current_task_execution_arn"]
    if "source_location_arn" in value:
        out["SourceLocationArn"] = value["source_location_arn"]
    if "destination_location_arn" in value:
        out["DestinationLocationArn"] = value["destination_location_arn"]
    if "cloud_watch_log_group_arn" in value:
        out["CloudWatchLogGroupArn"] = value["cloud_watch_log_group_arn"]
    if "source_network_interface_arns" in value:
        import aws_sdk_datasync.types.source_network_interface_arns

        out["SourceNetworkInterfaceArns"] = (
            aws_sdk_datasync.types.source_network_interface_arns.serialize_aws_json_1_1(
                value["source_network_interface_arns"]
            )
        )
    if "destination_network_interface_arns" in value:
        import aws_sdk_datasync.types.destination_network_interface_arns

        out["DestinationNetworkInterfaceArns"] = (
            aws_sdk_datasync.types.destination_network_interface_arns.serialize_aws_json_1_1(
                value["destination_network_interface_arns"]
            )
        )
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
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_detail" in value:
        out["ErrorDetail"] = value["error_detail"]
    if "creation_time" in value:
        import aws_sdk_datasync.types.time

        out["CreationTime"] = aws_sdk_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
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
    if "schedule_details" in value:
        import aws_sdk_datasync.types.task_schedule_details

        out["ScheduleDetails"] = (
            aws_sdk_datasync.types.task_schedule_details.serialize_aws_json_1_1(
                value["schedule_details"]
            )
        )
    if "task_mode" in value:
        import aws_sdk_datasync.types.task_mode

        out["TaskMode"] = aws_sdk_datasync.types.task_mode.serialize_aws_json_1_1(
            value["task_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTaskResponse:
    out: DescribeTaskResponse = {}  # type: ignore[typeddict-item]
    if "TaskArn" in data:
        out["task_arn"] = data["TaskArn"]
    if "Status" in data:
        import aws_sdk_datasync.types.task_status

        out["status"] = aws_sdk_datasync.types.task_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "CurrentTaskExecutionArn" in data:
        out["current_task_execution_arn"] = data["CurrentTaskExecutionArn"]
    if "SourceLocationArn" in data:
        out["source_location_arn"] = data["SourceLocationArn"]
    if "DestinationLocationArn" in data:
        out["destination_location_arn"] = data["DestinationLocationArn"]
    if "CloudWatchLogGroupArn" in data:
        out["cloud_watch_log_group_arn"] = data["CloudWatchLogGroupArn"]
    if "SourceNetworkInterfaceArns" in data:
        import aws_sdk_datasync.types.source_network_interface_arns

        out["source_network_interface_arns"] = (
            aws_sdk_datasync.types.source_network_interface_arns.deserialize_aws_json_1_1(
                data["SourceNetworkInterfaceArns"]
            )
        )
    if "DestinationNetworkInterfaceArns" in data:
        import aws_sdk_datasync.types.destination_network_interface_arns

        out["destination_network_interface_arns"] = (
            aws_sdk_datasync.types.destination_network_interface_arns.deserialize_aws_json_1_1(
                data["DestinationNetworkInterfaceArns"]
            )
        )
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
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorDetail" in data:
        out["error_detail"] = data["ErrorDetail"]
    if "CreationTime" in data:
        import aws_sdk_datasync.types.time

        out["creation_time"] = aws_sdk_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
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
    if "ScheduleDetails" in data:
        import aws_sdk_datasync.types.task_schedule_details

        out["schedule_details"] = (
            aws_sdk_datasync.types.task_schedule_details.deserialize_aws_json_1_1(
                data["ScheduleDetails"]
            )
        )
    if "TaskMode" in data:
        import aws_sdk_datasync.types.task_mode

        out["task_mode"] = aws_sdk_datasync.types.task_mode.deserialize_aws_json_1_1(
            data["TaskMode"]
        )
    return out
