"""Generated from Smithy shape ``com.amazonaws.connect#UpdateEvaluationFormResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.resource_id
    import aws_sdk_connect.types.version_number


class UpdateEvaluationFormResponse(TypedDict, closed=True):
    evaluation_form_id: "aws_sdk_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the contact evaluation resource.</p>"""
    evaluation_form_version: "aws_sdk_connect.types.version_number.VersionNumber"
    """<p>The version of the updated evaluation form resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEvaluationFormResponse) -> dict:
    out: dict = {}
    out["EvaluationFormId"] = value["evaluation_form_id"]
    out["EvaluationFormArn"] = value["evaluation_form_arn"]
    out["EvaluationFormVersion"] = value.get("evaluation_form_version", 0)
    return out


def deserialize_json(data: dict) -> UpdateEvaluationFormResponse:
    out: UpdateEvaluationFormResponse = {}  # type: ignore[typeddict-item]
    if "EvaluationFormId" in data:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        raise DeserializationError(
            "UpdateEvaluationFormResponse.evaluation_form_id required"
        )
    if "EvaluationFormArn" in data:
        out["evaluation_form_arn"] = data["EvaluationFormArn"]
    else:
        raise DeserializationError(
            "UpdateEvaluationFormResponse.evaluation_form_arn required"
        )
    if "EvaluationFormVersion" in data:
        out["evaluation_form_version"] = data["EvaluationFormVersion"]
    else:
        out["evaluation_form_version"] = 0
    return out
