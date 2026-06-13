"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CloudWatchLogsInputConfig``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.log_group_names_list
    import aws_sdk_bedrock_agentcore_control.types.service_names_list

class CloudWatchLogsInputConfig(TypedDict):
    log_group_names: "aws_sdk_bedrock_agentcore_control.types.log_group_names_list.LogGroupNamesList"
    """<p> The list of CloudWatch log group names to monitor for agent traces.</p>"""
    service_names: "aws_sdk_bedrock_agentcore_control.types.service_names_list.ServiceNamesList"
    """<p> The list of service names to filter traces within the specified log groups. Used to identify relevant agent sessions. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogsInputConfig) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.log_group_names_list
    out["logGroupNames"] = aws_sdk_bedrock_agentcore_control.types.log_group_names_list.serialize_json(value["log_group_names"])
    import aws_sdk_bedrock_agentcore_control.types.service_names_list
    out["serviceNames"] = aws_sdk_bedrock_agentcore_control.types.service_names_list.serialize_json(value["service_names"])
    return out


def deserialize_json(data: dict) -> CloudWatchLogsInputConfig:
    out: CloudWatchLogsInputConfig = {}  # type: ignore[typeddict-item]
    if "logGroupNames" in data:
        import aws_sdk_bedrock_agentcore_control.types.log_group_names_list
        out["log_group_names"] = aws_sdk_bedrock_agentcore_control.types.log_group_names_list.deserialize_json(data["logGroupNames"])
    else:
        raise DeserializationError("CloudWatchLogsInputConfig.log_group_names required")
    if "serviceNames" in data:
        import aws_sdk_bedrock_agentcore_control.types.service_names_list
        out["service_names"] = aws_sdk_bedrock_agentcore_control.types.service_names_list.deserialize_json(data["serviceNames"])
    else:
        raise DeserializationError("CloudWatchLogsInputConfig.service_names required")
    return out