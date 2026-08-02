"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceRootVolumeTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.image_id
    import capo_ec2.types.replace_root_volume_task_id
    import capo_ec2.types.replace_root_volume_task_state
    import capo_ec2.types.snapshot_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class ReplaceRootVolumeTask(TypedDict, closed=True):
    replace_root_volume_task_id: NotRequired[
        "capo_ec2.types.replace_root_volume_task_id.ReplaceRootVolumeTaskId"
    ]
    """<p>The ID of the root volume replacement task.</p>"""
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance for which the root volume replacement task was created.</p>"""
    task_state: NotRequired[
        "capo_ec2.types.replace_root_volume_task_state.ReplaceRootVolumeTaskState"
    ]
    """<p>The state of the task. The task can be in one of the following states:</p> <ul> <li> <p> <code>pending</code> - the replacement volume is being created.</p> </li> <li> <p> <code>in-progress</code> - the original volume is being detached and the replacement volume is being attached.</p> </li> <li> <p> <code>succeeded</code> - the replacement volume has been successfully attached to the instance and the instance is available.</p> </li> <li> <p> <code>failing</code> - the replacement task is in the process of failing.</p> </li> <li> <p> <code>failed</code> - the replacement task has failed but the original root volume is still attached.</p> </li> <li> <p> <code>failing-detached</code> - the replacement task is in the process of failing. The instance might have no root volume attached.</p> </li> <li> <p> <code>failed-detached</code> - the replacement task has failed and the instance has no root volume attached.</p> </li> </ul>"""
    start_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The time the task was started.</p>"""
    complete_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The time the task completed.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the task.</p>"""
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI used to create the replacement root volume.</p>"""
    snapshot_id: NotRequired["capo_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot used to create the replacement root volume.</p>"""
    delete_replaced_root_volume: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the original root volume is to be deleted after the root volume replacement task completes.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReplaceRootVolumeTask, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "replace_root_volume_task_id" in value:
        pairs.append(
            (
                f"{key_prefix}ReplaceRootVolumeTaskId",
                str(value["replace_root_volume_task_id"]),
            )
        )
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "task_state" in value:
        import capo_ec2.types.replace_root_volume_task_state

        capo_ec2.types.replace_root_volume_task_state.serialize_ec2_query(
            value["task_state"], pairs, f"{key_prefix}TaskState"
        )
    if "start_time" in value:
        pairs.append((f"{key_prefix}StartTime", str(value["start_time"])))
    if "complete_time" in value:
        pairs.append((f"{key_prefix}CompleteTime", str(value["complete_time"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "delete_replaced_root_volume" in value:
        pairs.append(
            (
                f"{key_prefix}DeleteReplacedRootVolume",
                "true" if value["delete_replaced_root_volume"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> ReplaceRootVolumeTask:
    out: ReplaceRootVolumeTask = {}  # type: ignore[typeddict-item]
    child_replace_root_volume_task_id = el.find("ReplaceRootVolumeTaskId")
    if child_replace_root_volume_task_id is not None:
        out["replace_root_volume_task_id"] = str(
            child_replace_root_volume_task_id.text or ""
        )
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_task_state = el.find("TaskState")
    if child_task_state is not None:
        import capo_ec2.types.replace_root_volume_task_state

        out["task_state"] = (
            capo_ec2.types.replace_root_volume_task_state.deserialize_ec2_query(
                child_task_state
            )
        )
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        out["start_time"] = str(child_start_time.text or "")
    child_complete_time = el.find("CompleteTime")
    if child_complete_time is not None:
        out["complete_time"] = str(child_complete_time.text or "")
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_delete_replaced_root_volume = el.find("DeleteReplacedRootVolume")
    if child_delete_replaced_root_volume is not None:
        out["delete_replaced_root_volume"] = (
            child_delete_replaced_root_volume.text or ""
        ).lower() == "true"
    return out
