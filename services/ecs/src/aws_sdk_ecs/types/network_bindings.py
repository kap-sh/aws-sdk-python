"""Generated from Smithy shape ``com.amazonaws.ecs#NetworkBindings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.network_binding

NetworkBindings: TypeAlias = list["aws_sdk_ecs.types.network_binding.NetworkBinding"]
