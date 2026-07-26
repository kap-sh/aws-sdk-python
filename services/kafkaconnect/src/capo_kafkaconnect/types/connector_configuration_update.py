"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ConnectorConfigurationUpdate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string

ConnectorConfigurationUpdate: TypeAlias = dict[
    "capo_kafkaconnect.types.__string.__string",
    "capo_kafkaconnect.types.__string.__string",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConnectorConfigurationUpdate) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ConnectorConfigurationUpdate:
    out: ConnectorConfigurationUpdate = {}
    for key, value in data.items():
        out[key] = value
    return out
