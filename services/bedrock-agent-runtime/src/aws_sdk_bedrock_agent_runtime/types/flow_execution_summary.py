"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_identifier
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_status
    import aws_sdk_bedrock_agent_runtime.types.flow_identifier
    import aws_sdk_bedrock_agent_runtime.types.version


class FlowExecutionSummary(TypedDict, closed=True):
    execution_arn: "aws_sdk_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the flow execution.</p>"""
    flow_alias_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier"
    )
    """<p>The unique identifier of the flow alias used for the execution.</p>"""
    flow_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier"
    )
    """<p>The unique identifier of the flow.</p>"""
    flow_version: "aws_sdk_bedrock_agent_runtime.types.version.Version"
    """<p>The version of the flow used for the execution.</p>"""
    status: (
        "aws_sdk_bedrock_agent_runtime.types.flow_execution_status.FlowExecutionStatus"
    )
    """<p>The current status of the flow execution.</p> <p>Flow executions time out after 24 hours.</p>"""
    created_at: "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the flow execution was created.</p>"""
    ended_at: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    ]
    """<p>The timestamp when the flow execution ended. This field is only populated when the execution has completed, failed, timed out, or been aborted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionSummary) -> dict:
    out: dict = {}
    out["executionArn"] = value["execution_arn"]
    out["flowAliasIdentifier"] = value["flow_alias_identifier"]
    out["flowIdentifier"] = value["flow_identifier"]
    out["flowVersion"] = value["flow_version"]
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_status

    out["status"] = (
        aws_sdk_bedrock_agent_runtime.types.flow_execution_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    if "ended_at" in value:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["endedAt"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(
                value["ended_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> FlowExecutionSummary:
    out: FlowExecutionSummary = {}  # type: ignore[typeddict-item]
    if "executionArn" in data:
        out["execution_arn"] = data["executionArn"]
    else:
        raise DeserializationError("FlowExecutionSummary.execution_arn required")
    if "flowAliasIdentifier" in data:
        out["flow_alias_identifier"] = data["flowAliasIdentifier"]
    else:
        raise DeserializationError(
            "FlowExecutionSummary.flow_alias_identifier required"
        )
    if "flowIdentifier" in data:
        out["flow_identifier"] = data["flowIdentifier"]
    else:
        raise DeserializationError("FlowExecutionSummary.flow_identifier required")
    if "flowVersion" in data:
        out["flow_version"] = data["flowVersion"]
    else:
        raise DeserializationError("FlowExecutionSummary.flow_version required")
    if "status" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_execution_status

        out["status"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_execution_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("FlowExecutionSummary.status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("FlowExecutionSummary.created_at required")
    if "endedAt" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["ended_at"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["endedAt"]
            )
        )
    return out
