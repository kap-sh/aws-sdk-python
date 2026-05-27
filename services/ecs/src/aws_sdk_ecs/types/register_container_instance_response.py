"""Generated from Smithy shape ``com.amazonaws.ecs#RegisterContainerInstanceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_instance


class RegisterContainerInstanceResponse(TypedDict):
    container_instance: NotRequired[
        "aws_sdk_ecs.types.container_instance.ContainerInstance"
    ]
    """<p>The container instance that was registered.</p>"""
