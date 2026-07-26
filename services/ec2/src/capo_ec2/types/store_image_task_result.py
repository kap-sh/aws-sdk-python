"""Generated from Smithy shape ``com.amazonaws.ec2#StoreImageTaskResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class StoreImageTaskResult(TypedDict, closed=True):
    ami_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the AMI that is being stored.</p>"""
    task_start_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time the task started.</p>"""
    bucket: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket that contains the stored AMI object.</p>"""
    s3object_key: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the stored AMI object in the bucket.</p>"""
    progress_percentage: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The progress of the task as a percentage.</p>"""
    store_task_state: NotRequired["capo_ec2.types.string.String"]
    """<p>The state of the store task (<code>InProgress</code>, <code>Completed</code>, or <code>Failed</code>).</p>"""
    store_task_failure_reason: NotRequired["capo_ec2.types.string.String"]
    """<p>If the tasks fails, the reason for the failure is returned. If the task succeeds, <code>null</code> is returned.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StoreImageTaskResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ami_id" in value:
        pairs.append((f"{prefix}.AmiId", str(value["ami_id"])))
    if "task_start_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["task_start_time"], pairs, f"{prefix}.TaskStartTime"
        )
    if "bucket" in value:
        pairs.append((f"{prefix}.Bucket", str(value["bucket"])))
    if "s3object_key" in value:
        pairs.append((f"{prefix}.S3objectKey", str(value["s3object_key"])))
    if "progress_percentage" in value:
        pairs.append(
            (f"{prefix}.ProgressPercentage", str(value["progress_percentage"]))
        )
    if "store_task_state" in value:
        pairs.append((f"{prefix}.StoreTaskState", str(value["store_task_state"])))
    if "store_task_failure_reason" in value:
        pairs.append(
            (
                f"{prefix}.StoreTaskFailureReason",
                str(value["store_task_failure_reason"]),
            )
        )


def deserialize_ec2_query(el: Element) -> StoreImageTaskResult:
    out: StoreImageTaskResult = {}  # type: ignore[typeddict-item]
    child_ami_id = el.find("AmiId")
    if child_ami_id is not None:
        out["ami_id"] = str(child_ami_id.text or "")
    child_task_start_time = el.find("TaskStartTime")
    if child_task_start_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["task_start_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_task_start_time
            )
        )
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_s3object_key = el.find("S3objectKey")
    if child_s3object_key is not None:
        out["s3object_key"] = str(child_s3object_key.text or "")
    child_progress_percentage = el.find("ProgressPercentage")
    if child_progress_percentage is not None:
        out["progress_percentage"] = int(child_progress_percentage.text or "")
    child_store_task_state = el.find("StoreTaskState")
    if child_store_task_state is not None:
        out["store_task_state"] = str(child_store_task_state.text or "")
    child_store_task_failure_reason = el.find("StoreTaskFailureReason")
    if child_store_task_failure_reason is not None:
        out["store_task_failure_reason"] = str(
            child_store_task_failure_reason.text or ""
        )
    return out
