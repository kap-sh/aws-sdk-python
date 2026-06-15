"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateFlowVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.client_token
    import aws_sdk_bedrock_agent.types.flow_description
    import aws_sdk_bedrock_agent.types.flow_identifier


class CreateFlowVersionRequest(TypedDict):
    flow_identifier: "aws_sdk_bedrock_agent.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow that you want to create a version of.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agent.types.flow_description.FlowDescription"
    ]
    """<p>A description of the version of the flow.</p>"""
    client_token: NotRequired["aws_sdk_bedrock_agent.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFlowVersionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateFlowVersionRequest:
    out: CreateFlowVersionRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
