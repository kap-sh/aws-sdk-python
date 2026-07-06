"""Generated from Smithy shape ``com.amazonaws.bedrock#BedrockEvaluatorModel``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluator_model_identifier


class BedrockEvaluatorModel(TypedDict, closed=True):
    model_identifier: (
        "aws_sdk_bedrock.types.evaluator_model_identifier.EvaluatorModelIdentifier"
    )
    """<p>The Amazon Resource Name (ARN) of the evaluator model used used in knowledge base evaluation job or in model evaluation job that use a model as judge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockEvaluatorModel) -> dict:
    out: dict = {}
    out["modelIdentifier"] = value["model_identifier"]
    return out


def deserialize_json(data: dict) -> BedrockEvaluatorModel:
    out: BedrockEvaluatorModel = {}  # type: ignore[typeddict-item]
    if "modelIdentifier" in data:
        out["model_identifier"] = data["modelIdentifier"]
    else:
        raise DeserializationError("BedrockEvaluatorModel.model_identifier required")
    return out
