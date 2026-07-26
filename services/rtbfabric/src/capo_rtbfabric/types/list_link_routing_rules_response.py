"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ListLinkRoutingRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.link_routing_rule_list


class ListLinkRoutingRulesResponse(TypedDict, closed=True):
    rules: NotRequired[
        "capo_rtbfabric.types.link_routing_rule_list.LinkRoutingRuleList"
    ]
    """<p>The list of routing rules for the link.</p>"""
    next_token: NotRequired["str"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLinkRoutingRulesResponse) -> dict:
    out: dict = {}
    if "rules" in value:
        import capo_rtbfabric.types.link_routing_rule_list

        out["rules"] = capo_rtbfabric.types.link_routing_rule_list.serialize_json(
            value["rules"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLinkRoutingRulesResponse:
    out: ListLinkRoutingRulesResponse = {}  # type: ignore[typeddict-item]
    if "rules" in data:
        import capo_rtbfabric.types.link_routing_rule_list

        out["rules"] = capo_rtbfabric.types.link_routing_rule_list.deserialize_json(
            data["rules"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
