"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.next_token
    import aws_sdk_resiliencehubv2.types.policy_summary_list


class ListPoliciesResponse(TypedDict, closed=True):
    policy_summaries: (
        "aws_sdk_resiliencehubv2.types.policy_summary_list.PolicySummaryList"
    )
    """<p>The list of policy summaries.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListPoliciesResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.policy_summary_list

    out["policySummaries"] = (
        aws_sdk_resiliencehubv2.types.policy_summary_list.serialize_json(
            value["policy_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPoliciesResponse:
    out: ListPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "policySummaries" in data:
        import aws_sdk_resiliencehubv2.types.policy_summary_list

        out["policy_summaries"] = (
            aws_sdk_resiliencehubv2.types.policy_summary_list.deserialize_json(
                data["policySummaries"]
            )
        )
    else:
        raise DeserializationError("ListPoliciesResponse.policy_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
