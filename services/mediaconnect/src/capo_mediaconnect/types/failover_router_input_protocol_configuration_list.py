"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FailoverRouterInputProtocolConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.failover_router_input_protocol_configuration

FailoverRouterInputProtocolConfigurationList: TypeAlias = list[
    "capo_mediaconnect.types.failover_router_input_protocol_configuration.FailoverRouterInputProtocolConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailoverRouterInputProtocolConfigurationList) -> list:
    import capo_mediaconnect.types.failover_router_input_protocol_configuration

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.failover_router_input_protocol_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FailoverRouterInputProtocolConfigurationList:
    import capo_mediaconnect.types.failover_router_input_protocol_configuration

    out: FailoverRouterInputProtocolConfigurationList = []
    for item in data:
        out.append(
            capo_mediaconnect.types.failover_router_input_protocol_configuration.deserialize_json(
                item
            )
        )
    return out
