"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AgentTracesConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.cloud_watch_logs_trace_config
    import aws_sdk_bedrock_agentcore.types.spans


class _AgentTracesConfig_sessionSpans(TypedDict, closed=True):
    sessionSpans: "aws_sdk_bedrock_agentcore.types.spans.Spans"


class _AgentTracesConfig_cloudwatchLogs(TypedDict, closed=True):
    cloudwatchLogs: "aws_sdk_bedrock_agentcore.types.cloud_watch_logs_trace_config.CloudWatchLogsTraceConfig"


AgentTracesConfig: TypeAlias = (
    _AgentTracesConfig_sessionSpans | _AgentTracesConfig_cloudwatchLogs
)


# --- restJson1 ser/de ---
def serialize_json(value: AgentTracesConfig) -> dict:
    if "sessionSpans" in value:
        import aws_sdk_bedrock_agentcore.types.spans

        return {
            "sessionSpans": aws_sdk_bedrock_agentcore.types.spans.serialize_json(
                value["sessionSpans"]
            )
        }
    elif "cloudwatchLogs" in value:
        import aws_sdk_bedrock_agentcore.types.cloud_watch_logs_trace_config

        return {
            "cloudwatchLogs": aws_sdk_bedrock_agentcore.types.cloud_watch_logs_trace_config.serialize_json(
                value["cloudwatchLogs"]
            )
        }
    else:
        raise SerializationError("AgentTracesConfig: no variant present")


def deserialize_json(data: dict) -> AgentTracesConfig:
    if "sessionSpans" in data:
        import aws_sdk_bedrock_agentcore.types.spans

        return {
            "sessionSpans": aws_sdk_bedrock_agentcore.types.spans.deserialize_json(
                data["sessionSpans"]
            )
        }
    elif "cloudwatchLogs" in data:
        import aws_sdk_bedrock_agentcore.types.cloud_watch_logs_trace_config

        return {
            "cloudwatchLogs": aws_sdk_bedrock_agentcore.types.cloud_watch_logs_trace_config.deserialize_json(
                data["cloudwatchLogs"]
            )
        }
    else:
        raise DeserializationError("AgentTracesConfig: no recognized variant key")
