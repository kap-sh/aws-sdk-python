"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.matter_event_id
    import aws_sdk_iot_managed_integrations.types.matter_fields

MatterEvents: TypeAlias = dict[
    "aws_sdk_iot_managed_integrations.types.matter_event_id.MatterEventId",
    "aws_sdk_iot_managed_integrations.types.matter_fields.MatterFields",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MatterEvents) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> MatterEvents:
    out: MatterEvents = {}
    for key, value in data.items():
        out[key] = value
    return out
