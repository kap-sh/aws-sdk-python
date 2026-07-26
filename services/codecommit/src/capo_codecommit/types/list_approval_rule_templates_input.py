"""Generated from Smithy shape ``com.amazonaws.codecommit#ListApprovalRuleTemplatesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.max_results
    import capo_codecommit.types.next_token


class ListApprovalRuleTemplatesInput(TypedDict, closed=True):
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>"""
    max_results: NotRequired["capo_codecommit.types.max_results.MaxResults"]
    """<p>A non-zero, non-negative integer used to limit the number of returned results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApprovalRuleTemplatesInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApprovalRuleTemplatesInput:
    out: ListApprovalRuleTemplatesInput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
