"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectClientAliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_connect_client_alias

ServiceConnectClientAliasList: TypeAlias = list[
    "aws_sdk_ecs.types.service_connect_client_alias.ServiceConnectClientAlias"
]
