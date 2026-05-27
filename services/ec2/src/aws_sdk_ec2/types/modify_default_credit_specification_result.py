"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyDefaultCreditSpecificationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_family_credit_specification


class ModifyDefaultCreditSpecificationResult(TypedDict):
    instance_family_credit_specification: NotRequired[
        "aws_sdk_ec2.types.instance_family_credit_specification.InstanceFamilyCreditSpecification"
    ]
    """<p>The default credit option for CPU usage of the instance family.</p>"""
