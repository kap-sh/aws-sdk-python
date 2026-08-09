"""Generated from Smithy shape ``com.amazonaws.ec2#RuleGroupTypePairList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.rule_group_type_pair

RuleGroupTypePairList: TypeAlias = list[
    "capo_ec2.types.rule_group_type_pair.RuleGroupTypePair"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RuleGroupTypePairList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.rule_group_type_pair

        capo_ec2.types.rule_group_type_pair.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> RuleGroupTypePairList:
    import capo_ec2.types.rule_group_type_pair

    out: RuleGroupTypePairList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.rule_group_type_pair.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> RuleGroupTypePairList:
    import capo_ec2.types.rule_group_type_pair

    out: RuleGroupTypePairList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.rule_group_type_pair.deserialize_ec2_query(child))
    return out
