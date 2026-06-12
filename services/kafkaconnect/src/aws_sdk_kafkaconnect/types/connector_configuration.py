"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ConnectorConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string

ConnectorConfiguration: TypeAlias = dict[
    "aws_sdk_kafkaconnect.types.__string.__string",
    "aws_sdk_kafkaconnect.types.__string.__string",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConnectorConfiguration) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ConnectorConfiguration:
    out: ConnectorConfiguration = {}
    for key, value in data.items():
        out[key] = value
    return out
