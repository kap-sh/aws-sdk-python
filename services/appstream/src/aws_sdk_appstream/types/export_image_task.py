"""Generated from Smithy shape ``com.amazonaws.appstream#ExportImageTask``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.ami_name
    import aws_sdk_appstream.types.arn
    import aws_sdk_appstream.types.description
    import aws_sdk_appstream.types.error_details_list
    import aws_sdk_appstream.types.export_image_task_state
    import aws_sdk_appstream.types.photon_ami_id
    import aws_sdk_appstream.types.tags
    import aws_sdk_appstream.types.timestamp
    import aws_sdk_appstream.types.uuid


class ExportImageTask(TypedDict):
    task_id: NotRequired["aws_sdk_appstream.types.uuid.UUID"]
    """<p>The unique identifier for the export image task. Use this ID to track the task's progress and retrieve its details.</p>"""
    image_arn: NotRequired["aws_sdk_appstream.types.arn.Arn"]
    """<p>The ARN of the WorkSpaces Applications image being exported.</p>"""
    ami_name: NotRequired["aws_sdk_appstream.types.ami_name.AmiName"]
    """<p>The name of the EC2 AMI that will be created by this export task.</p>"""
    created_date: NotRequired["aws_sdk_appstream.types.timestamp.Timestamp"]
    """<p>The date and time when the export image task was created.</p>"""
    ami_description: NotRequired["aws_sdk_appstream.types.description.Description"]
    """<p>The description that will be applied to the exported EC2 AMI.</p>"""
    state: NotRequired[
        "aws_sdk_appstream.types.export_image_task_state.ExportImageTaskState"
    ]
    """<p>The current state of the export image task, such as PENDING, RUNNING, COMPLETED, or FAILED.</p>"""
    ami_id: NotRequired["aws_sdk_appstream.types.photon_ami_id.PhotonAmiId"]
    """<p>The ID of the EC2 AMI that was created by this export task. This field is only populated when the task completes successfully.</p>"""
    tag_specifications: NotRequired["aws_sdk_appstream.types.tags.Tags"]
    """<p>The tags that will be applied to the exported EC2 AMI.</p>"""
    error_details: NotRequired[
        "aws_sdk_appstream.types.error_details_list.ErrorDetailsList"
    ]
    """<p>Details about any errors that occurred during the export process. This field is only populated when the task fails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportImageTask) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    if "image_arn" in value:
        out["ImageArn"] = value["image_arn"]
    if "ami_name" in value:
        out["AmiName"] = value["ami_name"]
    if "created_date" in value:
        import aws_sdk_appstream.types.timestamp

        out["CreatedDate"] = aws_sdk_appstream.types.timestamp.serialize_aws_json_1_1(
            value["created_date"]
        )
    if "ami_description" in value:
        out["AmiDescription"] = value["ami_description"]
    if "state" in value:
        import aws_sdk_appstream.types.export_image_task_state

        out["State"] = (
            aws_sdk_appstream.types.export_image_task_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "ami_id" in value:
        out["AmiId"] = value["ami_id"]
    if "tag_specifications" in value:
        import aws_sdk_appstream.types.tags

        out["TagSpecifications"] = aws_sdk_appstream.types.tags.serialize_aws_json_1_1(
            value["tag_specifications"]
        )
    if "error_details" in value:
        import aws_sdk_appstream.types.error_details_list

        out["ErrorDetails"] = (
            aws_sdk_appstream.types.error_details_list.serialize_aws_json_1_1(
                value["error_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportImageTask:
    out: ExportImageTask = {}  # type: ignore[typeddict-item]
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    if "ImageArn" in data:
        out["image_arn"] = data["ImageArn"]
    if "AmiName" in data:
        out["ami_name"] = data["AmiName"]
    if "CreatedDate" in data:
        import aws_sdk_appstream.types.timestamp

        out["created_date"] = (
            aws_sdk_appstream.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedDate"]
            )
        )
    if "AmiDescription" in data:
        out["ami_description"] = data["AmiDescription"]
    if "State" in data:
        import aws_sdk_appstream.types.export_image_task_state

        out["state"] = (
            aws_sdk_appstream.types.export_image_task_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "AmiId" in data:
        out["ami_id"] = data["AmiId"]
    if "TagSpecifications" in data:
        import aws_sdk_appstream.types.tags

        out["tag_specifications"] = (
            aws_sdk_appstream.types.tags.deserialize_aws_json_1_1(
                data["TagSpecifications"]
            )
        )
    if "ErrorDetails" in data:
        import aws_sdk_appstream.types.error_details_list

        out["error_details"] = (
            aws_sdk_appstream.types.error_details_list.deserialize_aws_json_1_1(
                data["ErrorDetails"]
            )
        )
    return out
