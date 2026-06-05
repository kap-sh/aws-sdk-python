"""Generated from Smithy shape ``com.amazonaws.ec2#ExportTask``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_task_state
    import aws_sdk_ec2.types.export_to_s3_task
    import aws_sdk_ec2.types.instance_export_details
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ExportTask(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the resource being exported.</p>"""
    export_task_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the export task.</p>"""
    export_to_s3_task: NotRequired["aws_sdk_ec2.types.export_to_s3_task.ExportToS3Task"]
    """<p>Information about the export task.</p>"""
    instance_export_details: NotRequired[
        "aws_sdk_ec2.types.instance_export_details.InstanceExportDetails"
    ]
    """<p>Information about the instance to export.</p>"""
    state: NotRequired["aws_sdk_ec2.types.export_task_state.ExportTaskState"]
    """<p>The state of the export task.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message related to the export task.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the export task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportTask, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "export_task_id" in value:
        pairs.append((f"{prefix}.ExportTaskId", str(value["export_task_id"])))
    if "export_to_s3_task" in value:
        import aws_sdk_ec2.types.export_to_s3_task

        aws_sdk_ec2.types.export_to_s3_task.serialize_ec2_query(
            value["export_to_s3_task"], pairs, f"{prefix}.ExportToS3"
        )
    if "instance_export_details" in value:
        import aws_sdk_ec2.types.instance_export_details

        aws_sdk_ec2.types.instance_export_details.serialize_ec2_query(
            value["instance_export_details"], pairs, f"{prefix}.InstanceExport"
        )
    if "state" in value:
        import aws_sdk_ec2.types.export_task_state

        aws_sdk_ec2.types.export_task_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> ExportTask:
    out: ExportTask = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_export_task_id = el.find("ExportTaskId")
    if child_export_task_id is not None:
        out["export_task_id"] = str(child_export_task_id.text or "")
    child_export_to_s3_task = el.find("ExportToS3")
    if child_export_to_s3_task is not None:
        import aws_sdk_ec2.types.export_to_s3_task

        out["export_to_s3_task"] = (
            aws_sdk_ec2.types.export_to_s3_task.deserialize_ec2_query(
                child_export_to_s3_task
            )
        )
    child_instance_export_details = el.find("InstanceExport")
    if child_instance_export_details is not None:
        import aws_sdk_ec2.types.instance_export_details

        out["instance_export_details"] = (
            aws_sdk_ec2.types.instance_export_details.deserialize_ec2_query(
                child_instance_export_details
            )
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.export_task_state

        out["state"] = aws_sdk_ec2.types.export_task_state.deserialize_ec2_query(
            child_state
        )
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
