"""Generated from Smithy shape ``com.amazonaws.qconnect#GenerativeReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.llm_model_id
    import aws_sdk_qconnect.types.uuid


class GenerativeReference(TypedDict, closed=True):
    model_id: NotRequired["aws_sdk_qconnect.types.llm_model_id.LlmModelId"]
    """<p>The identifier of the LLM model. </p>"""
    generation_id: NotRequired["aws_sdk_qconnect.types.uuid.Uuid"]
    """<p> The identifier of the LLM model. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerativeReference) -> dict:
    out: dict = {}
    if "model_id" in value:
        out["modelId"] = value["model_id"]
    if "generation_id" in value:
        out["generationId"] = value["generation_id"]
    return out


def deserialize_json(data: dict) -> GenerativeReference:
    out: GenerativeReference = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    if "generationId" in data:
        out["generation_id"] = data["generationId"]
    return out
