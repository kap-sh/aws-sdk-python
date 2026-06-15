"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPolicyEnginesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.policy_engines


class ListPolicyEnginesResponse(TypedDict):
    policy_engines: (
        "aws_sdk_bedrock_agentcore_control.types.policy_engines.PolicyEngines"
    )
    """<p>An array of policy engine objects that exist in the account. Each policy engine object contains the engine metadata, status, and key identifiers for further operations.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    r"""<p>A pagination token that can be used in subsequent <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyEngines.html\">ListPolicyEngines</a> calls to retrieve additional results. This token is only present when there are more results available. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyEnginesResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.policy_engines

    out["policyEngines"] = (
        aws_sdk_bedrock_agentcore_control.types.policy_engines.serialize_json(
            value["policy_engines"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPolicyEnginesResponse:
    out: ListPolicyEnginesResponse = {}  # type: ignore[typeddict-item]
    if "policyEngines" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_engines

        out["policy_engines"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_engines.deserialize_json(
                data["policyEngines"]
            )
        )
    else:
        raise DeserializationError("ListPolicyEnginesResponse.policy_engines required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
