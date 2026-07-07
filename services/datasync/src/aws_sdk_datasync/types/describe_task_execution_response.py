"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeTaskExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datasync.types.filter_list
    import aws_sdk_datasync.types.item_count
    import aws_sdk_datasync.types.long
    import aws_sdk_datasync.types.manifest_config
    import aws_sdk_datasync.types.options
    import aws_sdk_datasync.types.report_result
    import aws_sdk_datasync.types.task_execution_arn
    import aws_sdk_datasync.types.task_execution_files_failed_detail
    import aws_sdk_datasync.types.task_execution_files_listed_detail
    import aws_sdk_datasync.types.task_execution_folders_failed_detail
    import aws_sdk_datasync.types.task_execution_folders_listed_detail
    import aws_sdk_datasync.types.task_execution_result_detail
    import aws_sdk_datasync.types.task_execution_status
    import aws_sdk_datasync.types.task_mode
    import aws_sdk_datasync.types.task_report_config
    import aws_sdk_datasync.types.time


class DescribeTaskExecutionResponse(TypedDict, closed=True):
    task_execution_arn: NotRequired[
        "aws_sdk_datasync.types.task_execution_arn.TaskExecutionArn"
    ]
    """<p>The ARN of the task execution that you wanted information about. <code>TaskExecutionArn</code> is hierarchical and includes <code>TaskArn</code> for the task that was executed. </p> <p>For example, a <code>TaskExecution</code> value with the ARN <code>arn:aws:datasync:us-east-1:111222333444:task/task-0208075f79cedf4a2/execution/exec-08ef1e88ec491019b</code> executed the task with the ARN <code>arn:aws:datasync:us-east-1:111222333444:task/task-0208075f79cedf4a2</code>. </p>"""
    status: NotRequired[
        "aws_sdk_datasync.types.task_execution_status.TaskExecutionStatus"
    ]
    """<p>The status of the task execution. </p>"""
    options: NotRequired["aws_sdk_datasync.types.options.Options"]
    excludes: NotRequired["aws_sdk_datasync.types.filter_list.FilterList"]
    r"""<p>A list of filter rules that exclude specific data during your transfer. For more information and examples, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html\">Filtering data transferred by DataSync</a>.</p>"""
    includes: NotRequired["aws_sdk_datasync.types.filter_list.FilterList"]
    r"""<p>A list of filter rules that include specific data during your transfer. For more information and examples, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html\">Filtering data transferred by DataSync</a>.</p>"""
    manifest_config: NotRequired[
        "aws_sdk_datasync.types.manifest_config.ManifestConfig"
    ]
    r"""<p>The configuration of the manifest that lists the files or objects to transfer. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html\">Specifying what DataSync transfers by using a manifest</a>.</p>"""
    start_time: NotRequired["aws_sdk_datasync.types.time.Time"]
    """<p>The time that DataSync sends the request to start the task execution. For non-queued tasks, <code>LaunchTime</code> and <code>StartTime</code> are typically the same. For queued tasks, <code>LaunchTime</code> is typically later than <code>StartTime</code> because previously queued tasks must finish running before newer tasks can begin.</p>"""
    estimated_files_to_transfer: "aws_sdk_datasync.types.long.long"
    r"""<p>The number of files, objects, and directories that DataSync expects to transfer over the network. This value is calculated while DataSync <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses\">prepares</a> the transfer.</p> <p>How this gets calculated depends primarily on your task’s <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-TransferMode\">transfer mode</a> configuration:</p> <ul> <li> <p>If <code>TranserMode</code> is set to <code>CHANGED</code> - The calculation is based on comparing the content of the source and destination locations and determining the difference that needs to be transferred. The difference can include:</p> <ul> <li> <p>Anything that's added or modified at the source location.</p> </li> <li> <p>Anything that's in both locations and modified at the destination after an initial transfer (unless <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-OverwriteMode\">OverwriteMode</a> is set to <code>NEVER</code>).</p> </li> <li> <p> <b>(Basic task mode only)</b> The number of items that DataSync expects to delete (if <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-PreserveDeletedFiles\">PreserveDeletedFiles</a> is set to <code>REMOVE</code>).</p> </li> </ul> </li> <li> <p>If <code>TranserMode</code> is set to <code>ALL</code> - The calculation is based only on the items that DataSync finds at the source location.</p> </li> </ul> <note> <p>For <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>, this counter only includes files or objects. Directories are counted in <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-EstimatedFoldersToTransfer\">EstimatedFoldersToTransfer</a>. </p> </note>"""
    estimated_bytes_to_transfer: "aws_sdk_datasync.types.long.long"
    """<p>The number of logical bytes that DataSync expects to write to the destination location.</p>"""
    files_transferred: "aws_sdk_datasync.types.long.long"
    r"""<p>The number of files, objects, and directories that DataSync actually transfers over the network. This value is updated periodically during your task execution when something is read from the source and sent over the network.</p> <p>If DataSync fails to transfer something, this value can be less than <code>EstimatedFilesToTransfer</code>. In some cases, this value can also be greater than <code>EstimatedFilesToTransfer</code>. This element is implementation-specific for some location types, so don't use it as an exact indication of what's transferring or to monitor your task execution.</p> <note> <p>For <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>, this counter only includes files or objects. Directories are counted in <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-FoldersTransferred\">FoldersTransferred</a>. </p> </note>"""
    bytes_written: "aws_sdk_datasync.types.long.long"
    """<p>The number of logical bytes that DataSync actually writes to the destination location.</p>"""
    bytes_transferred: "aws_sdk_datasync.types.long.long"
    r"""<p>The number of bytes that DataSync sends to the network before compression (if compression is possible). For the number of bytes transferred over the network, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-BytesCompressed\">BytesCompressed</a>. </p>"""
    bytes_compressed: "aws_sdk_datasync.types.long.long"
    r"""<p>The number of physical bytes that DataSync transfers over the network after compression (if compression is possible). This number is typically less than <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-BytesTransferred\">BytesTransferred</a> unless the data isn't compressible.</p>"""
    result: NotRequired[
        "aws_sdk_datasync.types.task_execution_result_detail.TaskExecutionResultDetail"
    ]
    """<p>The result of the task execution.</p>"""
    task_report_config: NotRequired[
        "aws_sdk_datasync.types.task_report_config.TaskReportConfig"
    ]
    r"""<p>The configuration of your task report, which provides detailed information about for your DataSync transfer. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html\">Creating a task report</a>.</p>"""
    files_deleted: "aws_sdk_datasync.types.long.long"
    r"""<p>The number of files, objects, and directories that DataSync actually deletes in your destination location. If you don't configure your task to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html\">delete data in the destination that isn't in the source</a>, the value is always <code>0</code>.</p> <note> <p>For <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>, this counter only includes files or objects. Directories are counted in <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-FoldersDeleted\">FoldersDeleted</a>. </p> </note>"""
    files_skipped: "aws_sdk_datasync.types.long.long"
    r"""<p>The number of files, objects, and directories that DataSync skips during your transfer.</p> <note> <p>For <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>, this counter only includes files or objects. Directories are counted in <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-FoldersSkipped\">FoldersSkipped</a>. </p> </note>"""
    files_verified: "aws_sdk_datasync.types.long.long"
    r"""<p>The number of files, objects, and directories that DataSync verifies during your transfer.</p> <note> <p>When you configure your task to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/configure-data-verification-options.html\">verify only the data that's transferred</a>, DataSync doesn't verify directories in some situations or files that fail to transfer.</p> <p>For <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>, this counter only includes files or objects. Directories are counted in <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-FoldersVerified\">FoldersVerified</a>. </p> </note>"""
    report_result: NotRequired["aws_sdk_datasync.types.report_result.ReportResult"]
    r"""<p>Indicates whether DataSync generated a complete <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html\">task report</a> for your transfer.</p>"""
    estimated_files_to_delete: "aws_sdk_datasync.types.long.long"
    r"""<p>The number of files, objects, and directories that DataSync expects to delete in your destination location. If you don't configure your task to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html\">delete data in the destination that isn't in the source</a>, the value is always <code>0</code>.</p> <note> <p>For <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>, this counter only includes files or objects. Directories are counted in <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-EstimatedFoldersToDelete\">EstimatedFoldersToDelete</a>. </p> </note>"""
    task_mode: NotRequired["aws_sdk_datasync.types.task_mode.TaskMode"]
    r"""<p>The task mode that you're using. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Choosing a task mode for your data transfer</a>.</p>"""
    files_prepared: "aws_sdk_datasync.types.long.long"
    r"""<p>The number of files or objects that DataSync will attempt to transfer after comparing your source and destination locations.</p> <note> <p>Applies only to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>.</p> </note> <p>This counter isn't applicable if you configure your task to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html#task-option-transfer-mode\">transfer all data</a>. In that scenario, DataSync copies everything from the source to the destination without comparing differences between the locations.</p>"""
    files_listed: NotRequired[
        "aws_sdk_datasync.types.task_execution_files_listed_detail.TaskExecutionFilesListedDetail"
    ]
    r"""<p>The number of files or objects that DataSync finds at your locations.</p> <note> <p>Applies only to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>.</p> </note>"""
    files_failed: NotRequired[
        "aws_sdk_datasync.types.task_execution_files_failed_detail.TaskExecutionFilesFailedDetail"
    ]
    r"""<p>The number of files or objects that DataSync fails to prepare, transfer, verify, and delete during your task execution.</p> <note> <p>Applies only to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>.</p> </note>"""
    estimated_folders_to_delete: NotRequired[
        "aws_sdk_datasync.types.item_count.ItemCount"
    ]
    r"""<p>The number of directories that DataSync expects to delete in your destination location. If you don't configure your task to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html\">delete data in the destination that isn't in the source</a>, the value is always <code>0</code>.</p> <note> <p>Applies only to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>.</p> </note>"""
    estimated_folders_to_transfer: NotRequired[
        "aws_sdk_datasync.types.item_count.ItemCount"
    ]
    r"""<p>The number of directories that DataSync expects to transfer over the network. This value is calculated as DataSync <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses\">prepares</a> directories to transfer.</p> <p>How this gets calculated depends primarily on your task’s <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-TransferMode\">transfer mode</a> configuration:</p> <ul> <li> <p>If <code>TranserMode</code> is set to <code>CHANGED</code> - The calculation is based on comparing the content of the source and destination locations and determining the difference that needs to be transferred. The difference can include:</p> <ul> <li> <p>Anything that's added or modified at the source location.</p> </li> <li> <p>Anything that's in both locations and modified at the destination after an initial transfer (unless <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-OverwriteMode\">OverwriteMode</a> is set to <code>NEVER</code>).</p> </li> </ul> </li> <li> <p>If <code>TranserMode</code> is set to <code>ALL</code> - The calculation is based only on the items that DataSync finds at the source location.</p> </li> </ul> <note> <p>Applies only to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>.</p> </note>"""
    folders_skipped: NotRequired["aws_sdk_datasync.types.item_count.ItemCount"]
    r"""<p>The number of directories that DataSync skips during your transfer.</p> <note> <p>Applies only to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>.</p> </note>"""
    folders_prepared: NotRequired["aws_sdk_datasync.types.item_count.ItemCount"]
    r"""<p>The number of directories that DataSync will attempt to transfer after comparing your source and destination locations.</p> <note> <p>Applies only to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>.</p> </note> <p>This counter isn't applicable if you configure your task to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html#task-option-transfer-mode\">transfer all data</a>. In that scenario, DataSync copies everything from the source to the destination without comparing differences between the locations.</p>"""
    folders_transferred: NotRequired["aws_sdk_datasync.types.item_count.ItemCount"]
    r"""<p>The number of directories that DataSync actually transfers over the network. This value is updated periodically during your task execution when something is read from the source and sent over the network.</p> <p>If DataSync fails to transfer something, this value can be less than <code>EstimatedFoldersToTransfer</code>. In some cases, this value can also be greater than <code>EstimatedFoldersToTransfer</code>. </p> <note> <p>Applies only to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>.</p> </note>"""
    folders_verified: NotRequired["aws_sdk_datasync.types.item_count.ItemCount"]
    r"""<p>The number of directories that DataSync verifies during your transfer.</p> <note> <p>Applies only to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>.</p> </note>"""
    folders_deleted: NotRequired["aws_sdk_datasync.types.item_count.ItemCount"]
    r"""<p>The number of directories that DataSync actually deletes in your destination location. If you don't configure your task to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html\">delete data in the destination that isn't in the source</a>, the value is always <code>0</code>.</p> <note> <p>Applies only to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>.</p> </note>"""
    folders_listed: NotRequired[
        "aws_sdk_datasync.types.task_execution_folders_listed_detail.TaskExecutionFoldersListedDetail"
    ]
    r"""<p>The number of directories that DataSync finds at your locations.</p> <note> <p>Applies only to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>.</p> </note>"""
    folders_failed: NotRequired[
        "aws_sdk_datasync.types.task_execution_folders_failed_detail.TaskExecutionFoldersFailedDetail"
    ]
    r"""<p>The number of directories that DataSync fails to list, prepare, transfer, verify, and delete during your task execution.</p> <note> <p>Applies only to <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Enhanced mode tasks</a>.</p> </note>"""
    launch_time: NotRequired["aws_sdk_datasync.types.time.Time"]
    """<p>The time that the task execution actually begins. For non-queued tasks, <code>LaunchTime</code> and <code>StartTime</code> are typically the same. For queued tasks, <code>LaunchTime</code> is typically later than <code>StartTime</code> because previously queued tasks must finish running before newer tasks can begin.</p>"""
    end_time: NotRequired["aws_sdk_datasync.types.time.Time"]
    """<p>The time that the transfer task ends.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTaskExecutionResponse) -> dict:
    out: dict = {}
    if "task_execution_arn" in value:
        out["TaskExecutionArn"] = value["task_execution_arn"]
    if "status" in value:
        import aws_sdk_datasync.types.task_execution_status

        out["Status"] = (
            aws_sdk_datasync.types.task_execution_status.serialize_aws_json_1_1(
                value["status"]
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
    if "start_time" in value:
        import aws_sdk_datasync.types.time

        out["StartTime"] = aws_sdk_datasync.types.time.serialize_aws_json_1_1(
            value["start_time"]
        )
    out["EstimatedFilesToTransfer"] = value.get("estimated_files_to_transfer", 0)
    out["EstimatedBytesToTransfer"] = value.get("estimated_bytes_to_transfer", 0)
    out["FilesTransferred"] = value.get("files_transferred", 0)
    out["BytesWritten"] = value.get("bytes_written", 0)
    out["BytesTransferred"] = value.get("bytes_transferred", 0)
    out["BytesCompressed"] = value.get("bytes_compressed", 0)
    if "result" in value:
        import aws_sdk_datasync.types.task_execution_result_detail

        out["Result"] = (
            aws_sdk_datasync.types.task_execution_result_detail.serialize_aws_json_1_1(
                value["result"]
            )
        )
    if "task_report_config" in value:
        import aws_sdk_datasync.types.task_report_config

        out["TaskReportConfig"] = (
            aws_sdk_datasync.types.task_report_config.serialize_aws_json_1_1(
                value["task_report_config"]
            )
        )
    out["FilesDeleted"] = value.get("files_deleted", 0)
    out["FilesSkipped"] = value.get("files_skipped", 0)
    out["FilesVerified"] = value.get("files_verified", 0)
    if "report_result" in value:
        import aws_sdk_datasync.types.report_result

        out["ReportResult"] = (
            aws_sdk_datasync.types.report_result.serialize_aws_json_1_1(
                value["report_result"]
            )
        )
    out["EstimatedFilesToDelete"] = value.get("estimated_files_to_delete", 0)
    if "task_mode" in value:
        import aws_sdk_datasync.types.task_mode

        out["TaskMode"] = aws_sdk_datasync.types.task_mode.serialize_aws_json_1_1(
            value["task_mode"]
        )
    out["FilesPrepared"] = value.get("files_prepared", 0)
    if "files_listed" in value:
        import aws_sdk_datasync.types.task_execution_files_listed_detail

        out["FilesListed"] = (
            aws_sdk_datasync.types.task_execution_files_listed_detail.serialize_aws_json_1_1(
                value["files_listed"]
            )
        )
    if "files_failed" in value:
        import aws_sdk_datasync.types.task_execution_files_failed_detail

        out["FilesFailed"] = (
            aws_sdk_datasync.types.task_execution_files_failed_detail.serialize_aws_json_1_1(
                value["files_failed"]
            )
        )
    if "estimated_folders_to_delete" in value:
        out["EstimatedFoldersToDelete"] = value["estimated_folders_to_delete"]
    if "estimated_folders_to_transfer" in value:
        out["EstimatedFoldersToTransfer"] = value["estimated_folders_to_transfer"]
    if "folders_skipped" in value:
        out["FoldersSkipped"] = value["folders_skipped"]
    if "folders_prepared" in value:
        out["FoldersPrepared"] = value["folders_prepared"]
    if "folders_transferred" in value:
        out["FoldersTransferred"] = value["folders_transferred"]
    if "folders_verified" in value:
        out["FoldersVerified"] = value["folders_verified"]
    if "folders_deleted" in value:
        out["FoldersDeleted"] = value["folders_deleted"]
    if "folders_listed" in value:
        import aws_sdk_datasync.types.task_execution_folders_listed_detail

        out["FoldersListed"] = (
            aws_sdk_datasync.types.task_execution_folders_listed_detail.serialize_aws_json_1_1(
                value["folders_listed"]
            )
        )
    if "folders_failed" in value:
        import aws_sdk_datasync.types.task_execution_folders_failed_detail

        out["FoldersFailed"] = (
            aws_sdk_datasync.types.task_execution_folders_failed_detail.serialize_aws_json_1_1(
                value["folders_failed"]
            )
        )
    if "launch_time" in value:
        import aws_sdk_datasync.types.time

        out["LaunchTime"] = aws_sdk_datasync.types.time.serialize_aws_json_1_1(
            value["launch_time"]
        )
    if "end_time" in value:
        import aws_sdk_datasync.types.time

        out["EndTime"] = aws_sdk_datasync.types.time.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTaskExecutionResponse:
    out: DescribeTaskExecutionResponse = {}  # type: ignore[typeddict-item]
    if "TaskExecutionArn" in data:
        out["task_execution_arn"] = data["TaskExecutionArn"]
    if "Status" in data:
        import aws_sdk_datasync.types.task_execution_status

        out["status"] = (
            aws_sdk_datasync.types.task_execution_status.deserialize_aws_json_1_1(
                data["Status"]
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
    if "StartTime" in data:
        import aws_sdk_datasync.types.time

        out["start_time"] = aws_sdk_datasync.types.time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EstimatedFilesToTransfer" in data:
        out["estimated_files_to_transfer"] = data["EstimatedFilesToTransfer"]
    else:
        out["estimated_files_to_transfer"] = 0
    if "EstimatedBytesToTransfer" in data:
        out["estimated_bytes_to_transfer"] = data["EstimatedBytesToTransfer"]
    else:
        out["estimated_bytes_to_transfer"] = 0
    if "FilesTransferred" in data:
        out["files_transferred"] = data["FilesTransferred"]
    else:
        out["files_transferred"] = 0
    if "BytesWritten" in data:
        out["bytes_written"] = data["BytesWritten"]
    else:
        out["bytes_written"] = 0
    if "BytesTransferred" in data:
        out["bytes_transferred"] = data["BytesTransferred"]
    else:
        out["bytes_transferred"] = 0
    if "BytesCompressed" in data:
        out["bytes_compressed"] = data["BytesCompressed"]
    else:
        out["bytes_compressed"] = 0
    if "Result" in data:
        import aws_sdk_datasync.types.task_execution_result_detail

        out["result"] = (
            aws_sdk_datasync.types.task_execution_result_detail.deserialize_aws_json_1_1(
                data["Result"]
            )
        )
    if "TaskReportConfig" in data:
        import aws_sdk_datasync.types.task_report_config

        out["task_report_config"] = (
            aws_sdk_datasync.types.task_report_config.deserialize_aws_json_1_1(
                data["TaskReportConfig"]
            )
        )
    if "FilesDeleted" in data:
        out["files_deleted"] = data["FilesDeleted"]
    else:
        out["files_deleted"] = 0
    if "FilesSkipped" in data:
        out["files_skipped"] = data["FilesSkipped"]
    else:
        out["files_skipped"] = 0
    if "FilesVerified" in data:
        out["files_verified"] = data["FilesVerified"]
    else:
        out["files_verified"] = 0
    if "ReportResult" in data:
        import aws_sdk_datasync.types.report_result

        out["report_result"] = (
            aws_sdk_datasync.types.report_result.deserialize_aws_json_1_1(
                data["ReportResult"]
            )
        )
    if "EstimatedFilesToDelete" in data:
        out["estimated_files_to_delete"] = data["EstimatedFilesToDelete"]
    else:
        out["estimated_files_to_delete"] = 0
    if "TaskMode" in data:
        import aws_sdk_datasync.types.task_mode

        out["task_mode"] = aws_sdk_datasync.types.task_mode.deserialize_aws_json_1_1(
            data["TaskMode"]
        )
    if "FilesPrepared" in data:
        out["files_prepared"] = data["FilesPrepared"]
    else:
        out["files_prepared"] = 0
    if "FilesListed" in data:
        import aws_sdk_datasync.types.task_execution_files_listed_detail

        out["files_listed"] = (
            aws_sdk_datasync.types.task_execution_files_listed_detail.deserialize_aws_json_1_1(
                data["FilesListed"]
            )
        )
    if "FilesFailed" in data:
        import aws_sdk_datasync.types.task_execution_files_failed_detail

        out["files_failed"] = (
            aws_sdk_datasync.types.task_execution_files_failed_detail.deserialize_aws_json_1_1(
                data["FilesFailed"]
            )
        )
    if "EstimatedFoldersToDelete" in data:
        out["estimated_folders_to_delete"] = data["EstimatedFoldersToDelete"]
    if "EstimatedFoldersToTransfer" in data:
        out["estimated_folders_to_transfer"] = data["EstimatedFoldersToTransfer"]
    if "FoldersSkipped" in data:
        out["folders_skipped"] = data["FoldersSkipped"]
    if "FoldersPrepared" in data:
        out["folders_prepared"] = data["FoldersPrepared"]
    if "FoldersTransferred" in data:
        out["folders_transferred"] = data["FoldersTransferred"]
    if "FoldersVerified" in data:
        out["folders_verified"] = data["FoldersVerified"]
    if "FoldersDeleted" in data:
        out["folders_deleted"] = data["FoldersDeleted"]
    if "FoldersListed" in data:
        import aws_sdk_datasync.types.task_execution_folders_listed_detail

        out["folders_listed"] = (
            aws_sdk_datasync.types.task_execution_folders_listed_detail.deserialize_aws_json_1_1(
                data["FoldersListed"]
            )
        )
    if "FoldersFailed" in data:
        import aws_sdk_datasync.types.task_execution_folders_failed_detail

        out["folders_failed"] = (
            aws_sdk_datasync.types.task_execution_folders_failed_detail.deserialize_aws_json_1_1(
                data["FoldersFailed"]
            )
        )
    if "LaunchTime" in data:
        import aws_sdk_datasync.types.time

        out["launch_time"] = aws_sdk_datasync.types.time.deserialize_aws_json_1_1(
            data["LaunchTime"]
        )
    if "EndTime" in data:
        import aws_sdk_datasync.types.time

        out["end_time"] = aws_sdk_datasync.types.time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    return out
