"""Generated from Smithy shape ``com.amazonaws.machinelearning#DeleteEvaluationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id


class DeleteEvaluationInput(TypedDict, closed=True):
    evaluation_id: "aws_sdk_machine_learning.types.entity_id.EntityId"
    """<p>A user-supplied ID that uniquely identifies the <code>Evaluation</code> to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEvaluationInput) -> dict:
    out: dict = {}
    out["EvaluationId"] = value["evaluation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEvaluationInput:
    out: DeleteEvaluationInput = {}  # type: ignore[typeddict-item]
    if "EvaluationId" in data:
        out["evaluation_id"] = data["EvaluationId"]
    else:
        raise DeserializationError("DeleteEvaluationInput.evaluation_id required")
    return out
