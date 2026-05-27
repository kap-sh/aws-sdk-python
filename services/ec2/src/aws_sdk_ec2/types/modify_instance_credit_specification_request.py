"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceCreditSpecificationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_credit_specification_list_request
    import aws_sdk_ec2.types.string


class ModifyInstanceCreditSpecificationRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>"""
    instance_credit_specifications: NotRequired[
        "aws_sdk_ec2.types.instance_credit_specification_list_request.InstanceCreditSpecificationListRequest"
    ]
    """<p>Information about the credit option for CPU usage.</p>"""
