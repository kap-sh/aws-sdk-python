"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetRequestConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.activity_status
    import aws_sdk_ec2.types.batch_state
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.spot_fleet_request_config_data
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class SpotFleetRequestConfig(TypedDict):
    activity_status: NotRequired["aws_sdk_ec2.types.activity_status.ActivityStatus"]
    """<p>The progress of the Spot Fleet request. If there is an error, the status is <code>error</code>. After all requests are placed, the status is <code>pending_fulfillment</code>. If the size of the fleet is equal to or greater than its target capacity, the status is <code>fulfilled</code>. If the size of the fleet is decreased, the status is <code>pending_termination</code> while Spot Instances are terminating.</p>"""
    create_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The creation date and time of the request.</p>"""
    spot_fleet_request_config: NotRequired[
        "aws_sdk_ec2.types.spot_fleet_request_config_data.SpotFleetRequestConfigData"
    ]
    """<p>The configuration of the Spot Fleet request.</p>"""
    spot_fleet_request_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Spot Fleet request.</p>"""
    spot_fleet_request_state: NotRequired["aws_sdk_ec2.types.batch_state.BatchState"]
    """<p>The state of the Spot Fleet request.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for a Spot Fleet resource.</p>"""
