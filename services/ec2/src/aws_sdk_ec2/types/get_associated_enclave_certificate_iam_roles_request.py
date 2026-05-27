"""Generated from Smithy shape ``com.amazonaws.ec2#GetAssociatedEnclaveCertificateIamRolesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.certificate_id


class GetAssociatedEnclaveCertificateIamRolesRequest(TypedDict):
    certificate_arn: NotRequired["aws_sdk_ec2.types.certificate_id.CertificateId"]
    """<p>The ARN of the ACM certificate for which to view the associated IAM roles, encryption keys, and Amazon S3 object information.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
