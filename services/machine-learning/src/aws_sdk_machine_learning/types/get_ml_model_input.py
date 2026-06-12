"""Generated from Smithy shape ``com.amazonaws.machinelearning#GetMLModelInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id
    import aws_sdk_machine_learning.types.verbose


class GetMLModelInput(TypedDict):
    ml_model_id: "aws_sdk_machine_learning.types.entity_id.EntityId"
    """<p>The ID assigned to the <code>MLModel</code> at creation.</p>"""
    verbose: "aws_sdk_machine_learning.types.verbose.Verbose"
    """<p>Specifies whether the <code>GetMLModel</code> operation should return <code>Recipe</code>.</p> <p>If true, <code>Recipe</code> is returned.</p> <p>If false, <code>Recipe</code> is not returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMLModelInput) -> dict:
    out: dict = {}
    out["MLModelId"] = value["ml_model_id"]
    out["Verbose"] = value.get("verbose", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMLModelInput:
    out: GetMLModelInput = {}  # type: ignore[typeddict-item]
    if "MLModelId" in data:
        out["ml_model_id"] = data["MLModelId"]
    else:
        raise DeserializationError("GetMLModelInput.ml_model_id required")
    if "Verbose" in data:
        out["verbose"] = data["Verbose"]
    else:
        out["verbose"] = False
    return out
