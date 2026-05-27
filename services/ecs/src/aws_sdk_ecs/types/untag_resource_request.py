"""Generated from Smithy shape ``com.amazonaws.ecs#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.tag_keys


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the resource to delete tags from. Currently, the supported resources are Amazon ECS capacity providers, tasks, services, task definitions, clusters, and container instances.</p>"""
    tag_keys: "aws_sdk_ecs.types.tag_keys.TagKeys"
    """<p>The keys of the tags to be removed.</p>"""
