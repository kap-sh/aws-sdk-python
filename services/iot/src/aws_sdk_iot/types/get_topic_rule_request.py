"""Generated from Smithy shape ``com.amazonaws.iot#GetTopicRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.rule_name


class GetTopicRuleRequest(TypedDict):
    rule_name: "aws_sdk_iot.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTopicRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTopicRuleRequest:
    out: GetTopicRuleRequest = {}  # type: ignore[typeddict-item]
    return out
