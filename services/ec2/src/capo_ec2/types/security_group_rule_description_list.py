"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupRuleDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.security_group_rule_description

SecurityGroupRuleDescriptionList: TypeAlias = list[
    "capo_ec2.types.security_group_rule_description.SecurityGroupRuleDescription"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupRuleDescriptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.security_group_rule_description

        capo_ec2.types.security_group_rule_description.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> SecurityGroupRuleDescriptionList:
    import capo_ec2.types.security_group_rule_description

    out: SecurityGroupRuleDescriptionList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.security_group_rule_description.deserialize_ec2_query(child)
        )
    return out
