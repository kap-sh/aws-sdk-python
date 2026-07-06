"""Generated from Smithy shape ``com.amazonaws.sagemaker#UiTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.template_content


class UiTemplate(TypedDict, closed=True):
    content: NotRequired["aws_sdk_sagemaker.types.template_content.TemplateContent"]
    """<p>The content of the Liquid template for the worker user interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UiTemplate) -> dict:
    out: dict = {}
    if "content" in value:
        out["Content"] = value["content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UiTemplate:
    out: UiTemplate = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        out["content"] = data["Content"]
    return out
