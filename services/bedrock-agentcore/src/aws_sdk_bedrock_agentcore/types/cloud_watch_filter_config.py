"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CloudWatchFilterConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.evaluation_string_list
    import aws_sdk_bedrock_agentcore.types.session_filter_config


class CloudWatchFilterConfig(TypedDict):
    session_ids: NotRequired[
        "aws_sdk_bedrock_agentcore.types.evaluation_string_list.EvaluationStringList"
    ]
    """<p>A list of specific session IDs to evaluate. If specified, only these sessions are included in the evaluation.</p>"""
    time_range: NotRequired[
        "aws_sdk_bedrock_agentcore.types.session_filter_config.SessionFilterConfig"
    ]
    """<p>The time range filter for selecting sessions to evaluate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchFilterConfig) -> dict:
    out: dict = {}
    if "session_ids" in value:
        import aws_sdk_bedrock_agentcore.types.evaluation_string_list

        out["sessionIds"] = (
            aws_sdk_bedrock_agentcore.types.evaluation_string_list.serialize_json(
                value["session_ids"]
            )
        )
    if "time_range" in value:
        import aws_sdk_bedrock_agentcore.types.session_filter_config

        out["timeRange"] = (
            aws_sdk_bedrock_agentcore.types.session_filter_config.serialize_json(
                value["time_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> CloudWatchFilterConfig:
    out: CloudWatchFilterConfig = {}  # type: ignore[typeddict-item]
    if "sessionIds" in data:
        import aws_sdk_bedrock_agentcore.types.evaluation_string_list

        out["session_ids"] = (
            aws_sdk_bedrock_agentcore.types.evaluation_string_list.deserialize_json(
                data["sessionIds"]
            )
        )
    if "timeRange" in data:
        import aws_sdk_bedrock_agentcore.types.session_filter_config

        out["time_range"] = (
            aws_sdk_bedrock_agentcore.types.session_filter_config.deserialize_json(
                data["timeRange"]
            )
        )
    return out
