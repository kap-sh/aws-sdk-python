"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#__listOfConnectorSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.connector_summary

__listOfConnectorSummary: TypeAlias = list[
    "aws_sdk_kafkaconnect.types.connector_summary.ConnectorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfConnectorSummary) -> list:
    import aws_sdk_kafkaconnect.types.connector_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_kafkaconnect.types.connector_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfConnectorSummary:
    import aws_sdk_kafkaconnect.types.connector_summary

    out: __listOfConnectorSummary = []
    for item in data:
        out.append(aws_sdk_kafkaconnect.types.connector_summary.deserialize_json(item))
    return out
