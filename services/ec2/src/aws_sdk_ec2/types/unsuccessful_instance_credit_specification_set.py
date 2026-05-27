"""Generated from Smithy shape ``com.amazonaws.ec2#UnsuccessfulInstanceCreditSpecificationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.unsuccessful_instance_credit_specification_item

UnsuccessfulInstanceCreditSpecificationSet: TypeAlias = list[
    "aws_sdk_ec2.types.unsuccessful_instance_credit_specification_item.UnsuccessfulInstanceCreditSpecificationItem"
]
