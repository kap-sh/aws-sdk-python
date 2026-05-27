"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteClusterResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.cluster


class DeleteClusterResponse(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.cluster.Cluster"]
    """<p>The full description of the deleted cluster.</p>"""
