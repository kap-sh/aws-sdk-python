"""Generated from Smithy shape ``com.amazonaws.ec2#ConditionValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.condition_value

ConditionValueList: TypeAlias = list["aws_sdk_ec2.types.condition_value.ConditionValue"]
