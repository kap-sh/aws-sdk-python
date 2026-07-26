"""Generated from Smithy shape ``com.amazonaws.securityagent#ListFindingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.finding_summary_list
    import capo_securityagent.types.next_token


class ListFindingsOutput(TypedDict, closed=True):
    findings_summaries: NotRequired[
        "capo_securityagent.types.finding_summary_list.FindingSummaryList"
    ]
    """<p>The list of finding summaries.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsOutput) -> dict:
    out: dict = {}
    if "findings_summaries" in value:
        import capo_securityagent.types.finding_summary_list

        out["findingsSummaries"] = (
            capo_securityagent.types.finding_summary_list.serialize_json(
                value["findings_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFindingsOutput:
    out: ListFindingsOutput = {}  # type: ignore[typeddict-item]
    if "findingsSummaries" in data:
        import capo_securityagent.types.finding_summary_list

        out["findings_summaries"] = (
            capo_securityagent.types.finding_summary_list.deserialize_json(
                data["findingsSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
