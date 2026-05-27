"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedIngressPaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_ingress_path

ManagedIngressPaths: TypeAlias = list[
    "aws_sdk_ecs.types.managed_ingress_path.ManagedIngressPath"
]
