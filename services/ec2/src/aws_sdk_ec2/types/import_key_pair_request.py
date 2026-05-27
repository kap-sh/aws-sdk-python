"""Generated from Smithy shape ``com.amazonaws.ec2#ImportKeyPairRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.blob
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class ImportKeyPairRequest(TypedDict):
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the imported key pair.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    key_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique name for the key pair.</p>"""
    public_key_material: NotRequired["aws_sdk_ec2.types.blob.Blob"]
    """<p>The public key.</p>"""
