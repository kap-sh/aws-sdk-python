"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FailoverRouterInputProtocolConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.failover_router_input_protocol_configuration

FailoverRouterInputProtocolConfigurationList: TypeAlias = list[
    "aws_sdk_mediaconnect.types.failover_router_input_protocol_configuration.FailoverRouterInputProtocolConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailoverRouterInputProtocolConfigurationList) -> list:
    import aws_sdk_mediaconnect.types.failover_router_input_protocol_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.failover_router_input_protocol_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FailoverRouterInputProtocolConfigurationList:
    import aws_sdk_mediaconnect.types.failover_router_input_protocol_configuration

    out: FailoverRouterInputProtocolConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.failover_router_input_protocol_configuration.deserialize_json(
                item
            )
        )
    return out
