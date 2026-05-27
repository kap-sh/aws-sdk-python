"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageReport``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.image_usage_report_id
    import aws_sdk_ec2.types.image_usage_report_state
    import aws_sdk_ec2.types.image_usage_report_state_reason
    import aws_sdk_ec2.types.image_usage_resource_type_list
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.user_id_list


class ImageUsageReport(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the image that was specified when the report was created.</p>"""
    report_id: NotRequired["aws_sdk_ec2.types.image_usage_report_id.ImageUsageReportId"]
    """<p>The ID of the report.</p>"""
    resource_types: NotRequired[
        "aws_sdk_ec2.types.image_usage_resource_type_list.ImageUsageResourceTypeList"
    ]
    """<p>The resource types that were specified when the report was created.</p>"""
    account_ids: NotRequired["aws_sdk_ec2.types.user_id_list.UserIdList"]
    """<p>The IDs of the Amazon Web Services accounts that were specified when the report was created.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.image_usage_report_state.ImageUsageReportState"
    ]
    """<p>The current state of the report. Possible values:</p> <ul> <li> <p> <code>available</code> - The report is available to view.</p> </li> <li> <p> <code>pending</code> - The report is being created and not available to view.</p> </li> <li> <p> <code>error</code> - The report could not be created.</p> </li> </ul>"""
    state_reason: NotRequired[
        "aws_sdk_ec2.types.image_usage_report_state_reason.ImageUsageReportStateReason"
    ]
    """<p>Provides additional details when the report is in an <code>error</code> state.</p>"""
    creation_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the report was created.</p>"""
    expiration_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when Amazon EC2 will delete the report (30 days after the report was created).</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the report.</p>"""
