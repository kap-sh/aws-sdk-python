"""Generated from Smithy shape ``com.amazonaws.ec2#DiskImageDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disk_image_format
    import aws_sdk_ec2.types.import_manifest_url
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.string


class DiskImageDescription(TypedDict):
    checksum: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The checksum computed for the disk image.</p>"""
    format: NotRequired["aws_sdk_ec2.types.disk_image_format.DiskImageFormat"]
    """<p>The disk image format.</p>"""
    import_manifest_url: NotRequired[
        "aws_sdk_ec2.types.import_manifest_url.ImportManifestUrl"
    ]
    """<p>A presigned URL for the import manifest stored in Amazon S3. For information about creating a presigned URL for an Amazon S3 object, read the \"Query String Request Authentication Alternative\" section of the <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html\">Authenticating REST Requests</a> topic in the <i>Amazon Simple Storage Service Developer Guide</i>.</p> <p>For information about the import manifest referenced by this API action, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/manifest.html\">VM Import Manifest</a>.</p>"""
    size: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The size of the disk image, in GiB.</p>"""
