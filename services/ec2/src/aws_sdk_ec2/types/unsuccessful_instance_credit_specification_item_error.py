"""Generated from Smithy shape ``com.amazonaws.ec2#UnsuccessfulInstanceCreditSpecificationItemError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.unsuccessful_instance_credit_specification_error_code


class UnsuccessfulInstanceCreditSpecificationItemError(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.unsuccessful_instance_credit_specification_error_code.UnsuccessfulInstanceCreditSpecificationErrorCode"
    ]
    """<p>The error code.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The applicable error message.</p>"""
