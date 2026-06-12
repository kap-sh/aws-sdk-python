"""Generated from Smithy shape ``com.amazonaws.bedrock#KbInferenceConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.text_inference_config


class KbInferenceConfig(TypedDict):
    text_inference_config: NotRequired[
        "aws_sdk_bedrock.types.text_inference_config.TextInferenceConfig"
    ]
    """<p>Contains configuration details for text generation using a language model via the <code>RetrieveAndGenerate</code> function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KbInferenceConfig) -> dict:
    out: dict = {}
    if "text_inference_config" in value:
        import aws_sdk_bedrock.types.text_inference_config

        out["textInferenceConfig"] = (
            aws_sdk_bedrock.types.text_inference_config.serialize_json(
                value["text_inference_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> KbInferenceConfig:
    out: KbInferenceConfig = {}  # type: ignore[typeddict-item]
    if "textInferenceConfig" in data:
        import aws_sdk_bedrock.types.text_inference_config

        out["text_inference_config"] = (
            aws_sdk_bedrock.types.text_inference_config.deserialize_json(
                data["textInferenceConfig"]
            )
        )
    return out
