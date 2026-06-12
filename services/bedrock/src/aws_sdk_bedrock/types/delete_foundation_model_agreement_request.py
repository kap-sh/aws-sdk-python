"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteFoundationModelAgreementRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.bedrock_model_id


class DeleteFoundationModelAgreementRequest(TypedDict):
    model_id: "aws_sdk_bedrock.types.bedrock_model_id.BedrockModelId"
    """<p>Model Id of the model access to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFoundationModelAgreementRequest) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    return out


def deserialize_json(data: dict) -> DeleteFoundationModelAgreementRequest:
    out: DeleteFoundationModelAgreementRequest = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError(
            "DeleteFoundationModelAgreementRequest.model_id required"
        )
    return out
