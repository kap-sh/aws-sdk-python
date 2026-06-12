"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateCustomModelResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.model_arn


class CreateCustomModelResponse(TypedDict):
    model_arn: "aws_sdk_bedrock.types.model_arn.ModelArn"
    """<p>The Amazon Resource Name (ARN) of the new custom model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomModelResponse) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    return out


def deserialize_json(data: dict) -> CreateCustomModelResponse:
    out: CreateCustomModelResponse = {}  # type: ignore[typeddict-item]
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError("CreateCustomModelResponse.model_arn required")
    return out
