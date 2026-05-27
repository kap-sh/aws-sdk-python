"""Generated from Smithy shape ``com.amazonaws.ec2#CopyFpgaImageRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class CopyFpgaImageRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    source_fpga_image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the source AFI.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description for the new AFI.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name for the new AFI. The default is the name of the source AFI.</p>"""
    source_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region that contains the source AFI.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
