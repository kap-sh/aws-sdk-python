"""Generated from Smithy shape ``com.amazonaws.connect#CreateEvaluationFormResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.resource_id


class CreateEvaluationFormResponse(TypedDict):
    evaluation_form_id: "aws_sdk_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the evaluation form resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEvaluationFormResponse) -> dict:
    out: dict = {}
    out["EvaluationFormId"] = value["evaluation_form_id"]
    out["EvaluationFormArn"] = value["evaluation_form_arn"]
    return out


def deserialize_json(data: dict) -> CreateEvaluationFormResponse:
    out: CreateEvaluationFormResponse = {}  # type: ignore[typeddict-item]
    if "EvaluationFormId" in data:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        raise DeserializationError(
            "CreateEvaluationFormResponse.evaluation_form_id required"
        )
    if "EvaluationFormArn" in data:
        out["evaluation_form_arn"] = data["EvaluationFormArn"]
    else:
        raise DeserializationError(
            "CreateEvaluationFormResponse.evaluation_form_arn required"
        )
    return out
