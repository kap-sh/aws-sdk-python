"""Generated from Smithy shape ``com.amazonaws.bedrock#KbInferenceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.text_inference_config


class KbInferenceConfig(TypedDict, closed=True):
    text_inference_config: NotRequired[
        "capo_bedrock.types.text_inference_config.TextInferenceConfig"
    ]
    """<p>Contains configuration details for text generation using a language model via the <code>RetrieveAndGenerate</code> function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KbInferenceConfig) -> dict:
    out: dict = {}
    if "text_inference_config" in value:
        import capo_bedrock.types.text_inference_config

        out["textInferenceConfig"] = (
            capo_bedrock.types.text_inference_config.serialize_json(
                value["text_inference_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> KbInferenceConfig:
    out: KbInferenceConfig = {}  # type: ignore[typeddict-item]
    if data.get("textInferenceConfig") is not None:
        import capo_bedrock.types.text_inference_config

        out["text_inference_config"] = (
            capo_bedrock.types.text_inference_config.deserialize_json(
                data["textInferenceConfig"]
            )
        )
    return out
