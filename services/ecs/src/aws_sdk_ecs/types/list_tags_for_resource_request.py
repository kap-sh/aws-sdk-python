"""Generated from Smithy shape ``com.amazonaws.ecs#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) that identifies the resource to list the tags for. Currently, the supported resources are Amazon ECS tasks, services, task definitions, clusters, and container instances.</p>"""
