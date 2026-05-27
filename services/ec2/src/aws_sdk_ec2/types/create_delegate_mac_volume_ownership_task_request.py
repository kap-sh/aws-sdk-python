"""Generated from Smithy shape ``com.amazonaws.ec2#CreateDelegateMacVolumeOwnershipTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.sensitive_mac_credentials
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateDelegateMacVolumeOwnershipTaskRequest(TypedDict):
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the Amazon EC2 Mac instance.</p>"""
    mac_credentials: NotRequired[
        "aws_sdk_ec2.types.sensitive_mac_credentials.SensitiveMacCredentials"
    ]
    """<p>Specifies the following credentials:</p> <ul> <li> <p> <b>Internal disk administrative user</b> </p> <ul> <li> <p> <b>Username</b> - Only the default administrative user (<code>aws-managed-user</code>) is supported and it is used by default. You can't specify a different administrative user.</p> </li> <li> <p> <b>Password</b> - If you did not change the default password for <code>aws-managed-user</code>, specify the default password, which is <i>blank</i>. Otherwise, specify your password.</p> </li> </ul> </li> <li> <p> <b>Amazon EBS root volume administrative user</b> </p> <ul> <li> <p> <b>Username</b> - If you did not change the default administrative user, specify <code>ec2-user</code>. Otherwise, specify the username for your administrative user.</p> </li> <li> <p> <b>Password</b> - Specify the password for the administrative user.</p> </li> </ul> </li> </ul> <p>The credentials must be specified in the following JSON format:</p> <p> <code>{ \"internalDiskPassword\":\"<i>internal-disk-admin_password</i>\", \"rootVolumeUsername\":\"<i>root-volume-admin_username</i>\", \"rootVolumepassword\":\"<i>root-volume-admin_password</i>\" }</code> </p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the volume ownership delegation task.</p>"""
