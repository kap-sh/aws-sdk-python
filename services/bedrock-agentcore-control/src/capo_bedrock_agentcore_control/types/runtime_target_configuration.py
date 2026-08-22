"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RuntimeTargetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.runtime_arn
    import capo_bedrock_agentcore_control.types.runtime_qualifier


class RuntimeTargetConfiguration(TypedDict, closed=True):
    arn: "capo_bedrock_agentcore_control.types.runtime_arn.RuntimeArn"
    """<p>The Amazon Resource Name (ARN) of the AgentCore Runtime to route requests to.</p>"""
    qualifier: NotRequired[
        "capo_bedrock_agentcore_control.types.runtime_qualifier.RuntimeQualifier"
    ]
    """<p>The qualifier for the agent runtime, used to target a specific endpoint version. If not specified, the default endpoint is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeTargetConfiguration) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "qualifier" in value:
        out["qualifier"] = value["qualifier"]
    return out


def deserialize_json(data: dict) -> RuntimeTargetConfiguration:
    out: RuntimeTargetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("RuntimeTargetConfiguration.arn required")
    if data.get("qualifier") is not None:
        out["qualifier"] = data["qualifier"]
    return out
