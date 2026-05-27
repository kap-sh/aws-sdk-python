"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindow``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_event_window_association_target
    import aws_sdk_ec2.types.instance_event_window_cron_expression
    import aws_sdk_ec2.types.instance_event_window_id
    import aws_sdk_ec2.types.instance_event_window_state
    import aws_sdk_ec2.types.instance_event_window_time_range_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class InstanceEventWindow(TypedDict):
    instance_event_window_id: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_id.InstanceEventWindowId"
    ]
    """<p>The ID of the event window.</p>"""
    time_ranges: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_time_range_list.InstanceEventWindowTimeRangeList"
    ]
    """<p>One or more time ranges defined for the event window.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the event window.</p>"""
    cron_expression: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_cron_expression.InstanceEventWindowCronExpression"
    ]
    """<p>The cron expression defined for the event window.</p>"""
    association_target: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_association_target.InstanceEventWindowAssociationTarget"
    ]
    """<p>One or more targets associated with the event window.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_state.InstanceEventWindowState"
    ]
    """<p>The current state of the event window.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The instance tags associated with the event window.</p>"""
