"""Generated from Smithy shape ``com.amazonaws.machinelearning#DeleteMLModelOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id


class DeleteMLModelOutput(TypedDict):
    ml_model_id: NotRequired["aws_sdk_machine_learning.types.entity_id.EntityId"]
    """<p>A user-supplied ID that uniquely identifies the <code>MLModel</code>. This value should be identical to the value of the <code>MLModelID</code> in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMLModelOutput) -> dict:
    out: dict = {}
    if "ml_model_id" in value:
        out["MLModelId"] = value["ml_model_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMLModelOutput:
    out: DeleteMLModelOutput = {}  # type: ignore[typeddict-item]
    if "MLModelId" in data:
        out["ml_model_id"] = data["MLModelId"]
    return out
