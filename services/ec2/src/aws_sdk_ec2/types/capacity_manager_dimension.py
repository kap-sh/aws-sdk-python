"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerDimension``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_tag_dimension_set
    import aws_sdk_ec2.types.capacity_tenancy
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.reservation_end_date_type
    import aws_sdk_ec2.types.reservation_state
    import aws_sdk_ec2.types.reservation_type
    import aws_sdk_ec2.types.string


class CapacityManagerDimension(TypedDict):
    resource_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The Amazon Web Services Region where the capacity resource is located. </p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The unique identifier of the Availability Zone where the capacity resource is located. </p>"""
    account_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The Amazon Web Services account ID that owns the capacity resource. </p>"""
    account_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The name of the Amazon Web Services account that owns the capacity resource. This dimension is only available when Organizations access is enabled for Capacity Manager. </p>"""
    instance_family: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The EC2 instance family of the capacity resource. </p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The specific EC2 instance type of the capacity resource. </p>"""
    instance_platform: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The platform or operating system of the instance. </p>"""
    reservation_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The Amazon Resource Name (ARN) of the capacity reservation. This provides a unique identifier that can be used across Amazon Web Services services to reference the specific reservation. </p>"""
    reservation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The unique identifier of the capacity reservation. </p>"""
    reservation_type: NotRequired["aws_sdk_ec2.types.reservation_type.ReservationType"]
    """<p> The type of capacity reservation. </p>"""
    reservation_create_timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The timestamp when the capacity reservation was originally created, in milliseconds since epoch. This differs from the start timestamp as reservations can be created before they become active. </p>"""
    reservation_start_timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The timestamp when the capacity reservation becomes active and available for use, in milliseconds since epoch. This is when the reservation begins providing capacity. </p>"""
    reservation_end_timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The timestamp when the capacity reservation expires and is no longer available, in milliseconds since epoch. After this time, the reservation will not provide any capacity. </p>"""
    reservation_end_date_type: NotRequired[
        "aws_sdk_ec2.types.reservation_end_date_type.ReservationEndDateType"
    ]
    """<p> The type of end date for the capacity reservation. This indicates whether the reservation has a fixed end date, is open-ended, or follows a specific termination pattern. </p>"""
    tenancy: NotRequired["aws_sdk_ec2.types.capacity_tenancy.CapacityTenancy"]
    """<p> The tenancy of the EC2 instances associated with this capacity dimension. Valid values are 'default' for shared tenancy, 'dedicated' for dedicated instances, or 'host' for dedicated hosts. </p>"""
    reservation_state: NotRequired[
        "aws_sdk_ec2.types.reservation_state.ReservationState"
    ]
    """<p> The current state of the capacity reservation. </p>"""
    reservation_instance_match_criteria: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The instance matching criteria for the capacity reservation, determining how instances are matched to the reservation. </p>"""
    reservation_unused_financial_owner: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The Amazon Web Services account ID that is financially responsible for unused capacity reservation costs. </p>"""
    tags: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_tag_dimension_set.CapacityManagerTagDimensionSet"
    ]
    """<p> The tags associated with the capacity resource, represented as key-value pairs. Only tags that have been activated for monitoring via <code>UpdateCapacityManagerMonitoredTagKeys</code> are included. </p>"""
