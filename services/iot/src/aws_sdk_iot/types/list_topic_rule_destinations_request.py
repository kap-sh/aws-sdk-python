"""Generated from Smithy shape ``com.amazonaws.iot#ListTopicRuleDestinationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.topic_rule_destination_max_results


class ListTopicRuleDestinationsRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_iot.types.topic_rule_destination_max_results.TopicRuleDestinationMaxResults"
    ]
    """<p>The maximum number of results to return at one time.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTopicRuleDestinationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTopicRuleDestinationsRequest:
    out: ListTopicRuleDestinationsRequest = {}  # type: ignore[typeddict-item]
    return out
