"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#SetRulePrioritiesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.rule_priority_list


class SetRulePrioritiesInput(TypedDict, closed=True):
    rule_priorities: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.rule_priority_list.RulePriorityList"
    ]
    """<p>The rule priorities.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetRulePrioritiesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "rule_priorities" in value:
        import aws_sdk_elastic_load_balancing_v2.types.rule_priority_list

        aws_sdk_elastic_load_balancing_v2.types.rule_priority_list.serialize_query(
            value["rule_priorities"], pairs, f"{prefix}.RulePriorities"
        )


def deserialize_query(el: Element) -> SetRulePrioritiesInput:
    out: SetRulePrioritiesInput = {}  # type: ignore[typeddict-item]
    child_rule_priorities = el.find("RulePriorities")
    if child_rule_priorities is not None:
        import aws_sdk_elastic_load_balancing_v2.types.rule_priority_list

        out["rule_priorities"] = (
            aws_sdk_elastic_load_balancing_v2.types.rule_priority_list.deserialize_query(
                child_rule_priorities
            )
        )
    return out
