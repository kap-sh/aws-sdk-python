"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.resource_policy_body


class GetResourcePolicyResponse(TypedDict, closed=True):
    policy: NotRequired[
        "capo_bedrock_agentcore_control.types.resource_policy_body.ResourcePolicyBody"
    ]
    """<p>The resource policy associated with the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    return out
