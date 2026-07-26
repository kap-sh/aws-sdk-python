"""Generated from Smithy shape ``com.amazonaws.datapipeline#EvaluateExpressionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_data_pipeline.types.id
    import capo_data_pipeline.types.long_string


class EvaluateExpressionInput(TypedDict, closed=True):
    pipeline_id: "capo_data_pipeline.types.id.id"
    """<p>The ID of the pipeline.</p>"""
    object_id: "capo_data_pipeline.types.id.id"
    """<p>The ID of the object.</p>"""
    expression: "capo_data_pipeline.types.long_string.longString"
    """<p>The expression to evaluate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluateExpressionInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    out["objectId"] = value["object_id"]
    out["expression"] = value["expression"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluateExpressionInput:
    out: EvaluateExpressionInput = {}  # type: ignore[typeddict-item]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    else:
        raise DeserializationError("EvaluateExpressionInput.pipeline_id required")
    if "objectId" in data:
        out["object_id"] = data["objectId"]
    else:
        raise DeserializationError("EvaluateExpressionInput.object_id required")
    if "expression" in data:
        out["expression"] = data["expression"]
    else:
        raise DeserializationError("EvaluateExpressionInput.expression required")
    return out
