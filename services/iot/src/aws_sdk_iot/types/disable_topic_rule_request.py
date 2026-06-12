"""Generated from Smithy shape ``com.amazonaws.iot#DisableTopicRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.rule_name


class DisableTopicRuleRequest(TypedDict):
    rule_name: "aws_sdk_iot.types.rule_name.RuleName"
    """<p>The name of the rule to disable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableTopicRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisableTopicRuleRequest:
    out: DisableTopicRuleRequest = {}  # type: ignore[typeddict-item]
    return out
