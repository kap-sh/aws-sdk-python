"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.policies


class ListPoliciesResponse(TypedDict):
    policies: "aws_sdk_bedrock_agentcore_control.types.policies.Policies"
    """<p>An array of policy objects that match the specified criteria. Each policy object contains the policy metadata, status, and key identifiers for further operations.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    """<p>A pagination token that can be used in subsequent ListPolicies calls to retrieve additional results. This token is only present when there are more results available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPoliciesResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.policies

    out["policies"] = aws_sdk_bedrock_agentcore_control.types.policies.serialize_json(
        value["policies"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPoliciesResponse:
    out: ListPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "policies" in data:
        import aws_sdk_bedrock_agentcore_control.types.policies

        out["policies"] = (
            aws_sdk_bedrock_agentcore_control.types.policies.deserialize_json(
                data["policies"]
            )
        )
    else:
        raise DeserializationError("ListPoliciesResponse.policies required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
