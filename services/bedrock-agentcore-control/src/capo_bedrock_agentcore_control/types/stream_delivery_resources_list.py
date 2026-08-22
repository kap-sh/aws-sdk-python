"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StreamDeliveryResourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.stream_delivery_resource

StreamDeliveryResourcesList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.stream_delivery_resource.StreamDeliveryResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamDeliveryResourcesList) -> list:
    import capo_bedrock_agentcore_control.types.stream_delivery_resource

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.stream_delivery_resource.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StreamDeliveryResourcesList:
    import capo_bedrock_agentcore_control.types.stream_delivery_resource

    out: StreamDeliveryResourcesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.stream_delivery_resource.deserialize_json(
                item
            )
        )
    return out
