"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CloudWatchOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.log_group_name


class CloudWatchOutputConfig(TypedDict, closed=True):
    log_group_name: "capo_bedrock_agentcore_control.types.log_group_name.LogGroupName"
    """<p> The name of the CloudWatch log group where evaluation results will be written. The log group will be created if it doesn't exist. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchOutputConfig) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    return out


def deserialize_json(data: dict) -> CloudWatchOutputConfig:
    out: CloudWatchOutputConfig = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("CloudWatchOutputConfig.log_group_name required")
    return out
