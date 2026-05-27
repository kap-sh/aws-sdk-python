"""Generated from Smithy shape ``com.amazonaws.ec2#RuleOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.rule_option

RuleOptionList: TypeAlias = list["aws_sdk_ec2.types.rule_option.RuleOption"]
