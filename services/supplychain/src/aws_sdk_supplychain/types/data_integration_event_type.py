"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_supplychain.errors import DeserializationError

DataIntegrationEventType: TypeAlias = Literal[
    "scn.data.forecast",
    "scn.data.inventorylevel",
    "scn.data.inboundorder",
    "scn.data.inboundorderline",
    "scn.data.inboundorderlineschedule",
    "scn.data.outboundorderline",
    "scn.data.outboundshipment",
    "scn.data.processheader",
    "scn.data.processoperation",
    "scn.data.processproduct",
    "scn.data.reservation",
    "scn.data.shipment",
    "scn.data.shipmentstop",
    "scn.data.shipmentstoporder",
    "scn.data.supplyplan",
    "scn.data.dataset",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "scn.data.forecast",
        "scn.data.inventorylevel",
        "scn.data.inboundorder",
        "scn.data.inboundorderline",
        "scn.data.inboundorderlineschedule",
        "scn.data.outboundorderline",
        "scn.data.outboundshipment",
        "scn.data.processheader",
        "scn.data.processoperation",
        "scn.data.processproduct",
        "scn.data.reservation",
        "scn.data.shipment",
        "scn.data.shipmentstop",
        "scn.data.shipmentstoporder",
        "scn.data.supplyplan",
        "scn.data.dataset",
    )
)


def serialize_json(value: DataIntegrationEventType) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationEventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataIntegrationEventType value: {data!r}")
    return cast(DataIntegrationEventType, data)
