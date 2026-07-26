"""Generated from Smithy shape ``com.amazonaws.iot#ListTopicRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.is_disabled
    import capo_iot.types.next_token
    import capo_iot.types.topic
    import capo_iot.types.topic_rule_max_results


class ListTopicRulesRequest(TypedDict, closed=True):
    topic: NotRequired["capo_iot.types.topic.Topic"]
    """<p>The topic.</p>"""
    max_results: NotRequired[
        "capo_iot.types.topic_rule_max_results.TopicRuleMaxResults"
    ]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    rule_disabled: NotRequired["capo_iot.types.is_disabled.IsDisabled"]
    """<p>Specifies whether the rule is disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTopicRulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTopicRulesRequest:
    out: ListTopicRulesRequest = {}  # type: ignore[typeddict-item]
    return out
