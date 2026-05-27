"""Generated from Smithy shape ``com.amazonaws.ec2#CreateKeyPairRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.key_format
    import aws_sdk_ec2.types.key_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateKeyPairRequest(TypedDict):
    key_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique name for the key pair.</p> <p>Constraints: Up to 255 ASCII characters</p>"""
    key_type: NotRequired["aws_sdk_ec2.types.key_type.KeyType"]
    """<p>The type of key pair. Note that ED25519 keys are not supported for Windows instances.</p> <p>Default: <code>rsa</code> </p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the new key pair.</p>"""
    key_format: NotRequired["aws_sdk_ec2.types.key_format.KeyFormat"]
    """<p>The format of the key pair.</p> <p>Default: <code>pem</code> </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
