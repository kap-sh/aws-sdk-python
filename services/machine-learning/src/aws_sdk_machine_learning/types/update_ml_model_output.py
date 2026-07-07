"""Generated from Smithy shape ``com.amazonaws.machinelearning#UpdateMLModelOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id


class UpdateMLModelOutput(TypedDict, closed=True):
    ml_model_id: NotRequired["aws_sdk_machine_learning.types.entity_id.EntityId"]
    """<p>The ID assigned to the <code>MLModel</code> during creation. This value should be identical to the value of the <code>MLModelID</code> in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMLModelOutput) -> dict:
    out: dict = {}
    if "ml_model_id" in value:
        out["MLModelId"] = value["ml_model_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMLModelOutput:
    out: UpdateMLModelOutput = {}  # type: ignore[typeddict-item]
    if "MLModelId" in data:
        out["ml_model_id"] = data["MLModelId"]
    return out
