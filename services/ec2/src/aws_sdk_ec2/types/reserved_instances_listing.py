"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesListing``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.instance_count_list
    import aws_sdk_ec2.types.listing_status
    import aws_sdk_ec2.types.price_schedule_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ReservedInstancesListing(TypedDict):
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive key supplied by the client to ensure that the request is idempotent. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>"""
    create_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time the listing was created.</p>"""
    instance_counts: NotRequired[
        "aws_sdk_ec2.types.instance_count_list.InstanceCountList"
    ]
    """<p>The number of instances in this state.</p>"""
    price_schedules: NotRequired[
        "aws_sdk_ec2.types.price_schedule_list.PriceScheduleList"
    ]
    """<p>The price of the Reserved Instance listing.</p>"""
    reserved_instances_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Reserved Instance.</p>"""
    reserved_instances_listing_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Reserved Instance listing.</p>"""
    status: NotRequired["aws_sdk_ec2.types.listing_status.ListingStatus"]
    """<p>The status of the Reserved Instance listing.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for the current status of the Reserved Instance listing. The response can be blank.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the resource.</p>"""
    update_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The last modified timestamp of the listing.</p>"""
