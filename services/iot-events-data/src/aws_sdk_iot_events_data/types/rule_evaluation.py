"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#RuleEvaluation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.simple_rule_evaluation


class RuleEvaluation(TypedDict, closed=True):
    simple_rule_evaluation: NotRequired[
        "aws_sdk_iot_events_data.types.simple_rule_evaluation.SimpleRuleEvaluation"
    ]
    """<p>Information needed to compare two values with a comparison operator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleEvaluation) -> dict:
    out: dict = {}
    if "simple_rule_evaluation" in value:
        import aws_sdk_iot_events_data.types.simple_rule_evaluation

        out["simpleRuleEvaluation"] = (
            aws_sdk_iot_events_data.types.simple_rule_evaluation.serialize_json(
                value["simple_rule_evaluation"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuleEvaluation:
    out: RuleEvaluation = {}  # type: ignore[typeddict-item]
    if "simpleRuleEvaluation" in data:
        import aws_sdk_iot_events_data.types.simple_rule_evaluation

        out["simple_rule_evaluation"] = (
            aws_sdk_iot_events_data.types.simple_rule_evaluation.deserialize_json(
                data["simpleRuleEvaluation"]
            )
        )
    return out
