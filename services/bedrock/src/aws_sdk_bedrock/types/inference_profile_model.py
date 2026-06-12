"""Generated from Smithy shape ``com.amazonaws.bedrock#InferenceProfileModel``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.foundation_model_arn


class InferenceProfileModel(TypedDict):
    model_arn: NotRequired[
        "aws_sdk_bedrock.types.foundation_model_arn.FoundationModelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceProfileModel) -> dict:
    out: dict = {}
    if "model_arn" in value:
        out["modelArn"] = value["model_arn"]
    return out


def deserialize_json(data: dict) -> InferenceProfileModel:
    out: InferenceProfileModel = {}  # type: ignore[typeddict-item]
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    return out
