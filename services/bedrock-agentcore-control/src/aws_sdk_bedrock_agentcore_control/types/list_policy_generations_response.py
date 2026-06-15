"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPolicyGenerationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.policy_generations


class ListPolicyGenerationsResponse(TypedDict):
    policy_generations: (
        "aws_sdk_bedrock_agentcore_control.types.policy_generations.PolicyGenerations"
    )
    """<p>An array of policy generation objects that match the specified criteria.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    """<p>A pagination token for retrieving additional policy generations if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyGenerationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.policy_generations

    out["policyGenerations"] = (
        aws_sdk_bedrock_agentcore_control.types.policy_generations.serialize_json(
            value["policy_generations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPolicyGenerationsResponse:
    out: ListPolicyGenerationsResponse = {}  # type: ignore[typeddict-item]
    if "policyGenerations" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_generations

        out["policy_generations"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_generations.deserialize_json(
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
