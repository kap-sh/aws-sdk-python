"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateClusterSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.cluster


class UpdateClusterSettingsResponse(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.cluster.Cluster"]
    """<p>Details about the cluster</p>"""
