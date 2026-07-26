"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowHealthEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_health_entity

MetaFlowHealthEntityList: TypeAlias = list[
    "capo_socialmessaging.types.meta_flow_health_entity.MetaFlowHealthEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowHealthEntityList) -> list:
    import capo_socialmessaging.types.meta_flow_health_entity

    out: list = []
    for item in value:
        out.append(
            capo_socialmessaging.types.meta_flow_health_entity.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MetaFlowHealthEntityList:
    import capo_socialmessaging.types.meta_flow_health_entity

    out: MetaFlowHealthEntityList = []
    for item in data:
        out.append(
            capo_socialmessaging.types.meta_flow_health_entity.deserialize_json(item)
        )
    return out
