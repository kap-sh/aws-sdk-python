"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateFlowDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.flow_definition_arn


class CreateFlowDefinitionResponse(TypedDict, closed=True):
    flow_definition_arn: NotRequired[
        "capo_sagemaker.types.flow_definition_arn.FlowDefinitionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the flow definition you create.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFlowDefinitionResponse) -> dict:
    out: dict = {}
    if "flow_definition_arn" in value:
        out["FlowDefinitionArn"] = value["flow_definition_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFlowDefinitionResponse:
    out: CreateFlowDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "FlowDefinitionArn" in data:
        out["flow_definition_arn"] = data["FlowDefinitionArn"]
    return out
