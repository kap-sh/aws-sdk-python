"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.image_description
    import capo_sagemaker.types.image_display_name
    import capo_sagemaker.types.image_name
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list


class CreateImageRequest(TypedDict, closed=True):
    description: NotRequired["capo_sagemaker.types.image_description.ImageDescription"]
    """<p>The description of the image.</p>"""
    display_name: NotRequired[
        "capo_sagemaker.types.image_display_name.ImageDisplayName"
    ]
    """<p>The display name of the image. If not provided, <code>ImageName</code> is displayed.</p>"""
    image_name: NotRequired["capo_sagemaker.types.image_name.ImageName"]
    """<p>The name of the image. Must be unique to your account.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The ARN of an IAM role that enables Amazon SageMaker AI to perform tasks on your behalf.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of tags to apply to the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateImageRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "image_name" in value:
        out["ImageName"] = value["image_name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateImageRequest:
    out: CreateImageRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "ImageName" in data:
        out["image_name"] = data["ImageName"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
