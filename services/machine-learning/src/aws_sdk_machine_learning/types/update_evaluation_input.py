"""Generated from Smithy shape ``com.amazonaws.machinelearning#UpdateEvaluationInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id
    import aws_sdk_machine_learning.types.entity_name


class UpdateEvaluationInput(TypedDict):
    evaluation_id: "aws_sdk_machine_learning.types.entity_id.EntityId"
    """<p>The ID assigned to the <code>Evaluation</code> during creation.</p>"""
    evaluation_name: "aws_sdk_machine_learning.types.entity_name.EntityName"
    """<p>A new user-supplied name or description of the <code>Evaluation</code> that will replace the current content. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEvaluationInput) -> dict:
    out: dict = {}
    out["EvaluationId"] = value["evaluation_id"]
    out["EvaluationName"] = value["evaluation_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEvaluationInput:
    out: UpdateEvaluationInput = {}  # type: ignore[typeddict-item]
    if "EvaluationId" in data:
        out["evaluation_id"] = data["EvaluationId"]
    else:
        raise DeserializationError("UpdateEvaluationInput.evaluation_id required")
    if "EvaluationName" in data:
        out["evaluation_name"] = data["EvaluationName"]
    else:
        raise DeserializationError("UpdateEvaluationInput.evaluation_name required")
    return out
