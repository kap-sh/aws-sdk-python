"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CloudWatchLogsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.cloud_watch_logs_filter

CloudWatchLogsFilterList: TypeAlias = list[
    "capo_bedrock_agentcore.types.cloud_watch_logs_filter.CloudWatchLogsFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogsFilterList) -> list:
    import capo_bedrock_agentcore.types.cloud_watch_logs_filter

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.cloud_watch_logs_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CloudWatchLogsFilterList:
    import capo_bedrock_agentcore.types.cloud_watch_logs_filter

    out: CloudWatchLogsFilterList = []
    for item in data:
        out.append(
            capo_bedrock_agentcore.types.cloud_watch_logs_filter.deserialize_json(item)
        )
    return out
