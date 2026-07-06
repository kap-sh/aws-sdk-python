"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.image_delete_property_list
    import aws_sdk_sagemaker.types.image_description
    import aws_sdk_sagemaker.types.image_display_name
    import aws_sdk_sagemaker.types.image_name
    import aws_sdk_sagemaker.types.role_arn


class UpdateImageRequest(TypedDict, closed=True):
    delete_properties: NotRequired[
        "aws_sdk_sagemaker.types.image_delete_property_list.ImageDeletePropertyList"
    ]
    """<p>A list of properties to delete. Only the <code>Description</code> and <code>DisplayName</code> properties can be deleted.</p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.image_description.ImageDescription"
    ]
    """<p>The new description for the image.</p>"""
    display_name: NotRequired[
        "aws_sdk_sagemaker.types.image_display_name.ImageDisplayName"
    ]
    """<p>The new display name for the image.</p>"""
    image_name: NotRequired["aws_sdk_sagemaker.types.image_name.ImageName"]
    """<p>The name of the image to update.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The new ARN for the IAM role that enables Amazon SageMaker AI to perform tasks on your behalf.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateImageRequest) -> dict:
    out: dict = {}
    if "delete_properties" in value:
        import aws_sdk_sagemaker.types.image_delete_property_list

        out["DeleteProperties"] = (
            aws_sdk_sagemaker.types.image_delete_property_list.serialize_aws_json_1_1(
                value["delete_properties"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "image_name" in value:
        out["ImageName"] = value["image_name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateImageRequest:
    out: UpdateImageRequest = {}  # type: ignore[typeddict-item]
    if "DeleteProperties" in data:
        import aws_sdk_sagemaker.types.image_delete_property_list

        out["delete_properties"] = (
            aws_sdk_sagemaker.types.image_delete_property_list.deserialize_aws_json_1_1(
                data["DeleteProperties"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "ImageName" in data:
        out["image_name"] = data["ImageName"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
