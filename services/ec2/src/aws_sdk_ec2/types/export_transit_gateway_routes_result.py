"""Generated from Smithy shape ``com.amazonaws.ec2#ExportTransitGatewayRoutesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ExportTransitGatewayRoutesResult(TypedDict):
    s3_location: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The URL of the exported file in Amazon S3. For example, s3://<i>bucket_name</i>/VPCTransitGateway/TransitGatewayRouteTables/<i>file_name</i>.</p>"""
