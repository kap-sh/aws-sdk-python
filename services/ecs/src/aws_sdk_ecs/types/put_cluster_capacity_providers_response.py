"""Generated from Smithy shape ``com.amazonaws.ecs#PutClusterCapacityProvidersResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.cluster


class PutClusterCapacityProvidersResponse(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.cluster.Cluster"]
    """<p>Details about the cluster.</p>"""
