"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MergeRouterInputProtocolConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.merge_router_input_protocol_configuration

MergeRouterInputProtocolConfigurationList: TypeAlias = list[
    "capo_mediaconnect.types.merge_router_input_protocol_configuration.MergeRouterInputProtocolConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: MergeRouterInputProtocolConfigurationList) -> list:
    import capo_mediaconnect.types.merge_router_input_protocol_configuration

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.merge_router_input_protocol_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MergeRouterInputProtocolConfigurationList:
    import capo_mediaconnect.types.merge_router_input_protocol_configuration

    out: MergeRouterInputProtocolConfigurationList = []
    for item in data:
        out.append(
            capo_mediaconnect.types.merge_router_input_protocol_configuration.deserialize_json(
                item
            )
        )
    return out
