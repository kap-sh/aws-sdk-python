"""Generated from Smithy shape ``com.amazonaws.ec2#MacModificationTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_id
    import capo_ec2.types.mac_modification_task_id
    import capo_ec2.types.mac_modification_task_state
    import capo_ec2.types.mac_modification_task_type
    import capo_ec2.types.mac_system_integrity_protection_configuration
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.tag_list


class MacModificationTask(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the Amazon EC2 Mac instance.</p>"""
    mac_modification_task_id: NotRequired[
        "capo_ec2.types.mac_modification_task_id.MacModificationTaskId"
    ]
    """<p>The ID of task.</p>"""
    mac_system_integrity_protection_config: NotRequired[
        "capo_ec2.types.mac_system_integrity_protection_configuration.MacSystemIntegrityProtectionConfiguration"
    ]
    """<p>[SIP modification tasks only] Information about the SIP configuration.</p>"""
    start_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time the task was created, in the UTC timezone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the task.</p>"""
    task_state: NotRequired[
        "capo_ec2.types.mac_modification_task_state.MacModificationTaskState"
    ]
    """<p>The state of the task.</p>"""
    task_type: NotRequired[
        "capo_ec2.types.mac_modification_task_type.MacModificationTaskType"
    ]
    """<p>The type of task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MacModificationTask, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "mac_modification_task_id" in value:
        pairs.append(
            (
                f"{key_prefix}MacModificationTaskId",
                str(value["mac_modification_task_id"]),
            )
        )
    if "mac_system_integrity_protection_config" in value:
        import capo_ec2.types.mac_system_integrity_protection_configuration

        capo_ec2.types.mac_system_integrity_protection_configuration.serialize_ec2_query(
            value["mac_system_integrity_protection_config"],
            pairs,
            f"{key_prefix}MacSystemIntegrityProtectionConfig",
        )
    if "start_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "task_state" in value:
        import capo_ec2.types.mac_modification_task_state

        capo_ec2.types.mac_modification_task_state.serialize_ec2_query(
            value["task_state"], pairs, f"{key_prefix}TaskState"
        )
    if "task_type" in value:
        import capo_ec2.types.mac_modification_task_type

        capo_ec2.types.mac_modification_task_type.serialize_ec2_query(
            value["task_type"], pairs, f"{key_prefix}TaskType"
        )


def deserialize_ec2_query(el: Element) -> MacModificationTask:
    out: MacModificationTask = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_mac_modification_task_id = el.find("MacModificationTaskId")
    if child_mac_modification_task_id is not None:
        out["mac_modification_task_id"] = str(child_mac_modification_task_id.text or "")
    child_mac_system_integrity_protection_config = el.find(
        "MacSystemIntegrityProtectionConfig"
    )
    if child_mac_system_integrity_protection_config is not None:
        import capo_ec2.types.mac_system_integrity_protection_configuration

        out["mac_system_integrity_protection_config"] = (
            capo_ec2.types.mac_system_integrity_protection_configuration.deserialize_ec2_query(
                child_mac_system_integrity_protection_config
            )
        )
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["start_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_start_time
        )
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_task_state = el.find("TaskState")
    if child_task_state is not None:
        import capo_ec2.types.mac_modification_task_state

        out["task_state"] = (
            capo_ec2.types.mac_modification_task_state.deserialize_ec2_query(
                child_task_state
            )
        )
    child_task_type = el.find("TaskType")
    if child_task_type is not None:
        import capo_ec2.types.mac_modification_task_type

        out["task_type"] = (
            capo_ec2.types.mac_modification_task_type.deserialize_ec2_query(
                child_task_type
            )
        )
    return out
