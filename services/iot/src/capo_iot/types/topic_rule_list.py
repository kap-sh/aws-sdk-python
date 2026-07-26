"""Generated from Smithy shape ``com.amazonaws.iot#TopicRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.topic_rule_list_item

TopicRuleList: TypeAlias = list["capo_iot.types.topic_rule_list_item.TopicRuleListItem"]


# --- restJson1 ser/de ---
def serialize_json(value: TopicRuleList) -> list:
    import capo_iot.types.topic_rule_list_item

    out: list = []
    for item in value:
        out.append(capo_iot.types.topic_rule_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicRuleList:
    import capo_iot.types.topic_rule_list_item

    out: TopicRuleList = []
    for item in data:
        out.append(capo_iot.types.topic_rule_list_item.deserialize_json(item))
    return out
