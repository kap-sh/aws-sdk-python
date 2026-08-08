"""Generated from Smithy shape ``com.amazonaws.ec2#ExportTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.export_task_state
    import capo_ec2.types.export_to_s3_task
    import capo_ec2.types.instance_export_details
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class ExportTask(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description of the resource being exported.</p>"""
    export_task_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the export task.</p>"""
    export_to_s3_task: NotRequired["capo_ec2.types.export_to_s3_task.ExportToS3Task"]
    """<p>Information about the export task.</p>"""
    instance_export_details: NotRequired[
        "capo_ec2.types.instance_export_details.InstanceExportDetails"
    ]
    """<p>Information about the instance to export.</p>"""
    state: NotRequired["capo_ec2.types.export_task_state.ExportTaskState"]
    """<p>The state of the export task.</p>"""
    status_message: NotRequired["capo_ec2.types.string.String"]
    """<p>The status message related to the export task.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags for the export task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportTask, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "export_task_id" in value:
        pairs.append((f"{key_prefix}ExportTaskId", str(value["export_task_id"])))
    if "export_to_s3_task" in value:
        import capo_ec2.types.export_to_s3_task

        capo_ec2.types.export_to_s3_task.serialize_ec2_query(
            value["export_to_s3_task"], pairs, f"{key_prefix}ExportToS3"
        )
    if "instance_export_details" in value:
        import capo_ec2.types.instance_export_details

        capo_ec2.types.instance_export_details.serialize_ec2_query(
            value["instance_export_details"], pairs, f"{key_prefix}InstanceExport"
        )
    if "state" in value:
        import capo_ec2.types.export_task_state

        capo_ec2.types.export_task_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "status_message" in value:
        pairs.append((f"{key_prefix}StatusMessage", str(value["status_message"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> ExportTask:
    out: ExportTask = {}  # type: ignore[typeddict-item]
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_export_task_id = el.find("exportTaskId")
    if child_export_task_id is not None:
        out["export_task_id"] = str(child_export_task_id.text or "")
    child_export_to_s3_task = el.find("exportToS3")
    if child_export_to_s3_task is not None:
        import capo_ec2.types.export_to_s3_task

        out["export_to_s3_task"] = (
            capo_ec2.types.export_to_s3_task.deserialize_ec2_query(
                child_export_to_s3_task
            )
        )
    child_instance_export_details = el.find("instanceExport")
    if child_instance_export_details is not None:
        import capo_ec2.types.instance_export_details

        out["instance_export_details"] = (
            capo_ec2.types.instance_export_details.deserialize_ec2_query(
                child_instance_export_details
            )
        )
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.export_task_state

        out["state"] = capo_ec2.types.export_task_state.deserialize_ec2_query(
            child_state
        )
    child_status_message = el.find("statusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    return out
