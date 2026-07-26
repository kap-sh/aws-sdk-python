"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceLifecycleHook``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.notebook_instance_lifecycle_config_content


class NotebookInstanceLifecycleHook(TypedDict, closed=True):
    content: NotRequired[
        "capo_sagemaker.types.notebook_instance_lifecycle_config_content.NotebookInstanceLifecycleConfigContent"
    ]
    """<p>A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookInstanceLifecycleHook) -> dict:
    out: dict = {}
    if "content" in value:
        out["Content"] = value["content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotebookInstanceLifecycleHook:
    out: NotebookInstanceLifecycleHook = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        out["content"] = data["Content"]
    return out
