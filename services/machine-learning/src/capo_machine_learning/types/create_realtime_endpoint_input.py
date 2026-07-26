"""Generated from Smithy shape ``com.amazonaws.machinelearning#CreateRealtimeEndpointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id


class CreateRealtimeEndpointInput(TypedDict, closed=True):
    ml_model_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>The ID assigned to the <code>MLModel</code> during creation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRealtimeEndpointInput) -> dict:
    out: dict = {}
    out["MLModelId"] = value["ml_model_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRealtimeEndpointInput:
    out: CreateRealtimeEndpointInput = {}  # type: ignore[typeddict-item]
    if "MLModelId" in data:
        out["ml_model_id"] = data["MLModelId"]
    else:
        raise DeserializationError("CreateRealtimeEndpointInput.ml_model_id required")
    return out
