"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.initialization_status_details
    import aws_sdk_ec2.types.operator_response
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_status_actions_list
    import aws_sdk_ec2.types.volume_status_attachment_status_list
    import aws_sdk_ec2.types.volume_status_events_list
    import aws_sdk_ec2.types.volume_status_info


class VolumeStatusItem(TypedDict):
    actions: NotRequired[
        "aws_sdk_ec2.types.volume_status_actions_list.VolumeStatusActionsList"
    ]
    """<p>The details of the operation.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone of the volume.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost.</p>"""
    events: NotRequired[
        "aws_sdk_ec2.types.volume_status_events_list.VolumeStatusEventsList"
    ]
    """<p>A list of events associated with the volume.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The volume ID.</p>"""
    volume_status: NotRequired["aws_sdk_ec2.types.volume_status_info.VolumeStatusInfo"]
    """<p>The volume status.</p>"""
    attachment_statuses: NotRequired[
        "aws_sdk_ec2.types.volume_status_attachment_status_list.VolumeStatusAttachmentStatusList"
    ]
    """<p>Information about the instances to which the volume is attached.</p>"""
    initialization_status_details: NotRequired[
        "aws_sdk_ec2.types.initialization_status_details.InitializationStatusDetails"
    ]
    """<p>Information about the volume initialization. It can take up to 5 minutes for the volume initialization information to be updated.</p> <p>Only available for volumes created from snapshots. Not available for empty volumes created without a snapshot.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html\"> Initialize Amazon EBS volumes</a>.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the resource.</p>"""
