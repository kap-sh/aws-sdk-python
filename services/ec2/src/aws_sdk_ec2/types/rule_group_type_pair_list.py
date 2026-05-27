"""Generated from Smithy shape ``com.amazonaws.ec2#RuleGroupTypePairList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.rule_group_type_pair

RuleGroupTypePairList: TypeAlias = list[
    "aws_sdk_ec2.types.rule_group_type_pair.RuleGroupTypePair"
]
