"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#VariableDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.variable_definition

VariableDefinitions: TypeAlias = list[
    "aws_sdk_iot_events_data.types.variable_definition.VariableDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: VariableDefinitions) -> list:
    import aws_sdk_iot_events_data.types.variable_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_events_data.types.variable_definition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> VariableDefinitions:
    import aws_sdk_iot_events_data.types.variable_definition

    out: VariableDefinitions = []
    for item in data:
        out.append(
            aws_sdk_iot_events_data.types.variable_definition.deserialize_json(item)
        )
    return out
