"""Generated from Smithy shape ``com.amazonaws.ec2#Reservation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.group_identifier_list
    import aws_sdk_ec2.types.instance_list
    import aws_sdk_ec2.types.string


class Reservation(TypedDict):
    reservation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the reservation.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the reservation.</p>"""
    requester_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the requester that launched the instances on your behalf (for example, Amazon Web Services Management Console or Auto Scaling).</p>"""
    groups: NotRequired["aws_sdk_ec2.types.group_identifier_list.GroupIdentifierList"]
    """<p>Not supported.</p>"""
    instances: NotRequired["aws_sdk_ec2.types.instance_list.InstanceList"]
    """<p>The instances.</p>"""
