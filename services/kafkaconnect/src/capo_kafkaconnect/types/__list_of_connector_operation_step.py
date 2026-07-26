"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#__listOfConnectorOperationStep``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafkaconnect.types.connector_operation_step

__listOfConnectorOperationStep: TypeAlias = list[
    "capo_kafkaconnect.types.connector_operation_step.ConnectorOperationStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfConnectorOperationStep) -> list:
    import capo_kafkaconnect.types.connector_operation_step

    out: list = []
    for item in value:
        out.append(
            capo_kafkaconnect.types.connector_operation_step.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfConnectorOperationStep:
    import capo_kafkaconnect.types.connector_operation_step

    out: __listOfConnectorOperationStep = []
    for item in data:
        out.append(
            capo_kafkaconnect.types.connector_operation_step.deserialize_json(item)
        )
    return out
