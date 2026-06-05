"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupRuleList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_rule

SecurityGroupRuleList: TypeAlias = list[
    "aws_sdk_ec2.types.security_group_rule.SecurityGroupRule"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupRuleList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.security_group_rule

        aws_sdk_ec2.types.security_group_rule.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> SecurityGroupRuleList:
    import aws_sdk_ec2.types.security_group_rule

    out: SecurityGroupRuleList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.security_group_rule.deserialize_ec2_query(child))
    return out
