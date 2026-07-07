"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateHumanTaskUiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.human_task_ui_name
    import aws_sdk_sagemaker.types.tag_list
    import aws_sdk_sagemaker.types.ui_template


class CreateHumanTaskUiRequest(TypedDict, closed=True):
    human_task_ui_name: NotRequired[
        "aws_sdk_sagemaker.types.human_task_ui_name.HumanTaskUiName"
    ]
    """<p>The name of the user interface you are creating.</p>"""
    ui_template: NotRequired["aws_sdk_sagemaker.types.ui_template.UiTemplate"]
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs that contain metadata to help you categorize and organize a human review workflow user interface. Each tag consists of a key and a value, both of which you define.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHumanTaskUiRequest) -> dict:
    out: dict = {}
    if "human_task_ui_name" in value:
        out["HumanTaskUiName"] = value["human_task_ui_name"]
    if "ui_template" in value:
        import aws_sdk_sagemaker.types.ui_template

        out["UiTemplate"] = aws_sdk_sagemaker.types.ui_template.serialize_aws_json_1_1(
            value["ui_template"]
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHumanTaskUiRequest:
    out: CreateHumanTaskUiRequest = {}  # type: ignore[typeddict-item]
    if "HumanTaskUiName" in data:
        out["human_task_ui_name"] = data["HumanTaskUiName"]
    if "UiTemplate" in data:
        import aws_sdk_sagemaker.types.ui_template

        out["ui_template"] = (
            aws_sdk_sagemaker.types.ui_template.deserialize_aws_json_1_1(
                data["UiTemplate"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
