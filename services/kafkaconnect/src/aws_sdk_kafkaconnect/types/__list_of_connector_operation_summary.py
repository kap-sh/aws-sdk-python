"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#__listOfConnectorOperationSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.connector_operation_summary

__listOfConnectorOperationSummary: TypeAlias = list[
    "aws_sdk_kafkaconnect.types.connector_operation_summary.ConnectorOperationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfConnectorOperationSummary) -> list:
    import aws_sdk_kafkaconnect.types.connector_operation_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kafkaconnect.types.connector_operation_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfConnectorOperationSummary:
    import aws_sdk_kafkaconnect.types.connector_operation_summary

    out: __listOfConnectorOperationSummary = []
    for item in data:
        out.append(
            aws_sdk_kafkaconnect.types.connector_operation_summary.deserialize_json(
                item
            )
        )
    return out
