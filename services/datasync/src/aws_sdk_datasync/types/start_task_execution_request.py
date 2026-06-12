"""Generated from Smithy shape ``com.amazonaws.datasync#StartTaskExecutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.filter_list
    import aws_sdk_datasync.types.input_tag_list
    import aws_sdk_datasync.types.manifest_config
    import aws_sdk_datasync.types.options
    import aws_sdk_datasync.types.task_arn
    import aws_sdk_datasync.types.task_report_config


class StartTaskExecutionRequest(TypedDict):
    task_arn: "aws_sdk_datasync.types.task_arn.TaskArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the task that you want to start.</p>"""
    override_options: NotRequired["aws_sdk_datasync.types.options.Options"]
    includes: NotRequired["aws_sdk_datasync.types.filter_list.FilterList"]
    """<p>Specifies a list of filter rules that determines which files to include when running a task. The pattern should contain a single filter string that consists of the patterns to include. The patterns are delimited by \"|\" (that is, a pipe), for example, <code>\"/folder1|/folder2\"</code>. </p>"""
    excludes: NotRequired["aws_sdk_datasync.types.filter_list.FilterList"]
    """<p>Specifies a list of filter rules that determines which files to exclude from a task. The list contains a single filter string that consists of the patterns to exclude. The patterns are delimited by \"|\" (that is, a pipe), for example, <code>\"/folder1|/folder2\"</code>. </p>"""
    manifest_config: NotRequired[
        "aws_sdk_datasync.types.manifest_config.ManifestConfig"
    ]
    """<p>Configures a manifest, which is a list of files or objects that you want DataSync to transfer. For more information and configuration examples, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html\">Specifying what DataSync transfers by using a manifest</a>.</p> <p>When using this parameter, your caller identity (the role that you're using DataSync with) must have the <code>iam:PassRole</code> permission. The <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess\">AWSDataSyncFullAccess</a> policy includes this permission.</p> <p>To remove a manifest configuration, specify this parameter with an empty value.</p>"""
    task_report_config: NotRequired[
        "aws_sdk_datasync.types.task_report_config.TaskReportConfig"
    ]
    """<p>Specifies how you want to configure a task report, which provides detailed information about your DataSync transfer. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html\">Monitoring your DataSync transfers with task reports</a>.</p> <p>When using this parameter, your caller identity (the role that you're using DataSync with) must have the <code>iam:PassRole</code> permission. The <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess\">AWSDataSyncFullAccess</a> policy includes this permission.</p> <p>To remove a task report configuration, specify this parameter as empty.</p>"""
    tags: NotRequired["aws_sdk_datasync.types.input_tag_list.InputTagList"]
    """<p>Specifies the tags that you want to apply to the Amazon Resource Name (ARN) representing the task execution.</p> <p> <i>Tags</i> are key-value pairs that help you manage, filter, and search for your DataSync resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTaskExecutionRequest) -> dict:
    out: dict = {}
    out["TaskArn"] = value["task_arn"]
    if "override_options" in value:
        import aws_sdk_datasync.types.options

        out["OverrideOptions"] = aws_sdk_datasync.types.options.serialize_aws_json_1_1(
            value["override_options"]
        )
    if "includes" in value:
        import aws_sdk_datasync.types.filter_list

        out["Includes"] = aws_sdk_datasync.types.filter_list.serialize_aws_json_1_1(
            value["includes"]
        )
    if "excludes" in value:
        import aws_sdk_datasync.types.filter_list

        out["Excludes"] = aws_sdk_datasync.types.filter_list.serialize_aws_json_1_1(
            value["excludes"]
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
    if "tags" in value:
        import aws_sdk_datasync.types.input_tag_list

        out["Tags"] = aws_sdk_datasync.types.input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTaskExecutionRequest:
    out: StartTaskExecutionRequest = {}  # type: ignore[typeddict-item]
    if "TaskArn" in data:
        out["task_arn"] = data["TaskArn"]
    else:
        raise DeserializationError("StartTaskExecutionRequest.task_arn required")
    if "OverrideOptions" in data:
        import aws_sdk_datasync.types.options

        out["override_options"] = (
            aws_sdk_datasync.types.options.deserialize_aws_json_1_1(
                data["OverrideOptions"]
            )
        )
    if "Includes" in data:
        import aws_sdk_datasync.types.filter_list

        out["includes"] = aws_sdk_datasync.types.filter_list.deserialize_aws_json_1_1(
            data["Includes"]
        )
    if "Excludes" in data:
        import aws_sdk_datasync.types.filter_list

        out["excludes"] = aws_sdk_datasync.types.filter_list.deserialize_aws_json_1_1(
            data["Excludes"]
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
    if "Tags" in data:
        import aws_sdk_datasync.types.input_tag_list

        out["tags"] = aws_sdk_datasync.types.input_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
