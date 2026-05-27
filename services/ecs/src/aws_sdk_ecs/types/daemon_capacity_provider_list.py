"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonCapacityProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_capacity_provider

DaemonCapacityProviderList: TypeAlias = list[
    "aws_sdk_ecs.types.daemon_capacity_provider.DaemonCapacityProvider"
]
