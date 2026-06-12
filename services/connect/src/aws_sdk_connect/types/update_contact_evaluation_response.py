"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactEvaluationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.resource_id


class UpdateContactEvaluationResponse(TypedDict):
    evaluation_id: "aws_sdk_connect.types.resource_id.ResourceId"
    """<p>A unique identifier for the contact evaluation.</p>"""
    evaluation_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the contact evaluation resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactEvaluationResponse) -> dict:
    out: dict = {}
    out["EvaluationId"] = value["evaluation_id"]
    out["EvaluationArn"] = value["evaluation_arn"]
    return out


def deserialize_json(data: dict) -> UpdateContactEvaluationResponse:
    out: UpdateContactEvaluationResponse = {}  # type: ignore[typeddict-item]
    if "EvaluationId" in data:
        out["evaluation_id"] = data["EvaluationId"]
    else:
        raise DeserializationError(
            "UpdateContactEvaluationResponse.evaluation_id required"
        )
    if "EvaluationArn" in data:
        out["evaluation_arn"] = data["EvaluationArn"]
    else:
        raise DeserializationError(
            "UpdateContactEvaluationResponse.evaluation_arn required"
        )
    return out
