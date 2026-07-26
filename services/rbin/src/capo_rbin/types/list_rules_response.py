"""Generated from Smithy shape ``com.amazonaws.rbin#ListRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rbin.types.next_token
    import capo_rbin.types.rule_summary_list


class ListRulesResponse(TypedDict, closed=True):
    rules: NotRequired["capo_rbin.types.rule_summary_list.RuleSummaryList"]
    """<p>Information about the retention rules.</p>"""
    next_token: NotRequired["capo_rbin.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRulesResponse) -> dict:
    out: dict = {}
    if "rules" in value:
        import capo_rbin.types.rule_summary_list

        out["Rules"] = capo_rbin.types.rule_summary_list.serialize_json(value["rules"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRulesResponse:
    out: ListRulesResponse = {}  # type: ignore[typeddict-item]
    if "Rules" in data:
        import capo_rbin.types.rule_summary_list

        out["rules"] = capo_rbin.types.rule_summary_list.deserialize_json(data["Rules"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
