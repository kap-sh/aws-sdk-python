"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StopRuntimeSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.client_token
    import aws_sdk_bedrock_agentcore.types.session_type


class StopRuntimeSessionRequest(TypedDict):
    runtime_session_id: "aws_sdk_bedrock_agentcore.types.session_type.SessionType"
    """<p>The ID of the session that you want to stop.</p>"""
    agent_runtime_arn: "str"
    """<p>The ARN of the agent that contains the session that you want to stop.</p>"""
    qualifier: NotRequired["str"]
    """<p>Optional qualifier to specify an agent alias, such as <code>prod</code>code&gt; or <code>dev</code>. If you don't provide a value, the DEFAULT alias is used. </p>"""
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore.types.client_token.ClientToken"
    ]
    """<p>Idempotent token used to identify the request. If you use the same token with multiple requests, the same response is returned. Use ClientToken to prevent the same request from being processed more than once.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopRuntimeSessionRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StopRuntimeSessionRequest:
    out: StopRuntimeSessionRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
