"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_supplychain.types.data_integration_flow_execution_output_metadata
    import aws_sdk_supplychain.types.data_integration_flow_execution_source_info
    import aws_sdk_supplychain.types.data_integration_flow_execution_status
    import aws_sdk_supplychain.types.data_integration_flow_name
    import aws_sdk_supplychain.types.uuid


class DataIntegrationFlowExecution(TypedDict, closed=True):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The flow execution's instanceId.</p>"""
    flow_name: (
        "aws_sdk_supplychain.types.data_integration_flow_name.DataIntegrationFlowName"
    )
    """<p>The flow execution's flowName.</p>"""
    execution_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The flow executionId.</p>"""
    status: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_execution_status.DataIntegrationFlowExecutionStatus"
    ]
    """<p>The status of flow execution.</p>"""
    source_info: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_execution_source_info.DataIntegrationFlowExecutionSourceInfo"
    ]
    """<p>The source information for a flow execution.</p>"""
    message: NotRequired["str"]
    """<p>The failure message (if any) of failed flow execution.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The flow execution start timestamp.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The flow execution end timestamp.</p>"""
    output_metadata: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_execution_output_metadata.DataIntegrationFlowExecutionOutputMetadata"
    ]
    """<p>The flow execution output metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowExecution) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["flowName"] = value["flow_name"]
    out["executionId"] = value["execution_id"]
    if "status" in value:
        import aws_sdk_supplychain.types.data_integration_flow_execution_status

        out["status"] = (
            aws_sdk_supplychain.types.data_integration_flow_execution_status.serialize_json(
                value["status"]
            )
        )
    if "source_info" in value:
        import aws_sdk_supplychain.types.data_integration_flow_execution_source_info

        out["sourceInfo"] = (
            aws_sdk_supplychain.types.data_integration_flow_execution_source_info.serialize_json(
                value["source_info"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    if "start_time" in value:
        import aws_sdk_supplychain.types._prelude.timestamp

        out["startTime"] = aws_sdk_supplychain.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_supplychain.types._prelude.timestamp

        out["endTime"] = aws_sdk_supplychain.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    if "output_metadata" in value:
        import aws_sdk_supplychain.types.data_integration_flow_execution_output_metadata

        out["outputMetadata"] = (
            aws_sdk_supplychain.types.data_integration_flow_execution_output_metadata.serialize_json(
                value["output_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowExecution:
    out: DataIntegrationFlowExecution = {}  # type: ignore[typeddict-item]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    else:
        raise DeserializationError("DataIntegrationFlowExecution.instance_id required")
    if "flowName" in data:
        out["flow_name"] = data["flowName"]
    else:
        raise DeserializationError("DataIntegrationFlowExecution.flow_name required")
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("DataIntegrationFlowExecution.execution_id required")
    if "status" in data:
        import aws_sdk_supplychain.types.data_integration_flow_execution_status

        out["status"] = (
            aws_sdk_supplychain.types.data_integration_flow_execution_status.deserialize_json(
                data["status"]
            )
        )
    if "sourceInfo" in data:
        import aws_sdk_supplychain.types.data_integration_flow_execution_source_info

        out["source_info"] = (
            aws_sdk_supplychain.types.data_integration_flow_execution_source_info.deserialize_json(
                data["sourceInfo"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    if "startTime" in data:
        import aws_sdk_supplychain.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_supplychain.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_supplychain.types._prelude.timestamp

        out["end_time"] = aws_sdk_supplychain.types._prelude.timestamp.deserialize_json(
            data["endTime"]
        )
    if "outputMetadata" in data:
        import aws_sdk_supplychain.types.data_integration_flow_execution_output_metadata

        out["output_metadata"] = (
            aws_sdk_supplychain.types.data_integration_flow_execution_output_metadata.deserialize_json(
                data["outputMetadata"]
            )
        )
    return out
