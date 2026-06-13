"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MergeRouterInputProtocolConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.merge_router_input_protocol_configuration

MergeRouterInputProtocolConfigurationList: TypeAlias = list[
    "aws_sdk_mediaconnect.types.merge_router_input_protocol_configuration.MergeRouterInputProtocolConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: MergeRouterInputProtocolConfigurationList) -> list:
    import aws_sdk_mediaconnect.types.merge_router_input_protocol_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.merge_router_input_protocol_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MergeRouterInputProtocolConfigurationList:
    import aws_sdk_mediaconnect.types.merge_router_input_protocol_configuration

    out: MergeRouterInputProtocolConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.merge_router_input_protocol_configuration.deserialize_json(
                item
            )
        )
    return out
