"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFpgaImageRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.storage_location
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateFpgaImageRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    input_storage_location: NotRequired[
        "aws_sdk_ec2.types.storage_location.StorageLocation"
    ]
    """<p>The location of the encrypted design checkpoint in Amazon S3. The input must be a tarball.</p>"""
    logs_storage_location: NotRequired[
        "aws_sdk_ec2.types.storage_location.StorageLocation"
    ]
    """<p>The location in Amazon S3 for the output logs.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the AFI.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A name for the AFI.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring Idempotency</a>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the FPGA image during creation.</p>"""
