"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GatewayIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rtbfabric.types.gateway_id

GatewayIdList: TypeAlias = list["capo_rtbfabric.types.gateway_id.GatewayId"]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> GatewayIdList:
    return list(data)
