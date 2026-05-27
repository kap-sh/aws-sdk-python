"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteCapacityProviderResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.capacity_provider


class DeleteCapacityProviderResponse(TypedDict):
    capacity_provider: NotRequired[
        "aws_sdk_ecs.types.capacity_provider.CapacityProvider"
    ]
    """<p>The details of the capacity provider.</p>"""
