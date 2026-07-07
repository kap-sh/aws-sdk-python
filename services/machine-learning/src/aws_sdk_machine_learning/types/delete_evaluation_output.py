"""Generated from Smithy shape ``com.amazonaws.machinelearning#DeleteEvaluationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id


class DeleteEvaluationOutput(TypedDict, closed=True):
    evaluation_id: NotRequired["aws_sdk_machine_learning.types.entity_id.EntityId"]
    """<p>A user-supplied ID that uniquely identifies the <code>Evaluation</code>. This value should be identical to the value of the <code>EvaluationId</code> in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEvaluationOutput) -> dict:
    out: dict = {}
    if "evaluation_id" in value:
        out["EvaluationId"] = value["evaluation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEvaluationOutput:
    out: DeleteEvaluationOutput = {}  # type: ignore[typeddict-item]
    if "EvaluationId" in data:
        out["evaluation_id"] = data["EvaluationId"]
    return out
