"""Generated from Smithy shape ``com.amazonaws.machinelearning#DeleteRealtimeEndpointInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id


class DeleteRealtimeEndpointInput(TypedDict):
    ml_model_id: "aws_sdk_machine_learning.types.entity_id.EntityId"
    """<p>The ID assigned to the <code>MLModel</code> during creation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRealtimeEndpointInput) -> dict:
    out: dict = {}
    out["MLModelId"] = value["ml_model_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRealtimeEndpointInput:
    out: DeleteRealtimeEndpointInput = {}  # type: ignore[typeddict-item]
    if "MLModelId" in data:
        out["ml_model_id"] = data["MLModelId"]
    else:
        raise DeserializationError("DeleteRealtimeEndpointInput.ml_model_id required")
    return out
