"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateStudioLifecycleConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.studio_lifecycle_config_app_type
    import capo_sagemaker.types.studio_lifecycle_config_content
    import capo_sagemaker.types.studio_lifecycle_config_name
    import capo_sagemaker.types.tag_list


class CreateStudioLifecycleConfigRequest(TypedDict, closed=True):
    studio_lifecycle_config_name: NotRequired[
        "capo_sagemaker.types.studio_lifecycle_config_name.StudioLifecycleConfigName"
    ]
    """<p>The name of the Amazon SageMaker AI Studio Lifecycle Configuration to create.</p>"""
    studio_lifecycle_config_content: NotRequired[
        "capo_sagemaker.types.studio_lifecycle_config_content.StudioLifecycleConfigContent"
    ]
    """<p>The content of your Amazon SageMaker AI Studio Lifecycle Configuration script. This content must be base64 encoded.</p>"""
    studio_lifecycle_config_app_type: NotRequired[
        "capo_sagemaker.types.studio_lifecycle_config_app_type.StudioLifecycleConfigAppType"
    ]
    """<p>The App type that the Lifecycle Configuration is attached to.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>Tags to be associated with the Lifecycle Configuration. Each tag consists of a key and an optional value. Tag keys must be unique per resource. Tags are searchable using the Search API. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStudioLifecycleConfigRequest) -> dict:
    out: dict = {}
    if "studio_lifecycle_config_name" in value:
        out["StudioLifecycleConfigName"] = value["studio_lifecycle_config_name"]
    if "studio_lifecycle_config_content" in value:
        out["StudioLifecycleConfigContent"] = value["studio_lifecycle_config_content"]
    if "studio_lifecycle_config_app_type" in value:
        import capo_sagemaker.types.studio_lifecycle_config_app_type

        out["StudioLifecycleConfigAppType"] = (
            capo_sagemaker.types.studio_lifecycle_config_app_type.serialize_aws_json_1_1(
                value["studio_lifecycle_config_app_type"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStudioLifecycleConfigRequest:
    out: CreateStudioLifecycleConfigRequest = {}  # type: ignore[typeddict-item]
    if "StudioLifecycleConfigName" in data:
        out["studio_lifecycle_config_name"] = data["StudioLifecycleConfigName"]
    if "StudioLifecycleConfigContent" in data:
        out["studio_lifecycle_config_content"] = data["StudioLifecycleConfigContent"]
    if "StudioLifecycleConfigAppType" in data:
        import capo_sagemaker.types.studio_lifecycle_config_app_type

        out["studio_lifecycle_config_app_type"] = (
            capo_sagemaker.types.studio_lifecycle_config_app_type.deserialize_aws_json_1_1(
                data["StudioLifecycleConfigAppType"]
            )
        )
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
