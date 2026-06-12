"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#__listOfConnectorOperationStep``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.connector_operation_step

__listOfConnectorOperationStep: TypeAlias = list[
    "aws_sdk_kafkaconnect.types.connector_operation_step.ConnectorOperationStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfConnectorOperationStep) -> list:
    import aws_sdk_kafkaconnect.types.connector_operation_step

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kafkaconnect.types.connector_operation_step.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfConnectorOperationStep:
    import aws_sdk_kafkaconnect.types.connector_operation_step

    out: __listOfConnectorOperationStep = []
    for item in data:
        out.append(
            aws_sdk_kafkaconnect.types.connector_operation_step.deserialize_json(item)
        )
    return out
