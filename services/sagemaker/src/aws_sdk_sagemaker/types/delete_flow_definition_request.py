"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteFlowDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.flow_definition_name


class DeleteFlowDefinitionRequest(TypedDict, closed=True):
    flow_definition_name: NotRequired[
        "aws_sdk_sagemaker.types.flow_definition_name.FlowDefinitionName"
    ]
    """<p>The name of the flow definition you are deleting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFlowDefinitionRequest) -> dict:
    out: dict = {}
    if "flow_definition_name" in value:
        out["FlowDefinitionName"] = value["flow_definition_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFlowDefinitionRequest:
    out: DeleteFlowDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "FlowDefinitionName" in data:
        out["flow_definition_name"] = data["FlowDefinitionName"]
    return out
