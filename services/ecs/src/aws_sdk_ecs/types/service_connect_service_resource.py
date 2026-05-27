"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectServiceResource``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ServiceConnectServiceResource(TypedDict):
    discovery_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The discovery name of this Service Connect resource.</p> <p>The <code>discoveryName</code> is the name of the new Cloud Map service that Amazon ECS creates for this Amazon ECS service. This must be unique within the Cloud Map namespace. The name can contain up to 64 characters. The name can include lowercase letters, numbers, underscores (_), and hyphens (-). The name can't start with a hyphen.</p> <p>If the <code>discoveryName</code> isn't specified, the port mapping name from the task definition is used in <code>portName.namespace</code>.</p>"""
    discovery_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the service in Cloud Map that matches the discovery name for this Service Connect resource. You can use this ARN in other integrations with Cloud Map. However, Service Connect can't ensure connectivity outside of Amazon ECS.</p>"""
