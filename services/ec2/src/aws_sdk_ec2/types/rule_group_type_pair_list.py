"""Generated from Smithy shape ``com.amazonaws.ec2#RuleGroupTypePairList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.rule_group_type_pair

RuleGroupTypePairList: TypeAlias = list[
    "aws_sdk_ec2.types.rule_group_type_pair.RuleGroupTypePair"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RuleGroupTypePairList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.rule_group_type_pair

        aws_sdk_ec2.types.rule_group_type_pair.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> RuleGroupTypePairList:
    import aws_sdk_ec2.types.rule_group_type_pair

    out: RuleGroupTypePairList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.rule_group_type_pair.deserialize_ec2_query(child))
    return out
