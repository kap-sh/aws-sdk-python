"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CloudWatchOutputConfig``."""

from typing import TypedDict
from aws_sdk_bedrock_agentcore.errors import DeserializationError

class CloudWatchOutputConfig(TypedDict):
    log_group_name: "str"
    """<p>The name of the CloudWatch log group where evaluation results will be written.</p>"""
    log_stream_name: "str"
    """<p>The name of the CloudWatch log stream where evaluation results will be written.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchOutputConfig) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    out["logStreamName"] = value["log_stream_name"]
    return out


def deserialize_json(data: dict) -> CloudWatchOutputConfig:
    out: CloudWatchOutputConfig = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("CloudWatchOutputConfig.log_group_name required")
    if "logStreamName" in data:
        out["log_stream_name"] = data["logStreamName"]
    else:
        raise DeserializationError("CloudWatchOutputConfig.log_stream_name required")
    return out