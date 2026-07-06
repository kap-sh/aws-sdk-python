"""Generated from Smithy shape ``com.amazonaws.machinelearning#UpdateEvaluationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id


class UpdateEvaluationOutput(TypedDict, closed=True):
    evaluation_id: NotRequired["aws_sdk_machine_learning.types.entity_id.EntityId"]
    """<p>The ID assigned to the <code>Evaluation</code> during creation. This value should be identical to the value of the <code>Evaluation</code> in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEvaluationOutput) -> dict:
    out: dict = {}
    if "evaluation_id" in value:
        out["EvaluationId"] = value["evaluation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEvaluationOutput:
    out: UpdateEvaluationOutput = {}  # type: ignore[typeddict-item]
    if "EvaluationId" in data:
        out["evaluation_id"] = data["EvaluationId"]
    return out
