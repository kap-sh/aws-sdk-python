"""Generated from Smithy shape ``com.amazonaws.sagemaker#TextGenerationResolvedAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.base_model_name


class TextGenerationResolvedAttributes(TypedDict, closed=True):
    base_model_name: NotRequired["capo_sagemaker.types.base_model_name.BaseModelName"]
    """<p>The name of the base model to fine-tune.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextGenerationResolvedAttributes) -> dict:
    out: dict = {}
    if "base_model_name" in value:
        out["BaseModelName"] = value["base_model_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TextGenerationResolvedAttributes:
    out: TextGenerationResolvedAttributes = {}  # type: ignore[typeddict-item]
    if "BaseModelName" in data:
        out["base_model_name"] = data["BaseModelName"]
    return out
