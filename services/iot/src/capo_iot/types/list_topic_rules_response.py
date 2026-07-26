"""Generated from Smithy shape ``com.amazonaws.iot#ListTopicRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.topic_rule_list


class ListTopicRulesResponse(TypedDict, closed=True):
    rules: NotRequired["capo_iot.types.topic_rule_list.TopicRuleList"]
    """<p>The rules.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTopicRulesResponse) -> dict:
    out: dict = {}
    if "rules" in value:
        import capo_iot.types.topic_rule_list

        out["rules"] = capo_iot.types.topic_rule_list.serialize_json(value["rules"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTopicRulesResponse:
    out: ListTopicRulesResponse = {}  # type: ignore[typeddict-item]
    if "rules" in data:
        import capo_iot.types.topic_rule_list

        out["rules"] = capo_iot.types.topic_rule_list.deserialize_json(data["rules"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
