"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateCapacityProviderResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.capacity_provider


class UpdateCapacityProviderResponse(TypedDict):
    capacity_provider: NotRequired[
        "aws_sdk_ecs.types.capacity_provider.CapacityProvider"
    ]
    """<p>Details about the capacity provider.</p>"""
