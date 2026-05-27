"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowDisassociationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dedicated_host_id_list
    import aws_sdk_ec2.types.instance_id_list
    import aws_sdk_ec2.types.tag_list


class InstanceEventWindowDisassociationRequest(TypedDict):
    instance_ids: NotRequired["aws_sdk_ec2.types.instance_id_list.InstanceIdList"]
    """<p>The IDs of the instances to disassociate from the event window.</p>"""
    instance_tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The instance tags to disassociate from the event window. Any instances associated with the tags will be disassociated from the event window.</p>"""
    dedicated_host_ids: NotRequired[
        "aws_sdk_ec2.types.dedicated_host_id_list.DedicatedHostIdList"
    ]
    """<p>The IDs of the Dedicated Hosts to disassociate from the event window.</p>"""
