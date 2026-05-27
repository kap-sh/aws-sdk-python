"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectServiceResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_connect_service_resource

ServiceConnectServiceResourceList: TypeAlias = list[
    "aws_sdk_ecs.types.service_connect_service_resource.ServiceConnectServiceResource"
]
