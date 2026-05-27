"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateEnclaveCertificateIamRoleRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.certificate_id
    import aws_sdk_ec2.types.role_id


class AssociateEnclaveCertificateIamRoleRequest(TypedDict):
    certificate_arn: NotRequired["aws_sdk_ec2.types.certificate_id.CertificateId"]
    """<p>The ARN of the ACM certificate with which to associate the IAM role.</p>"""
    role_arn: NotRequired["aws_sdk_ec2.types.role_id.RoleId"]
    """<p>The ARN of the IAM role to associate with the ACM certificate. You can associate up to 16 IAM roles with an ACM certificate.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
