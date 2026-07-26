"""Generated from Smithy shape ``com.amazonaws.iot#TopicRuleDestinationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.topic_rule_destination_summary

TopicRuleDestinationSummaries: TypeAlias = list[
    "capo_iot.types.topic_rule_destination_summary.TopicRuleDestinationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicRuleDestinationSummaries) -> list:
    import capo_iot.types.topic_rule_destination_summary

    out: list = []
    for item in value:
        out.append(capo_iot.types.topic_rule_destination_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicRuleDestinationSummaries:
    import capo_iot.types.topic_rule_destination_summary

    out: TopicRuleDestinationSummaries = []
    for item in data:
        out.append(capo_iot.types.topic_rule_destination_summary.deserialize_json(item))
    return out
