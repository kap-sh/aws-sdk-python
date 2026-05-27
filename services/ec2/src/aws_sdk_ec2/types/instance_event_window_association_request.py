"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dedicated_host_id_list
    import aws_sdk_ec2.types.instance_id_list
    import aws_sdk_ec2.types.tag_list


class InstanceEventWindowAssociationRequest(TypedDict):
    instance_ids: NotRequired["aws_sdk_ec2.types.instance_id_list.InstanceIdList"]
    """<p>The IDs of the instances to associate with the event window. If the instance is on a Dedicated Host, you can't specify the Instance ID parameter; you must use the Dedicated Host ID parameter.</p>"""
    instance_tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The instance tags to associate with the event window. Any instances associated with the tags will be associated with the event window.</p> <p>Note that while you can't create tag keys beginning with <code>aws:</code>, you can specify existing Amazon Web Services managed tag keys (with the <code>aws:</code> prefix) when specifying them as targets to associate with the event window.</p>"""
    dedicated_host_ids: NotRequired[
        "aws_sdk_ec2.types.dedicated_host_id_list.DedicatedHostIdList"
    ]
    """<p>The IDs of the Dedicated Hosts to associate with the event window.</p>"""
