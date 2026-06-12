"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowVersionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.date_timestamp
    import aws_sdk_bedrock_agent.types.flow_arn
    import aws_sdk_bedrock_agent.types.flow_id
    import aws_sdk_bedrock_agent.types.flow_status
    import aws_sdk_bedrock_agent.types.numerical_version


class FlowVersionSummary(TypedDict):
    id: "aws_sdk_bedrock_agent.types.flow_id.FlowId"
    """<p>The unique identifier of the flow.</p>"""
    arn: "aws_sdk_bedrock_agent.types.flow_arn.FlowArn"
    """<p>The Amazon Resource Name (ARN) of the flow that the version belongs to.</p>"""
    status: "aws_sdk_bedrock_agent.types.flow_status.FlowStatus"
    """<p>The status of the flow.</p>"""
    created_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at the version was created.</p>"""
    version: "aws_sdk_bedrock_agent.types.numerical_version.NumericalVersion"
    """<p>The version of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowVersionSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import aws_sdk_bedrock_agent.types.flow_status

    out["status"] = aws_sdk_bedrock_agent.types.flow_status.serialize_json(
        value["status"]
    )
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> FlowVersionSummary:
    out: FlowVersionSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FlowVersionSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("FlowVersionSummary.arn required")
    if "status" in data:
        import aws_sdk_bedrock_agent.types.flow_status

        out["status"] = aws_sdk_bedrock_agent.types.flow_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("FlowVersionSummary.status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["created_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("FlowVersionSummary.created_at required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("FlowVersionSummary.version required")
    return out
