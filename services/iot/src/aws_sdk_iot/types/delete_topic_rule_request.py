"""Generated from Smithy shape ``com.amazonaws.iot#DeleteTopicRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.rule_name


class DeleteTopicRuleRequest(TypedDict):
    rule_name: "aws_sdk_iot.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTopicRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTopicRuleRequest:
    out: DeleteTopicRuleRequest = {}  # type: ignore[typeddict-item]
    return out
