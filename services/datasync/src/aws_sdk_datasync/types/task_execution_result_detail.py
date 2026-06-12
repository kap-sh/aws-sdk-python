"""Generated from Smithy shape ``com.amazonaws.datasync#TaskExecutionResultDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.duration
    import aws_sdk_datasync.types.phase_status
    import aws_sdk_datasync.types.string


class TaskExecutionResultDetail(TypedDict):
    prepare_duration: NotRequired["aws_sdk_datasync.types.duration.Duration"]
    """<p>The time in milliseconds that your task execution was in the <code>PREPARING</code> step. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses\">Task execution statuses</a>.</p> <p>For Enhanced mode tasks, the value is always <code>0</code>. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/how-datasync-transfer-works.html#how-datasync-prepares\">How DataSync prepares your data transfer</a>.</p>"""
    prepare_status: NotRequired["aws_sdk_datasync.types.phase_status.PhaseStatus"]
    """<p>The status of the <code>PREPARING</code> step for your task execution. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses\">Task execution statuses</a>.</p>"""
    total_duration: NotRequired["aws_sdk_datasync.types.duration.Duration"]
    """<p>The time in milliseconds that your task execution ran.</p>"""
    transfer_duration: NotRequired["aws_sdk_datasync.types.duration.Duration"]
    """<p>The time in milliseconds that your task execution was in the <code>TRANSFERRING</code> step. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses\">Task execution statuses</a>.</p> <p>For Enhanced mode tasks, the value is always <code>0</code>. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/how-datasync-transfer-works.html#how-datasync-transfers\">How DataSync transfers your data</a>.</p>"""
    transfer_status: NotRequired["aws_sdk_datasync.types.phase_status.PhaseStatus"]
    """<p>The status of the <code>TRANSFERRING</code> step for your task execution. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses\">Task execution statuses</a>.</p>"""
    verify_duration: NotRequired["aws_sdk_datasync.types.duration.Duration"]
    """<p>The time in milliseconds that your task execution was in the <code>VERIFYING</code> step. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses\">Task execution statuses</a>.</p> <p>For Enhanced mode tasks, the value is always <code>0</code>. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/how-datasync-transfer-works.html#how-verifying-works\">How DataSync verifies your data's integrity</a>.</p>"""
    verify_status: NotRequired["aws_sdk_datasync.types.phase_status.PhaseStatus"]
    """<p>The status of the <code>VERIFYING</code> step for your task execution. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses\">Task execution statuses</a>.</p>"""
    error_code: NotRequired["aws_sdk_datasync.types.string.string"]
    """<p>An error that DataSync encountered during your task execution. You can use this information to help <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html\">troubleshoot issues</a>.</p>"""
    error_detail: NotRequired["aws_sdk_datasync.types.string.string"]
    """<p>The detailed description of an error that DataSync encountered during your task execution. You can use this information to help <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html\">troubleshoot issues</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskExecutionResultDetail) -> dict:
    out: dict = {}
    if "prepare_duration" in value:
        out["PrepareDuration"] = value["prepare_duration"]
    if "prepare_status" in value:
        import aws_sdk_datasync.types.phase_status

        out["PrepareStatus"] = (
            aws_sdk_datasync.types.phase_status.serialize_aws_json_1_1(
                value["prepare_status"]
            )
        )
    if "total_duration" in value:
        out["TotalDuration"] = value["total_duration"]
    if "transfer_duration" in value:
        out["TransferDuration"] = value["transfer_duration"]
    if "transfer_status" in value:
        import aws_sdk_datasync.types.phase_status

        out["TransferStatus"] = (
            aws_sdk_datasync.types.phase_status.serialize_aws_json_1_1(
                value["transfer_status"]
            )
        )
    if "verify_duration" in value:
        out["VerifyDuration"] = value["verify_duration"]
    if "verify_status" in value:
        import aws_sdk_datasync.types.phase_status

        out["VerifyStatus"] = (
            aws_sdk_datasync.types.phase_status.serialize_aws_json_1_1(
                value["verify_status"]
            )
        )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_detail" in value:
        out["ErrorDetail"] = value["error_detail"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskExecutionResultDetail:
    out: TaskExecutionResultDetail = {}  # type: ignore[typeddict-item]
    if "PrepareDuration" in data:
        out["prepare_duration"] = data["PrepareDuration"]
    if "PrepareStatus" in data:
        import aws_sdk_datasync.types.phase_status

        out["prepare_status"] = (
            aws_sdk_datasync.types.phase_status.deserialize_aws_json_1_1(
                data["PrepareStatus"]
            )
        )
    if "TotalDuration" in data:
        out["total_duration"] = data["TotalDuration"]
    if "TransferDuration" in data:
        out["transfer_duration"] = data["TransferDuration"]
    if "TransferStatus" in data:
        import aws_sdk_datasync.types.phase_status

        out["transfer_status"] = (
            aws_sdk_datasync.types.phase_status.deserialize_aws_json_1_1(
                data["TransferStatus"]
            )
        )
    if "VerifyDuration" in data:
        out["verify_duration"] = data["VerifyDuration"]
    if "VerifyStatus" in data:
        import aws_sdk_datasync.types.phase_status

        out["verify_status"] = (
            aws_sdk_datasync.types.phase_status.deserialize_aws_json_1_1(
                data["VerifyStatus"]
            )
        )
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorDetail" in data:
        out["error_detail"] = data["ErrorDetail"]
    return out
