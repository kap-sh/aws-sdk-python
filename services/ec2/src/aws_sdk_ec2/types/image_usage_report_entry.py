"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageReportEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.image_usage_report_id
    import aws_sdk_ec2.types.image_usage_resource_type_name
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class ImageUsageReportEntry(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_ec2.types.image_usage_resource_type_name.ImageUsageResourceTypeName"
    ]
    """<p>The type of resource (<code>ec2:Instance</code> or <code>ec2:LaunchTemplate</code>).</p>"""
    report_id: NotRequired["aws_sdk_ec2.types.image_usage_report_id.ImageUsageReportId"]
    """<p>The ID of the report.</p>"""
    usage_count: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The number of times resources of this type reference this image in the account.</p>"""
    account_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the account that uses the image.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the image.</p>"""
    report_creation_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time the report creation was initiated.</p>"""
