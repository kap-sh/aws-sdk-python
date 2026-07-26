"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPolicyGenerationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.policy_generations


class ListPolicyGenerationsResponse(TypedDict, closed=True):
    policy_generations: (
        "capo_bedrock_agentcore_control.types.policy_generations.PolicyGenerations"
    )
    """<p>An array of policy generation objects that match the specified criteria.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>A pagination token for retrieving additional policy generations if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyGenerationsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.policy_generations

    out["policyGenerations"] = (
        capo_bedrock_agentcore_control.types.policy_generations.serialize_json(
            value["policy_generations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPolicyGenerationsResponse:
    out: ListPolicyGenerationsResponse = {}  # type: ignore[typeddict-item]
    if "policyGenerations" in data:
        import capo_bedrock_agentcore_control.types.policy_generations

        out["policy_generations"] = (
            capo_bedrock_agentcore_control.types.policy_generations.deserialize_json(
                data["policyGenerations"]
            )
        )
    else:
        raise DeserializationError(
            "ListPolicyGenerationsResponse.policy_generations required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
