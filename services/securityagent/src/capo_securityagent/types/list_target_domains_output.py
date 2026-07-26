"""Generated from Smithy shape ``com.amazonaws.securityagent#ListTargetDomainsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.next_token
    import capo_securityagent.types.target_domain_summary_list


class ListTargetDomainsOutput(TypedDict, closed=True):
    target_domain_summaries: NotRequired[
        "capo_securityagent.types.target_domain_summary_list.TargetDomainSummaryList"
    ]
    """<p>The list of target domain summaries.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetDomainsOutput) -> dict:
    out: dict = {}
    if "target_domain_summaries" in value:
        import capo_securityagent.types.target_domain_summary_list

        out["targetDomainSummaries"] = (
            capo_securityagent.types.target_domain_summary_list.serialize_json(
                value["target_domain_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTargetDomainsOutput:
    out: ListTargetDomainsOutput = {}  # type: ignore[typeddict-item]
    if "targetDomainSummaries" in data:
        import capo_securityagent.types.target_domain_summary_list

        out["target_domain_summaries"] = (
            capo_securityagent.types.target_domain_summary_list.deserialize_json(
                data["targetDomainSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
