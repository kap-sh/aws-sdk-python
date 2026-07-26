"""Generated from Smithy shape ``com.amazonaws.inspector2#ListFindingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.finding_list
    import capo_inspector2.types.next_token


class ListFindingsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""
    findings: NotRequired["capo_inspector2.types.finding_list.FindingList"]
    """<p>Contains details on the findings in your environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "findings" in value:
        import capo_inspector2.types.finding_list

        out["findings"] = capo_inspector2.types.finding_list.serialize_json(
            value["findings"]
        )
    return out


def deserialize_json(data: dict) -> ListFindingsResponse:
    out: ListFindingsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "findings" in data:
        import capo_inspector2.types.finding_list

        out["findings"] = capo_inspector2.types.finding_list.deserialize_json(
            data["findings"]
        )
    return out
