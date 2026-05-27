"""Generated from Smithy shape ``com.amazonaws.ec2#SuccessfulInstanceCreditSpecificationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.successful_instance_credit_specification_item

SuccessfulInstanceCreditSpecificationSet: TypeAlias = list[
    "aws_sdk_ec2.types.successful_instance_credit_specification_item.SuccessfulInstanceCreditSpecificationItem"
]
