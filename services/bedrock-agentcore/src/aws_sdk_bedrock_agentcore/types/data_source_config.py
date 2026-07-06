"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DataSourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.cloud_watch_logs_source


class _DataSourceConfig_cloudWatchLogs(TypedDict, closed=True):
    cloudWatchLogs: (
        "aws_sdk_bedrock_agentcore.types.cloud_watch_logs_source.CloudWatchLogsSource"
    )


DataSourceConfig: TypeAlias = _DataSourceConfig_cloudWatchLogs


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceConfig) -> dict:
    if "cloudWatchLogs" in value:
        import aws_sdk_bedrock_agentcore.types.cloud_watch_logs_source

        return {
            "cloudWatchLogs": aws_sdk_bedrock_agentcore.types.cloud_watch_logs_source.serialize_json(
                value["cloudWatchLogs"]
            )
        }
    else:
        raise SerializationError("DataSourceConfig: no variant present")


def deserialize_json(data: dict) -> DataSourceConfig:
    if "cloudWatchLogs" in data:
        import aws_sdk_bedrock_agentcore.types.cloud_watch_logs_source

        return {
            "cloudWatchLogs": aws_sdk_bedrock_agentcore.types.cloud_watch_logs_source.deserialize_json(
                data["cloudWatchLogs"]
            )
        }
    else:
        raise DeserializationError("DataSourceConfig: no recognized variant key")
