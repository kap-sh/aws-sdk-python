"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceCreditSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_credit_specification

InstanceCreditSpecificationList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_credit_specification.InstanceCreditSpecification"
]
