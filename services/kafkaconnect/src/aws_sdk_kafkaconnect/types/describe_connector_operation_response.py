"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DescribeConnectorOperationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__list_of_connector_operation_step
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.__timestamp_iso8601
    import aws_sdk_kafkaconnect.types.connector_configuration
    import aws_sdk_kafkaconnect.types.connector_operation_state
    import aws_sdk_kafkaconnect.types.connector_operation_type
    import aws_sdk_kafkaconnect.types.state_description
    import aws_sdk_kafkaconnect.types.worker_setting


class DescribeConnectorOperationResponse(TypedDict):
    connector_arn: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    connector_operation_arn: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the connector operation.</p>"""
    connector_operation_state: NotRequired[
        "aws_sdk_kafkaconnect.types.connector_operation_state.ConnectorOperationState"
    ]
    """<p>The state of the connector operation.</p>"""
    connector_operation_type: NotRequired[
        "aws_sdk_kafkaconnect.types.connector_operation_type.ConnectorOperationType"
    ]
    """<p>The type of connector operation performed.</p>"""
    operation_steps: NotRequired[
        "aws_sdk_kafkaconnect.types.__list_of_connector_operation_step.__listOfConnectorOperationStep"
    ]
    """<p>The array of operation steps taken.</p>"""
    origin_worker_setting: NotRequired[
        "aws_sdk_kafkaconnect.types.worker_setting.WorkerSetting"
    ]
    """<p>The origin worker setting.</p>"""
    origin_connector_configuration: NotRequired[
        "aws_sdk_kafkaconnect.types.connector_configuration.ConnectorConfiguration"
    ]
    """<p>The origin connector configuration.</p>"""
    target_worker_setting: NotRequired[
        "aws_sdk_kafkaconnect.types.worker_setting.WorkerSetting"
    ]
    """<p>The target worker setting.</p>"""
    target_connector_configuration: NotRequired[
        "aws_sdk_kafkaconnect.types.connector_configuration.ConnectorConfiguration"
    ]
    """<p>The target connector configuration.</p>"""
    error_info: NotRequired[
        "aws_sdk_kafkaconnect.types.state_description.StateDescription"
    ]
    creation_time: NotRequired[
        "aws_sdk_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when the operation was created.</p>"""
    end_time: NotRequired[
        "aws_sdk_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when the operation ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConnectorOperationResponse) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["connectorArn"] = value["connector_arn"]
    if "connector_operation_arn" in value:
        out["connectorOperationArn"] = value["connector_operation_arn"]
    if "connector_operation_state" in value:
        out["connectorOperationState"] = value["connector_operation_state"]
    if "connector_operation_type" in value:
        out["connectorOperationType"] = value["connector_operation_type"]
    if "operation_steps" in value:
        import aws_sdk_kafkaconnect.types.__list_of_connector_operation_step

        out["operationSteps"] = (
            aws_sdk_kafkaconnect.types.__list_of_connector_operation_step.serialize_json(
                value["operation_steps"]
            )
        )
    if "origin_worker_setting" in value:
        import aws_sdk_kafkaconnect.types.worker_setting

        out["originWorkerSetting"] = (
            aws_sdk_kafkaconnect.types.worker_setting.serialize_json(
                value["origin_worker_setting"]
            )
        )
    if "origin_connector_configuration" in value:
        import aws_sdk_kafkaconnect.types.connector_configuration

        out["originConnectorConfiguration"] = (
            aws_sdk_kafkaconnect.types.connector_configuration.serialize_json(
                value["origin_connector_configuration"]
            )
        )
    if "target_worker_setting" in value:
        import aws_sdk_kafkaconnect.types.worker_setting

        out["targetWorkerSetting"] = (
            aws_sdk_kafkaconnect.types.worker_setting.serialize_json(
                value["target_worker_setting"]
            )
        )
    if "target_connector_configuration" in value:
        import aws_sdk_kafkaconnect.types.connector_configuration

        out["targetConnectorConfiguration"] = (
            aws_sdk_kafkaconnect.types.connector_configuration.serialize_json(
                value["target_connector_configuration"]
            )
        )
    if "error_info" in value:
        import aws_sdk_kafkaconnect.types.state_description

        out["errorInfo"] = aws_sdk_kafkaconnect.types.state_description.serialize_json(
            value["error_info"]
        )
    if "creation_time" in value:
        import aws_sdk_kafkaconnect.types.__timestamp_iso8601

        out["creationTime"] = (
            aws_sdk_kafkaconnect.types.__timestamp_iso8601.serialize_json(
                value["creation_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_kafkaconnect.types.__timestamp_iso8601

        out["endTime"] = aws_sdk_kafkaconnect.types.__timestamp_iso8601.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> DescribeConnectorOperationResponse:
    out: DescribeConnectorOperationResponse = {}  # type: ignore[typeddict-item]
    if "connectorArn" in data:
        out["connector_arn"] = data["connectorArn"]
    if "connectorOperationArn" in data:
        out["connector_operation_arn"] = data["connectorOperationArn"]
    if "connectorOperationState" in data:
        out["connector_operation_state"] = data["connectorOperationState"]
    if "connectorOperationType" in data:
        out["connector_operation_type"] = data["connectorOperationType"]
    if "operationSteps" in data:
        import aws_sdk_kafkaconnect.types.__list_of_connector_operation_step

        out["operation_steps"] = (
            aws_sdk_kafkaconnect.types.__list_of_connector_operation_step.deserialize_json(
                data["operationSteps"]
            )
        )
    if "originWorkerSetting" in data:
        import aws_sdk_kafkaconnect.types.worker_setting

        out["origin_worker_setting"] = (
            aws_sdk_kafkaconnect.types.worker_setting.deserialize_json(
                data["originWorkerSetting"]
            )
        )
    if "originConnectorConfiguration" in data:
        import aws_sdk_kafkaconnect.types.connector_configuration

        out["origin_connector_configuration"] = (
            aws_sdk_kafkaconnect.types.connector_configuration.deserialize_json(
                data["originConnectorConfiguration"]
            )
        )
    if "targetWorkerSetting" in data:
        import aws_sdk_kafkaconnect.types.worker_setting

        out["target_worker_setting"] = (
            aws_sdk_kafkaconnect.types.worker_setting.deserialize_json(
                data["targetWorkerSetting"]
            )
        )
    if "targetConnectorConfiguration" in data:
        import aws_sdk_kafkaconnect.types.connector_configuration

        out["target_connector_configuration"] = (
            aws_sdk_kafkaconnect.types.connector_configuration.deserialize_json(
                data["targetConnectorConfiguration"]
            )
        )
    if "errorInfo" in data:
        import aws_sdk_kafkaconnect.types.state_description

        out["error_info"] = (
            aws_sdk_kafkaconnect.types.state_description.deserialize_json(
                data["errorInfo"]
            )
        )
    if "creationTime" in data:
        import aws_sdk_kafkaconnect.types.__timestamp_iso8601

        out["creation_time"] = (
            aws_sdk_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
                data["creationTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_kafkaconnect.types.__timestamp_iso8601

        out["end_time"] = (
            aws_sdk_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
                data["endTime"]
            )
        )
    return out
