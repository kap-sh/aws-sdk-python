"""Generated from Smithy shape ``com.amazonaws.ec2#RuleOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.rule_option

RuleOptionList: TypeAlias = list["capo_ec2.types.rule_option.RuleOption"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RuleOptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.rule_option

        capo_ec2.types.rule_option.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> RuleOptionList:
    import capo_ec2.types.rule_option

    out: RuleOptionList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.rule_option.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> RuleOptionList:
    import capo_ec2.types.rule_option

    out: RuleOptionList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.rule_option.deserialize_ec2_query(child))
    return out
