"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DeleteRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.rule_arn


class DeleteRuleInput(TypedDict, closed=True):
    rule_arn: NotRequired["capo_elastic_load_balancing_v2.types.rule_arn.RuleArn"]
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteRuleInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "rule_arn" in value:
        pairs.append((f"{prefix}.RuleArn", str(value["rule_arn"])))


def deserialize_query(el: Element) -> DeleteRuleInput:
    out: DeleteRuleInput = {}  # type: ignore[typeddict-item]
    child_rule_arn = el.find("RuleArn")
    if child_rule_arn is not None:
        out["rule_arn"] = str(child_rule_arn.text or "")
    return out
