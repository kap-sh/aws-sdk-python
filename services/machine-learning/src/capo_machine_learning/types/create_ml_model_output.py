"""Generated from Smithy shape ``com.amazonaws.machinelearning#CreateMLModelOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id


class CreateMLModelOutput(TypedDict, closed=True):
    ml_model_id: NotRequired["capo_machine_learning.types.entity_id.EntityId"]
    """<p>A user-supplied ID that uniquely identifies the <code>MLModel</code>. This value should be identical to the value of the <code>MLModelId</code> in the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMLModelOutput) -> dict:
    out: dict = {}
    if "ml_model_id" in value:
        out["MLModelId"] = value["ml_model_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMLModelOutput:
    out: CreateMLModelOutput = {}  # type: ignore[typeddict-item]
    if "MLModelId" in data:
        out["ml_model_id"] = data["MLModelId"]
    return out
