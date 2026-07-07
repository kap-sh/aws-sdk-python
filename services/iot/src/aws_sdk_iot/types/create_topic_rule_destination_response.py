"""Generated from Smithy shape ``com.amazonaws.iot#CreateTopicRuleDestinationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.topic_rule_destination


class CreateTopicRuleDestinationResponse(TypedDict, closed=True):
    topic_rule_destination: NotRequired[
        "aws_sdk_iot.types.topic_rule_destination.TopicRuleDestination"
    ]
    """<p>The topic rule destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTopicRuleDestinationResponse) -> dict:
    out: dict = {}
    if "topic_rule_destination" in value:
        import aws_sdk_iot.types.topic_rule_destination

        out["topicRuleDestination"] = (
            aws_sdk_iot.types.topic_rule_destination.serialize_json(
                value["topic_rule_destination"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateTopicRuleDestinationResponse:
    out: CreateTopicRuleDestinationResponse = {}  # type: ignore[typeddict-item]
    if "topicRuleDestination" in data:
        import aws_sdk_iot.types.topic_rule_destination

        out["topic_rule_destination"] = (
            aws_sdk_iot.types.topic_rule_destination.deserialize_json(
                data["topicRuleDestination"]
            )
        )
    return out
