"""Generated from Smithy shape ``com.amazonaws.sagemaker#Image``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.image_arn
    import aws_sdk_sagemaker.types.image_description
    import aws_sdk_sagemaker.types.image_display_name
    import aws_sdk_sagemaker.types.image_name
    import aws_sdk_sagemaker.types.image_status
    import aws_sdk_sagemaker.types.timestamp


class Image(TypedDict):
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the image was created.</p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.image_description.ImageDescription"
    ]
    """<p>The description of the image.</p>"""
    display_name: NotRequired[
        "aws_sdk_sagemaker.types.image_display_name.ImageDisplayName"
    ]
    """<p>The name of the image as displayed.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>When a create, update, or delete operation fails, the reason for the failure.</p>"""
    image_arn: NotRequired["aws_sdk_sagemaker.types.image_arn.ImageArn"]
    """<p>The ARN of the image.</p>"""
    image_name: NotRequired["aws_sdk_sagemaker.types.image_name.ImageName"]
    """<p>The name of the image.</p>"""
    image_status: NotRequired["aws_sdk_sagemaker.types.image_status.ImageStatus"]
    """<p>The status of the image.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the image was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Image) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "image_arn" in value:
        out["ImageArn"] = value["image_arn"]
    if "image_name" in value:
        out["ImageName"] = value["image_name"]
    if "image_status" in value:
        import aws_sdk_sagemaker.types.image_status

        out["ImageStatus"] = (
            aws_sdk_sagemaker.types.image_status.serialize_aws_json_1_1(
                value["image_status"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Image:
    out: Image = {}  # type: ignore[typeddict-item]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "ImageArn" in data:
        out["image_arn"] = data["ImageArn"]
    if "ImageName" in data:
        out["image_name"] = data["ImageName"]
    if "ImageStatus" in data:
        import aws_sdk_sagemaker.types.image_status

        out["image_status"] = (
            aws_sdk_sagemaker.types.image_status.deserialize_aws_json_1_1(
                data["ImageStatus"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
