"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Metadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.usage


class Metadata(TypedDict, closed=True):
    start_time: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    ]
    """<p>In the final response, <code>startTime</code> is the start time of the agent invocation operation.</p>"""
    end_time: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    ]
    """<p>In the final response, <code>endTime</code> is the end time of the agent invocation operation.</p>"""
    total_time_ms: NotRequired["int"]
    """<p> The total execution time for the specific invocation being processed (model, knowledge base, guardrail, agent collaborator, or code interpreter). It represents how long the individual invocation took.</p>"""
    operation_total_time_ms: NotRequired["int"]
    """<p>The total time it took for the agent to complete execution. This field is only set for the final response.</p>"""
    client_request_id: NotRequired["str"]
    """<p>A unique identifier associated with the downstream invocation. This ID can be used for tracing, debugging, and identifying specific invocations in customer logs or systems.</p>"""
    usage: NotRequired["aws_sdk_bedrock_agent_runtime.types.usage.Usage"]
    """<p>Specific to model invocation and contains details about the usage of a foundation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Metadata) -> dict:
    out: dict = {}
    if "start_time" in value:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["startTime"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["endTime"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(
                value["end_time"]
            )
        )
    if "total_time_ms" in value:
        out["totalTimeMs"] = value["total_time_ms"]
    if "operation_total_time_ms" in value:
        out["operationTotalTimeMs"] = value["operation_total_time_ms"]
    if "client_request_id" in value:
        out["clientRequestId"] = value["client_request_id"]
    if "usage" in value:
        import aws_sdk_bedrock_agent_runtime.types.usage

        out["usage"] = aws_sdk_bedrock_agent_runtime.types.usage.serialize_json(
            value["usage"]
        )
    return out


def deserialize_json(data: dict) -> Metadata:
    out: Metadata = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["start_time"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["end_time"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["endTime"]
            )
        )
    if "totalTimeMs" in data:
        out["total_time_ms"] = data["totalTimeMs"]
    if "operationTotalTimeMs" in data:
        out["operation_total_time_ms"] = data["operationTotalTimeMs"]
    if "clientRequestId" in data:
        out["client_request_id"] = data["clientRequestId"]
    if "usage" in data:
        import aws_sdk_bedrock_agent_runtime.types.usage

        out["usage"] = aws_sdk_bedrock_agent_runtime.types.usage.deserialize_json(
            data["usage"]
        )
    return out
