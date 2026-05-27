"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterServiceConnectDefaults``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ClusterServiceConnectDefaults(TypedDict):
    namespace: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The namespace name or full Amazon Resource Name (ARN) of the Cloud Map namespace. When you create a service and don't specify a Service Connect configuration, this namespace is used.</p>"""
