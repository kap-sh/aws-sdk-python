"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeFlowDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.flow_definition_name


class DescribeFlowDefinitionRequest(TypedDict):
    flow_definition_name: NotRequired[
        "aws_sdk_sagemaker.types.flow_definition_name.FlowDefinitionName"
    ]
    """<p>The name of the flow definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFlowDefinitionRequest) -> dict:
    out: dict = {}
    if "flow_definition_name" in value:
        out["FlowDefinitionName"] = value["flow_definition_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFlowDefinitionRequest:
    out: DescribeFlowDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "FlowDefinitionName" in data:
        out["flow_definition_name"] = data["FlowDefinitionName"]
    return out
