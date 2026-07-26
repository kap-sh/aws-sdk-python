"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeImageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.image_arn
    import capo_sagemaker.types.image_description
    import capo_sagemaker.types.image_display_name
    import capo_sagemaker.types.image_name
    import capo_sagemaker.types.image_status
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.timestamp


class DescribeImageResponse(TypedDict, closed=True):
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the image was created.</p>"""
    description: NotRequired["capo_sagemaker.types.image_description.ImageDescription"]
    """<p>The description of the image.</p>"""
    display_name: NotRequired[
        "capo_sagemaker.types.image_display_name.ImageDisplayName"
    ]
    """<p>The name of the image as displayed.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>When a create, update, or delete operation fails, the reason for the failure.</p>"""
    image_arn: NotRequired["capo_sagemaker.types.image_arn.ImageArn"]
    """<p>The ARN of the image.</p>"""
    image_name: NotRequired["capo_sagemaker.types.image_name.ImageName"]
    """<p>The name of the image.</p>"""
    image_status: NotRequired["capo_sagemaker.types.image_status.ImageStatus"]
    """<p>The status of the image.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the image was last modified.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role that enables Amazon SageMaker AI to perform tasks on your behalf.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImageResponse) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
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
        import capo_sagemaker.types.image_status

        out["ImageStatus"] = capo_sagemaker.types.image_status.serialize_aws_json_1_1(
            value["image_status"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImageResponse:
    out: DescribeImageResponse = {}  # type: ignore[typeddict-item]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
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
        import capo_sagemaker.types.image_status

        out["image_status"] = (
            capo_sagemaker.types.image_status.deserialize_aws_json_1_1(
                data["ImageStatus"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
