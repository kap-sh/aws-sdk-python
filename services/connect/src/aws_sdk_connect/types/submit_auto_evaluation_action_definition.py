"""Generated from Smithy shape ``com.amazonaws.connect#SubmitAutoEvaluationActionDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_id


class SubmitAutoEvaluationActionDefinition(TypedDict):
    evaluation_form_id: "aws_sdk_connect.types.evaluation_form_id.EvaluationFormId"
    """<p>The identifier of the auto-evaluation enabled form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubmitAutoEvaluationActionDefinition) -> dict:
    out: dict = {}
    out["EvaluationFormId"] = value["evaluation_form_id"]
    return out


def deserialize_json(data: dict) -> SubmitAutoEvaluationActionDefinition:
    out: SubmitAutoEvaluationActionDefinition = {}  # type: ignore[typeddict-item]
    if "EvaluationFormId" in data:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        raise DeserializationError(
            "SubmitAutoEvaluationActionDefinition.evaluation_form_id required"
        )
    return out
