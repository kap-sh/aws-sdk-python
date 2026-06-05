"""Generated from Smithy shape ``com.amazonaws.ec2#BundleTask``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.bundle_task_error
    import aws_sdk_ec2.types.bundle_task_state
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.storage
    import aws_sdk_ec2.types.string


class BundleTask(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance associated with this bundle task.</p>"""
    bundle_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the bundle task.</p>"""
    state: NotRequired["aws_sdk_ec2.types.bundle_task_state.BundleTaskState"]
    """<p>The state of the task.</p>"""
    start_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time this task started.</p>"""
    update_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time of the most recent update for the task.</p>"""
    storage: NotRequired["aws_sdk_ec2.types.storage.Storage"]
    """<p>The Amazon S3 storage locations.</p>"""
    progress: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The level of task completion, as a percent (for example, 20%).</p>"""
    bundle_task_error: NotRequired[
        "aws_sdk_ec2.types.bundle_task_error.BundleTaskError"
    ]
    """<p>If the task fails, a description of the error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: BundleTask, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "bundle_id" in value:
        pairs.append((f"{prefix}.BundleId", str(value["bundle_id"])))
    if "state" in value:
        import aws_sdk_ec2.types.bundle_task_state

        aws_sdk_ec2.types.bundle_task_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "start_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "update_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["update_time"], pairs, f"{prefix}.UpdateTime"
        )
    if "storage" in value:
        import aws_sdk_ec2.types.storage

        aws_sdk_ec2.types.storage.serialize_ec2_query(
            value["storage"], pairs, f"{prefix}.Storage"
        )
    if "progress" in value:
        pairs.append((f"{prefix}.Progress", str(value["progress"])))
    if "bundle_task_error" in value:
        import aws_sdk_ec2.types.bundle_task_error

        aws_sdk_ec2.types.bundle_task_error.serialize_ec2_query(
            value["bundle_task_error"], pairs, f"{prefix}.Error"
        )


def deserialize_ec2_query(el: Element) -> BundleTask:
    out: BundleTask = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_bundle_id = el.find("BundleId")
    if child_bundle_id is not None:
        out["bundle_id"] = str(child_bundle_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.bundle_task_state

        out["state"] = aws_sdk_ec2.types.bundle_task_state.deserialize_ec2_query(
            child_state
        )
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import aws_sdk_ec2.types.date_time

        out["start_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_start_time
        )
    child_update_time = el.find("UpdateTime")
    if child_update_time is not None:
        import aws_sdk_ec2.types.date_time

        out["update_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_update_time
        )
    child_storage = el.find("Storage")
    if child_storage is not None:
        import aws_sdk_ec2.types.storage

        out["storage"] = aws_sdk_ec2.types.storage.deserialize_ec2_query(child_storage)
    child_progress = el.find("Progress")
    if child_progress is not None:
        out["progress"] = str(child_progress.text or "")
    child_bundle_task_error = el.find("Error")
    if child_bundle_task_error is not None:
        import aws_sdk_ec2.types.bundle_task_error

        out["bundle_task_error"] = (
            aws_sdk_ec2.types.bundle_task_error.deserialize_ec2_query(
                child_bundle_task_error
            )
        )
    return out
