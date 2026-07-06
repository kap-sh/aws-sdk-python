"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPolicyEngineSummariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.policy_engine_summary_list


class ListPolicyEngineSummariesResponse(TypedDict, closed=True):
    policy_engines: "aws_sdk_bedrock_agentcore_control.types.policy_engine_summary_list.PolicyEngineSummaryList"
    """<p>An array of policy engine summary objects that exist in the account. Each summary contains resource identifiers, status, and timestamps without customer-encrypted content.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    r"""<p>A pagination token that can be used in subsequent <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyEngineSummaries.html\">ListPolicyEngineSummaries</a> calls to retrieve additional results. This token is only present when there are more results available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyEngineSummariesResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.policy_engine_summary_list

    out["policyEngines"] = (
        aws_sdk_bedrock_agentcore_control.types.policy_engine_summary_list.serialize_json(
            value["policy_engines"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPolicyEngineSummariesResponse:
    out: ListPolicyEngineSummariesResponse = {}  # type: ignore[typeddict-item]
    if "policyEngines" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_engine_summary_list

        out["policy_engines"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_engine_summary_list.deserialize_json(
                data["policyEngines"]
            )
        )
    else:
        raise DeserializationError(
            "ListPolicyEngineSummariesResponse.policy_engines required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
