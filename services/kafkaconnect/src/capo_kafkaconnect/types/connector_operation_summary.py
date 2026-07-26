"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ConnectorOperationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.__timestamp_iso8601
    import capo_kafkaconnect.types.connector_operation_state
    import capo_kafkaconnect.types.connector_operation_type


class ConnectorOperationSummary(TypedDict, closed=True):
    connector_operation_arn: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the connector operation.</p>"""
    connector_operation_type: NotRequired[
        "capo_kafkaconnect.types.connector_operation_type.ConnectorOperationType"
    ]
    """<p>The type of connector operation performed.</p>"""
    connector_operation_state: NotRequired[
        "capo_kafkaconnect.types.connector_operation_state.ConnectorOperationState"
    ]
    """<p>The state of the connector operation.</p>"""
    creation_time: NotRequired[
        "capo_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when operation was created.</p>"""
    end_time: NotRequired[
        "capo_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when operation ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorOperationSummary) -> dict:
    out: dict = {}
    if "connector_operation_arn" in value:
        out["connectorOperationArn"] = value["connector_operation_arn"]
    if "connector_operation_type" in value:
        out["connectorOperationType"] = value["connector_operation_type"]
    if "connector_operation_state" in value:
        out["connectorOperationState"] = value["connector_operation_state"]
    if "creation_time" in value:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["creationTime"] = (
            capo_kafkaconnect.types.__timestamp_iso8601.serialize_json(
                value["creation_time"]
            )
        )
    if "end_time" in value:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["endTime"] = capo_kafkaconnect.types.__timestamp_iso8601.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> ConnectorOperationSummary:
    out: ConnectorOperationSummary = {}  # type: ignore[typeddict-item]
    if "connectorOperationArn" in data:
        out["connector_operation_arn"] = data["connectorOperationArn"]
    if "connectorOperationType" in data:
        out["connector_operation_type"] = data["connectorOperationType"]
    if "connectorOperationState" in data:
        out["connector_operation_state"] = data["connectorOperationState"]
    if "creationTime" in data:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["creation_time"] = (
            capo_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
                data["creationTime"]
            )
        )
    if "endTime" in data:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["end_time"] = capo_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
            data["endTime"]
        )
    return out
