"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteCapacityProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DeleteCapacityProviderRequest(TypedDict):
    capacity_provider: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the capacity provider to delete.</p>"""
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the cluster that contains the capacity provider to delete. Managed instances capacity providers are cluster-scoped and can only be deleted from their associated cluster.</p>"""
