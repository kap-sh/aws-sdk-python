"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RuleConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.rule_condition

RuleConditionList: TypeAlias = list[
    "capo_elastic_load_balancing_v2.types.rule_condition.RuleCondition"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RuleConditionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.rule_condition

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.rule_condition.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> RuleConditionList:
    import capo_elastic_load_balancing_v2.types.rule_condition

    out: RuleConditionList = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing_v2.types.rule_condition.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: RuleConditionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.rule_condition

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.rule_condition.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RuleConditionList:
    import capo_elastic_load_balancing_v2.types.rule_condition

    out: RuleConditionList = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing_v2.types.rule_condition.deserialize_query(child)
        )
    return out
