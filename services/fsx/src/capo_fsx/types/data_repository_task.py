"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.capacity_to_release
    import capo_fsx.types.completion_report
    import capo_fsx.types.creation_time
    import capo_fsx.types.data_repository_task_failure_details
    import capo_fsx.types.data_repository_task_lifecycle
    import capo_fsx.types.data_repository_task_paths
    import capo_fsx.types.data_repository_task_status
    import capo_fsx.types.data_repository_task_type
    import capo_fsx.types.end_time
    import capo_fsx.types.file_cache_id
    import capo_fsx.types.file_system_id
    import capo_fsx.types.release_configuration
    import capo_fsx.types.resource_arn
    import capo_fsx.types.start_time
    import capo_fsx.types.tags
    import capo_fsx.types.task_id


class DataRepositoryTask(TypedDict, closed=True):
    task_id: NotRequired["capo_fsx.types.task_id.TaskId"]
    """<p>The system-generated, unique 17-digit ID of the data repository task.</p>"""
    lifecycle: NotRequired[
        "capo_fsx.types.data_repository_task_lifecycle.DataRepositoryTaskLifecycle"
    ]
    """<p>The lifecycle status of the data repository task, as follows:</p> <ul> <li> <p> <code>PENDING</code> - The task has not started.</p> </li> <li> <p> <code>EXECUTING</code> - The task is in process.</p> </li> <li> <p> <code>FAILED</code> - The task was not able to be completed. For example, there may be files the task failed to process. The <a>DataRepositoryTaskFailureDetails</a> property provides more information about task failures.</p> </li> <li> <p> <code>SUCCEEDED</code> - The task has completed successfully.</p> </li> <li> <p> <code>CANCELED</code> - The task was canceled and it did not complete.</p> </li> <li> <p> <code>CANCELING</code> - The task is in process of being canceled.</p> </li> </ul> <note> <p>You cannot delete an FSx for Lustre file system if there are data repository tasks for the file system in the <code>PENDING</code> or <code>EXECUTING</code> states. Please retry when the data repository task is finished (with a status of <code>CANCELED</code>, <code>SUCCEEDED</code>, or <code>FAILED</code>). You can use the DescribeDataRepositoryTask action to monitor the task status. Contact the FSx team if you need to delete your file system immediately.</p> </note>"""
    type: NotRequired["capo_fsx.types.data_repository_task_type.DataRepositoryTaskType"]
    """<p>The type of data repository task.</p> <ul> <li> <p> <code>EXPORT_TO_REPOSITORY</code> tasks export from your Amazon FSx for Lustre file system to a linked data repository.</p> </li> <li> <p> <code>IMPORT_METADATA_FROM_REPOSITORY</code> tasks import metadata changes from a linked S3 bucket to your Amazon FSx for Lustre file system.</p> </li> <li> <p> <code>RELEASE_DATA_FROM_FILESYSTEM</code> tasks release files in your Amazon FSx for Lustre file system that have been exported to a linked S3 bucket and that meet your specified release criteria.</p> </li> <li> <p> <code>AUTO_RELEASE_DATA</code> tasks automatically release files from an Amazon File Cache resource.</p> </li> </ul>"""
    creation_time: NotRequired["capo_fsx.types.creation_time.CreationTime"]
    start_time: NotRequired["capo_fsx.types.start_time.StartTime"]
    """<p>The time the system began processing the task.</p>"""
    end_time: NotRequired["capo_fsx.types.end_time.EndTime"]
    """<p>The time the system completed processing the task, populated after the task is complete.</p>"""
    resource_arn: NotRequired["capo_fsx.types.resource_arn.ResourceARN"]
    tags: NotRequired["capo_fsx.types.tags.Tags"]
    file_system_id: NotRequired["capo_fsx.types.file_system_id.FileSystemId"]
    """<p>The globally unique ID of the file system.</p>"""
    paths: NotRequired[
        "capo_fsx.types.data_repository_task_paths.DataRepositoryTaskPaths"
    ]
    """<p>An array of paths that specify the data for the data repository task to process. For example, in an EXPORT_TO_REPOSITORY task, the paths specify which data to export to the linked data repository.</p> <p>(Default) If <code>Paths</code> is not specified, Amazon FSx uses the file system root directory.</p>"""
    failure_details: NotRequired[
        "capo_fsx.types.data_repository_task_failure_details.DataRepositoryTaskFailureDetails"
    ]
    """<p>Failure message describing why the task failed, it is populated only when <code>Lifecycle</code> is set to <code>FAILED</code>.</p>"""
    status: NotRequired[
        "capo_fsx.types.data_repository_task_status.DataRepositoryTaskStatus"
    ]
    """<p>Provides the status of the number of files that the task has processed successfully and failed to process.</p>"""
    report: NotRequired["capo_fsx.types.completion_report.CompletionReport"]
    capacity_to_release: NotRequired[
        "capo_fsx.types.capacity_to_release.CapacityToRelease"
    ]
    """<p>Specifies the amount of data to release, in GiB, by an Amazon File Cache AUTO_RELEASE_DATA task that automatically releases files from the cache.</p>"""
    file_cache_id: NotRequired["capo_fsx.types.file_cache_id.FileCacheId"]
    """<p>The system-generated, unique ID of the cache.</p>"""
    release_configuration: NotRequired[
        "capo_fsx.types.release_configuration.ReleaseConfiguration"
    ]
    """<p>The configuration that specifies the last accessed time criteria for files that will be released from an Amazon FSx for Lustre file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryTask) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    if "lifecycle" in value:
        import capo_fsx.types.data_repository_task_lifecycle

        out["Lifecycle"] = (
            capo_fsx.types.data_repository_task_lifecycle.serialize_aws_json_1_1(
                value["lifecycle"]
            )
        )
    if "type" in value:
        import capo_fsx.types.data_repository_task_type

        out["Type"] = capo_fsx.types.data_repository_task_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "creation_time" in value:
        import capo_fsx.types.creation_time

        out["CreationTime"] = capo_fsx.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "start_time" in value:
        import capo_fsx.types.start_time

        out["StartTime"] = capo_fsx.types.start_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_fsx.types.end_time

        out["EndTime"] = capo_fsx.types.end_time.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "tags" in value:
        import capo_fsx.types.tags

        out["Tags"] = capo_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "paths" in value:
        import capo_fsx.types.data_repository_task_paths

        out["Paths"] = capo_fsx.types.data_repository_task_paths.serialize_aws_json_1_1(
            value["paths"]
        )
    if "failure_details" in value:
        import capo_fsx.types.data_repository_task_failure_details

        out["FailureDetails"] = (
            capo_fsx.types.data_repository_task_failure_details.serialize_aws_json_1_1(
                value["failure_details"]
            )
        )
    if "status" in value:
        import capo_fsx.types.data_repository_task_status

        out["Status"] = (
            capo_fsx.types.data_repository_task_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "report" in value:
        import capo_fsx.types.completion_report

        out["Report"] = capo_fsx.types.completion_report.serialize_aws_json_1_1(
            value["report"]
        )
    if "capacity_to_release" in value:
        out["CapacityToRelease"] = value["capacity_to_release"]
    if "file_cache_id" in value:
        out["FileCacheId"] = value["file_cache_id"]
    if "release_configuration" in value:
        import capo_fsx.types.release_configuration

        out["ReleaseConfiguration"] = (
            capo_fsx.types.release_configuration.serialize_aws_json_1_1(
                value["release_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataRepositoryTask:
    out: DataRepositoryTask = {}  # type: ignore[typeddict-item]
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    if "Lifecycle" in data:
        import capo_fsx.types.data_repository_task_lifecycle

        out["lifecycle"] = (
            capo_fsx.types.data_repository_task_lifecycle.deserialize_aws_json_1_1(
                data["Lifecycle"]
            )
        )
    if "Type" in data:
        import capo_fsx.types.data_repository_task_type

        out["type"] = capo_fsx.types.data_repository_task_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "CreationTime" in data:
        import capo_fsx.types.creation_time

        out["creation_time"] = capo_fsx.types.creation_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "StartTime" in data:
        import capo_fsx.types.start_time

        out["start_time"] = capo_fsx.types.start_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_fsx.types.end_time

        out["end_time"] = capo_fsx.types.end_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "Tags" in data:
        import capo_fsx.types.tags

        out["tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "Paths" in data:
        import capo_fsx.types.data_repository_task_paths

        out["paths"] = (
            capo_fsx.types.data_repository_task_paths.deserialize_aws_json_1_1(
                data["Paths"]
            )
        )
    if "FailureDetails" in data:
        import capo_fsx.types.data_repository_task_failure_details

        out["failure_details"] = (
            capo_fsx.types.data_repository_task_failure_details.deserialize_aws_json_1_1(
                data["FailureDetails"]
            )
        )
    if "Status" in data:
        import capo_fsx.types.data_repository_task_status

        out["status"] = (
            capo_fsx.types.data_repository_task_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Report" in data:
        import capo_fsx.types.completion_report

        out["report"] = capo_fsx.types.completion_report.deserialize_aws_json_1_1(
            data["Report"]
        )
    if "CapacityToRelease" in data:
        out["capacity_to_release"] = data["CapacityToRelease"]
    if "FileCacheId" in data:
        out["file_cache_id"] = data["FileCacheId"]
    if "ReleaseConfiguration" in data:
        import capo_fsx.types.release_configuration

        out["release_configuration"] = (
            capo_fsx.types.release_configuration.deserialize_aws_json_1_1(
                data["ReleaseConfiguration"]
            )
        )
    return out
