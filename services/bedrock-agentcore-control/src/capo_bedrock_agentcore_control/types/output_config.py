"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.cloud_watch_output_config


class OutputConfig(TypedDict, closed=True):
    cloud_watch_config: "capo_bedrock_agentcore_control.types.cloud_watch_output_config.CloudWatchOutputConfig"
    """<p> The CloudWatch configuration for writing evaluation results to CloudWatch logs with embedded metric format. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputConfig) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.cloud_watch_output_config

    out["cloudWatchConfig"] = (
        capo_bedrock_agentcore_control.types.cloud_watch_output_config.serialize_json(
            value["cloud_watch_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> OutputConfig:
    out: OutputConfig = {}  # type: ignore[typeddict-item]
    if "cloudWatchConfig" in data:
        import capo_bedrock_agentcore_control.types.cloud_watch_output_config

        out["cloud_watch_config"] = (
            capo_bedrock_agentcore_control.types.cloud_watch_output_config.deserialize_json(
                data["cloudWatchConfig"]
            )
        )
    else:
        raise DeserializationError("OutputConfig.cloud_watch_config required")
    return out
