"""Generated from Smithy shape ``com.amazonaws.ec2#CreateReservedInstancesListingRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.price_schedule_specification_list
    import aws_sdk_ec2.types.reservation_id
    import aws_sdk_ec2.types.string


class CreateReservedInstancesListingRequest(TypedDict):
    reserved_instances_id: NotRequired["aws_sdk_ec2.types.reservation_id.ReservationId"]
    """<p>The ID of the active Standard Reserved Instance.</p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances that are a part of a Reserved Instance account to be listed in the Reserved Instance Marketplace. This number should be less than or equal to the instance count associated with the Reserved Instance ID specified in this call.</p>"""
    price_schedules: NotRequired[
        "aws_sdk_ec2.types.price_schedule_specification_list.PriceScheduleSpecificationList"
    ]
    """<p>A list specifying the price of the Standard Reserved Instance for each month remaining in the Reserved Instance term.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier you provide to ensure idempotency of your listings. This helps avoid duplicate listings. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>"""
