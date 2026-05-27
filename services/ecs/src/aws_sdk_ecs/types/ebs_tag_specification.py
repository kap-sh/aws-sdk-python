"""Generated from Smithy shape ``com.amazonaws.ecs#EBSTagSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.ebs_resource_type
    import aws_sdk_ecs.types.propagate_tags
    import aws_sdk_ecs.types.tags


class EBSTagSpecification(TypedDict):
    resource_type: "aws_sdk_ecs.types.ebs_resource_type.EBSResourceType"
    """<p>The type of volume resource.</p>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The tags applied to this Amazon EBS volume. <code>AmazonECSCreated</code> and <code>AmazonECSManaged</code> are reserved tags that can't be used.</p>"""
    propagate_tags: NotRequired["aws_sdk_ecs.types.propagate_tags.PropagateTags"]
    """<p>Determines whether to propagate the tags from the task definition to the Amazon EBS volume. Tags can only propagate to a <code>SERVICE</code> specified in <code>ServiceVolumeConfiguration</code>. If no value is specified, the tags aren't propagated.</p>"""
