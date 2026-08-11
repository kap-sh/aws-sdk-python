"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupRuleUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.security_group_rule_update

SecurityGroupRuleUpdateList: TypeAlias = list[
    "capo_ec2.types.security_group_rule_update.SecurityGroupRuleUpdate"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupRuleUpdateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.security_group_rule_update

        capo_ec2.types.security_group_rule_update.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> SecurityGroupRuleUpdateList:
    import capo_ec2.types.security_group_rule_update

    out: SecurityGroupRuleUpdateList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.security_group_rule_update.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> SecurityGroupRuleUpdateList:
    import capo_ec2.types.security_group_rule_update

    out: SecurityGroupRuleUpdateList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.security_group_rule_update.deserialize_ec2_query(child)
        )
    return out
