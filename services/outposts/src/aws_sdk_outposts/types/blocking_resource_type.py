"""Generated from Smithy shape ``com.amazonaws.outposts#BlockingResourceType``."""

from typing import Literal, TypeAlias, cast

BlockingResourceType: TypeAlias = Literal[
    "EC2_INSTANCE",
    "OUTPOST_RAM_SHARE",
    "LGW_ROUTING_DOMAIN",
    "LGW_ROUTE_TABLE",
    "LGW_VIRTUAL_INTERFACE_GROUP",
    "OUTPOST_ORDER_CANCELLABLE",
    "OUTPOST_ORDER_INTERVENTION_REQUIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: BlockingResourceType) -> str:
    return value


def deserialize_json(data: str) -> BlockingResourceType:
    return cast(BlockingResourceType, data)
