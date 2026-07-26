"""Generated from Smithy shape ``com.amazonaws.bedrockagent#LambdaFunctionFlowNodeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_lambda_arn


class LambdaFunctionFlowNodeConfiguration(TypedDict, closed=True):
    lambda_arn: "capo_bedrock_agent.types.flow_lambda_arn.FlowLambdaArn"
    """<p>The Amazon Resource Name (ARN) of the Lambda function to invoke.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaFunctionFlowNodeConfiguration) -> dict:
    out: dict = {}
    out["lambdaArn"] = value.get("lambda_arn", "")
    return out


def deserialize_json(data: dict) -> LambdaFunctionFlowNodeConfiguration:
    out: LambdaFunctionFlowNodeConfiguration = {}  # type: ignore[typeddict-item]
    if "lambdaArn" in data:
        out["lambda_arn"] = data["lambdaArn"]
    else:
        out["lambda_arn"] = ""
    return out
