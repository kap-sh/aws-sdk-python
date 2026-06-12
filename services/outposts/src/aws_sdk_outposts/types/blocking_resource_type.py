"""Generated from Smithy shape ``com.amazonaws.outposts#BlockingResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "EC2_INSTANCE",
        "OUTPOST_RAM_SHARE",
        "LGW_ROUTING_DOMAIN",
        "LGW_ROUTE_TABLE",
        "LGW_VIRTUAL_INTERFACE_GROUP",
        "OUTPOST_ORDER_CANCELLABLE",
        "OUTPOST_ORDER_INTERVENTION_REQUIRED",
    )
)


def serialize_json(value: BlockingResourceType) -> str:
    return value


def deserialize_json(data: str) -> BlockingResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlockingResourceType value: {data!r}")
    return cast(BlockingResourceType, data)
