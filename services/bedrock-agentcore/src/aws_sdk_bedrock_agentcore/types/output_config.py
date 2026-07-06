"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#OutputConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.cloud_watch_output_config


class _OutputConfig_cloudWatchConfig(TypedDict, closed=True):
    cloudWatchConfig: "aws_sdk_bedrock_agentcore.types.cloud_watch_output_config.CloudWatchOutputConfig"


OutputConfig: TypeAlias = _OutputConfig_cloudWatchConfig


# --- restJson1 ser/de ---
def serialize_json(value: OutputConfig) -> dict:
    if "cloudWatchConfig" in value:
        import aws_sdk_bedrock_agentcore.types.cloud_watch_output_config

        return {
            "cloudWatchConfig": aws_sdk_bedrock_agentcore.types.cloud_watch_output_config.serialize_json(
                value["cloudWatchConfig"]
            )
        }
    else:
        raise SerializationError("OutputConfig: no variant present")


def deserialize_json(data: dict) -> OutputConfig:
    if "cloudWatchConfig" in data:
        import aws_sdk_bedrock_agentcore.types.cloud_watch_output_config

        return {
            "cloudWatchConfig": aws_sdk_bedrock_agentcore.types.cloud_watch_output_config.deserialize_json(
                data["cloudWatchConfig"]
            )
        }
    else:
        raise DeserializationError("OutputConfig: no recognized variant key")
