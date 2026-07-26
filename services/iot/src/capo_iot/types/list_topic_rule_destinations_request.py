"""Generated from Smithy shape ``com.amazonaws.iot#ListTopicRuleDestinationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.topic_rule_destination_max_results


class ListTopicRuleDestinationsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_iot.types.topic_rule_destination_max_results.TopicRuleDestinationMaxResults"
    ]
    """<p>The maximum number of results to return at one time.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTopicRuleDestinationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTopicRuleDestinationsRequest:
    out: ListTopicRuleDestinationsRequest = {}  # type: ignore[typeddict-item]
    return out
