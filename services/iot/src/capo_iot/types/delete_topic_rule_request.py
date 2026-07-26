"""Generated from Smithy shape ``com.amazonaws.iot#DeleteTopicRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.rule_name


class DeleteTopicRuleRequest(TypedDict, closed=True):
    rule_name: "capo_iot.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTopicRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTopicRuleRequest:
    out: DeleteTopicRuleRequest = {}  # type: ignore[typeddict-item]
    return out
