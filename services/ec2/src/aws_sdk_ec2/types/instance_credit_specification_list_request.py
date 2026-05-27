"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceCreditSpecificationListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_credit_specification_request

InstanceCreditSpecificationListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.instance_credit_specification_request.InstanceCreditSpecificationRequest"
]
