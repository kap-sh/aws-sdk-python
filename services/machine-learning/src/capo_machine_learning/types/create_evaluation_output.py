"""Generated from Smithy shape ``com.amazonaws.machinelearning#CreateEvaluationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id


class CreateEvaluationOutput(TypedDict, closed=True):
    evaluation_id: NotRequired["capo_machine_learning.types.entity_id.EntityId"]
    """<p>The user-supplied ID that uniquely identifies the <code>Evaluation</code>. This value should be identical to the value of the <code>EvaluationId</code> in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEvaluationOutput) -> dict:
    out: dict = {}
    if "evaluation_id" in value:
        out["EvaluationId"] = value["evaluation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEvaluationOutput:
    out: CreateEvaluationOutput = {}  # type: ignore[typeddict-item]
    if "EvaluationId" in data:
        out["evaluation_id"] = data["EvaluationId"]
    return out
