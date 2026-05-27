"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeContainerInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_instance_field_list
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class DescribeContainerInstancesRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to describe. If you do not specify a cluster, the default cluster is assumed. This parameter is required if the container instance or container instances you are describing were launched in any cluster other than the default cluster.</p>"""
    container_instances: "aws_sdk_ecs.types.string_list.StringList"
    """<p>A list of up to 100 container instance IDs or full Amazon Resource Name (ARN) entries.</p>"""
    include: NotRequired[
        "aws_sdk_ecs.types.container_instance_field_list.ContainerInstanceFieldList"
    ]
    """<p>Specifies whether you want to see the resource tags for the container instance. If <code>TAGS</code> is specified, the tags are included in the response. If <code>CONTAINER_INSTANCE_HEALTH</code> is specified, the container instance health is included in the response. If this field is omitted, tags and container instance health status aren't included in the response.</p>"""
