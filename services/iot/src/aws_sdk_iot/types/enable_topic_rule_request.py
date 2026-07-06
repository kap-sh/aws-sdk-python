"""Generated from Smithy shape ``com.amazonaws.iot#EnableTopicRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.rule_name


class EnableTopicRuleRequest(TypedDict, closed=True):
    rule_name: "aws_sdk_iot.types.rule_name.RuleName"
    """<p>The name of the topic rule to enable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableTopicRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> EnableTopicRuleRequest:
    out: EnableTopicRuleRequest = {}  # type: ignore[typeddict-item]
    return out
