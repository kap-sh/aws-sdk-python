"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CloudWatchLogsRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.cloud_watch_logs_filter_list


class CloudWatchLogsRule(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_bedrock_agentcore.types.cloud_watch_logs_filter_list.CloudWatchLogsFilterList"
    ]
    """<p>The list of filters to apply when reading agent traces.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogsRule) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_bedrock_agentcore.types.cloud_watch_logs_filter_list

        out["filters"] = (
            aws_sdk_bedrock_agentcore.types.cloud_watch_logs_filter_list.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> CloudWatchLogsRule:
    out: CloudWatchLogsRule = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_bedrock_agentcore.types.cloud_watch_logs_filter_list

        out["filters"] = (
            aws_sdk_bedrock_agentcore.types.cloud_watch_logs_filter_list.deserialize_json(
                data["filters"]
            )
        )
    return out
