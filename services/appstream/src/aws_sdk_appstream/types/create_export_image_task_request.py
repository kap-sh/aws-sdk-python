"""Generated from Smithy shape ``com.amazonaws.appstream#CreateExportImageTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.ami_name
    import aws_sdk_appstream.types.arn
    import aws_sdk_appstream.types.description
    import aws_sdk_appstream.types.name
    import aws_sdk_appstream.types.tags


class CreateExportImageTaskRequest(TypedDict, closed=True):
    image_name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the WorkSpaces Applications image to export. The image must be in an available state and owned by your account.</p>"""
    ami_name: NotRequired["aws_sdk_appstream.types.ami_name.AmiName"]
    """<p>The name for the exported EC2 AMI. This is a required field that must be unique within your account and region.</p>"""
    iam_role_arn: NotRequired["aws_sdk_appstream.types.arn.Arn"]
    """<p>The ARN of the IAM role that allows WorkSpaces Applications to create the AMI. The role must have permissions to copy images, describe images, and create tags, with a trust relationship allowing appstream.amazonaws.com to assume the role.</p>"""
    tag_specifications: NotRequired["aws_sdk_appstream.types.tags.Tags"]
    """<p>The tags to apply to the exported AMI. These tags help you organize and manage your EC2 AMIs.</p>"""
    ami_description: NotRequired["aws_sdk_appstream.types.description.Description"]
    """<p>An optional description for the exported AMI. This description will be applied to the resulting EC2 AMI.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExportImageTaskRequest) -> dict:
    out: dict = {}
    if "image_name" in value:
        out["ImageName"] = value["image_name"]
    if "ami_name" in value:
        out["AmiName"] = value["ami_name"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "tag_specifications" in value:
        import aws_sdk_appstream.types.tags

        out["TagSpecifications"] = aws_sdk_appstream.types.tags.serialize_aws_json_1_1(
            value["tag_specifications"]
        )
    if "ami_description" in value:
        out["AmiDescription"] = value["ami_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExportImageTaskRequest:
    out: CreateExportImageTaskRequest = {}  # type: ignore[typeddict-item]
    if "ImageName" in data:
        out["image_name"] = data["ImageName"]
    if "AmiName" in data:
        out["ami_name"] = data["AmiName"]
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    if "TagSpecifications" in data:
        import aws_sdk_appstream.types.tags

        out["tag_specifications"] = (
            aws_sdk_appstream.types.tags.deserialize_aws_json_1_1(
                data["TagSpecifications"]
            )
        )
    if "AmiDescription" in data:
        out["ami_description"] = data["AmiDescription"]
    return out
