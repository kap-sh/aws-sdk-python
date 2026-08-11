"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.security_group_rule

SecurityGroupRuleList: TypeAlias = list[
    "capo_ec2.types.security_group_rule.SecurityGroupRule"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupRuleList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.security_group_rule

        capo_ec2.types.security_group_rule.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> SecurityGroupRuleList:
    import capo_ec2.types.security_group_rule

    out: SecurityGroupRuleList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.security_group_rule.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> SecurityGroupRuleList:
    import capo_ec2.types.security_group_rule

    out: SecurityGroupRuleList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.security_group_rule.deserialize_ec2_query(child))
    return out
