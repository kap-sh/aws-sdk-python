"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceCreditSpecificationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.successful_instance_credit_specification_set
    import aws_sdk_ec2.types.unsuccessful_instance_credit_specification_set


class ModifyInstanceCreditSpecificationResult(TypedDict):
    successful_instance_credit_specifications: NotRequired[
        "aws_sdk_ec2.types.successful_instance_credit_specification_set.SuccessfulInstanceCreditSpecificationSet"
    ]
    """<p>Information about the instances whose credit option for CPU usage was successfully modified.</p>"""
    unsuccessful_instance_credit_specifications: NotRequired[
        "aws_sdk_ec2.types.unsuccessful_instance_credit_specification_set.UnsuccessfulInstanceCreditSpecificationSet"
    ]
    """<p>Information about the instances whose credit option for CPU usage was not modified.</p>"""
