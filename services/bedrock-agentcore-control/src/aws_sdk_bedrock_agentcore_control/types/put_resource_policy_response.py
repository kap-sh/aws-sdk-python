"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.resource_policy_body


class PutResourcePolicyResponse(TypedDict):
    policy: "aws_sdk_bedrock_agentcore_control.types.resource_policy_body.ResourcePolicyBody"
    """<p>The resource policy that was created or updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("PutResourcePolicyResponse.policy required")
    return out
