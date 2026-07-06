"""Generated from Smithy shape ``com.amazonaws.iot#ListTopicRuleDestinationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.topic_rule_destination_summaries


class ListTopicRuleDestinationsResponse(TypedDict, closed=True):
    destination_summaries: NotRequired[
        "aws_sdk_iot.types.topic_rule_destination_summaries.TopicRuleDestinationSummaries"
    ]
    """<p>Information about a topic rule destination.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTopicRuleDestinationsResponse) -> dict:
    out: dict = {}
    if "destination_summaries" in value:
        import aws_sdk_iot.types.topic_rule_destination_summaries

        out["destinationSummaries"] = (
            aws_sdk_iot.types.topic_rule_destination_summaries.serialize_json(
                value["destination_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTopicRuleDestinationsResponse:
    out: ListTopicRuleDestinationsResponse = {}  # type: ignore[typeddict-item]
    if "destinationSummaries" in data:
        import aws_sdk_iot.types.topic_rule_destination_summaries

        out["destination_summaries"] = (
            aws_sdk_iot.types.topic_rule_destination_summaries.deserialize_json(
                data["destinationSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
