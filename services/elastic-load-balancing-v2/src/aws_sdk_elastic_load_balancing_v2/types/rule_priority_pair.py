"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RulePriorityPair``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.rule_arn
    import aws_sdk_elastic_load_balancing_v2.types.rule_priority


class RulePriorityPair(TypedDict):
    rule_arn: NotRequired["aws_sdk_elastic_load_balancing_v2.types.rule_arn.RuleArn"]
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    priority: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.rule_priority.RulePriority"
    ]
    """<p>The rule priority.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RulePriorityPair, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "rule_arn" in value:
        pairs.append((f"{prefix}.RuleArn", str(value["rule_arn"])))
    if "priority" in value:
        pairs.append((f"{prefix}.Priority", str(value["priority"])))


def deserialize_query(el: Element) -> RulePriorityPair:
    out: RulePriorityPair = {}  # type: ignore[typeddict-item]
    child_rule_arn = el.find("RuleArn")
    if child_rule_arn is not None:
        out["rule_arn"] = str(child_rule_arn.text or "")
    child_priority = el.find("Priority")
    if child_priority is not None:
        out["priority"] = int(child_priority.text or "")
    return out
