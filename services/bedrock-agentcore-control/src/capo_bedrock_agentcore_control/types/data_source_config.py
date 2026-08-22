"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DataSourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.cloud_watch_logs_input_config


class _DataSourceConfig_cloudWatchLogs(TypedDict, closed=True):
    cloudWatchLogs: "capo_bedrock_agentcore_control.types.cloud_watch_logs_input_config.CloudWatchLogsInputConfig"


DataSourceConfig: TypeAlias = _DataSourceConfig_cloudWatchLogs


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceConfig) -> dict:
    if "cloudWatchLogs" in value:
        import capo_bedrock_agentcore_control.types.cloud_watch_logs_input_config

        return {
            "cloudWatchLogs": capo_bedrock_agentcore_control.types.cloud_watch_logs_input_config.serialize_json(
                value["cloudWatchLogs"]
            )
        }
    else:
        raise SerializationError("DataSourceConfig: no variant present")


def deserialize_json(data: dict) -> DataSourceConfig:
    if data.get("cloudWatchLogs") is not None:
        import capo_bedrock_agentcore_control.types.cloud_watch_logs_input_config

        return {
            "cloudWatchLogs": capo_bedrock_agentcore_control.types.cloud_watch_logs_input_config.deserialize_json(
                data["cloudWatchLogs"]
            )
        }
    else:
        raise DeserializationError("DataSourceConfig: no recognized variant key")
