"""Generated from Smithy shape ``com.amazonaws.ec2#ExportImageTask``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_task_s3_location
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ExportImageTask(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the image being exported.</p>"""
    export_image_task_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the export image task.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the image.</p>"""
    progress: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The percent complete of the export image task.</p>"""
    s3_export_location: NotRequired[
        "aws_sdk_ec2.types.export_task_s3_location.ExportTaskS3Location"
    ]
    """<p>Information about the destination Amazon S3 bucket.</p>"""
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status of the export image task. The possible values are <code>active</code>, <code>completed</code>, <code>deleting</code>, and <code>deleted</code>.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message for the export image task.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the export image task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportImageTask, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "export_image_task_id" in value:
        pairs.append(
            (f"{prefix}.ExportImageTaskId", str(value["export_image_task_id"]))
        )
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "progress" in value:
        pairs.append((f"{prefix}.Progress", str(value["progress"])))
    if "s3_export_location" in value:
        import aws_sdk_ec2.types.export_task_s3_location

        aws_sdk_ec2.types.export_task_s3_location.serialize_ec2_query(
            value["s3_export_location"], pairs, f"{prefix}.S3ExportLocation"
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> ExportImageTask:
    out: ExportImageTask = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_export_image_task_id = el.find("ExportImageTaskId")
    if child_export_image_task_id is not None:
        out["export_image_task_id"] = str(child_export_image_task_id.text or "")
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_progress = el.find("Progress")
    if child_progress is not None:
        out["progress"] = str(child_progress.text or "")
    child_s3_export_location = el.find("S3ExportLocation")
    if child_s3_export_location is not None:
        import aws_sdk_ec2.types.export_task_s3_location

        out["s3_export_location"] = (
            aws_sdk_ec2.types.export_task_s3_location.deserialize_ec2_query(
                child_s3_export_location
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
