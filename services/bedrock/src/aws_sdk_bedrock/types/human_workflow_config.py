"""Generated from Smithy shape ``com.amazonaws.bedrock#HumanWorkflowConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.human_task_instructions
    import aws_sdk_bedrock.types.sage_maker_flow_definition_arn


class HumanWorkflowConfig(TypedDict):
    flow_definition_arn: "aws_sdk_bedrock.types.sage_maker_flow_definition_arn.SageMakerFlowDefinitionArn"
    """<p>The Amazon Resource Number (ARN) for the flow definition</p>"""
    instructions: NotRequired[
        "aws_sdk_bedrock.types.human_task_instructions.HumanTaskInstructions"
    ]
    """<p>Instructions for the flow definition</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HumanWorkflowConfig) -> dict:
    out: dict = {}
    out["flowDefinitionArn"] = value["flow_definition_arn"]
    if "instructions" in value:
        out["instructions"] = value["instructions"]
    return out


def deserialize_json(data: dict) -> HumanWorkflowConfig:
    out: HumanWorkflowConfig = {}  # type: ignore[typeddict-item]
    if "flowDefinitionArn" in data:
        out["flow_definition_arn"] = data["flowDefinitionArn"]
    else:
        raise DeserializationError("HumanWorkflowConfig.flow_definition_arn required")
    if "instructions" in data:
        out["instructions"] = data["instructions"]
    return out
