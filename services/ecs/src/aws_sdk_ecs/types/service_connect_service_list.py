"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_connect_service

ServiceConnectServiceList: TypeAlias = list[
    "aws_sdk_ecs.types.service_connect_service.ServiceConnectService"
]
