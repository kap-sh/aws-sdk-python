"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageVersion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.image_arn
    import aws_sdk_sagemaker.types.image_version_arn
    import aws_sdk_sagemaker.types.image_version_number
    import aws_sdk_sagemaker.types.image_version_status
    import aws_sdk_sagemaker.types.timestamp


class ImageVersion(TypedDict):
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the version was created.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>When a create or delete operation fails, the reason for the failure.</p>"""
    image_arn: NotRequired["aws_sdk_sagemaker.types.image_arn.ImageArn"]
    """<p>The ARN of the image the version is based on.</p>"""
    image_version_arn: NotRequired[
        "aws_sdk_sagemaker.types.image_version_arn.ImageVersionArn"
    ]
    """<p>The ARN of the version.</p>"""
    image_version_status: NotRequired[
        "aws_sdk_sagemaker.types.image_version_status.ImageVersionStatus"
    ]
    """<p>The status of the version.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the version was last modified.</p>"""
    version: NotRequired[
        "aws_sdk_sagemaker.types.image_version_number.ImageVersionNumber"
    ]
    """<p>The version number.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageVersion) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "image_arn" in value:
        out["ImageArn"] = value["image_arn"]
    if "image_version_arn" in value:
        out["ImageVersionArn"] = value["image_version_arn"]
    if "image_version_status" in value:
        import aws_sdk_sagemaker.types.image_version_status

        out["ImageVersionStatus"] = (
            aws_sdk_sagemaker.types.image_version_status.serialize_aws_json_1_1(
                value["image_version_status"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageVersion:
    out: ImageVersion = {}  # type: ignore[typeddict-item]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "ImageArn" in data:
        out["image_arn"] = data["ImageArn"]
    if "ImageVersionArn" in data:
        out["image_version_arn"] = data["ImageVersionArn"]
    if "ImageVersionStatus" in data:
        import aws_sdk_sagemaker.types.image_version_status

        out["image_version_status"] = (
            aws_sdk_sagemaker.types.image_version_status.deserialize_aws_json_1_1(
                data["ImageVersionStatus"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "Version" in data:
        out["version"] = data["Version"]
    return out
