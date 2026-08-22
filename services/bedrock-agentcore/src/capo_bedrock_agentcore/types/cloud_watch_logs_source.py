"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CloudWatchLogsSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.cloud_watch_filter_config
    import capo_bedrock_agentcore.types.evaluation_string_list


class CloudWatchLogsSource(TypedDict, closed=True):
    service_names: (
        "capo_bedrock_agentcore.types.evaluation_string_list.EvaluationStringList"
    )
    """<p>The list of agent service names to filter traces within the specified log groups.</p>"""
    log_group_names: (
        "capo_bedrock_agentcore.types.evaluation_string_list.EvaluationStringList"
    )
    """<p>The list of CloudWatch log group names to read agent traces from. Maximum of 5 log groups.</p>"""
    filter_config: NotRequired[
        "capo_bedrock_agentcore.types.cloud_watch_filter_config.CloudWatchFilterConfig"
    ]
    """<p>Optional filter configuration to narrow down which sessions to evaluate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogsSource) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.evaluation_string_list

    out["serviceNames"] = (
        capo_bedrock_agentcore.types.evaluation_string_list.serialize_json(
            value["service_names"]
        )
    )
    import capo_bedrock_agentcore.types.evaluation_string_list

    out["logGroupNames"] = (
        capo_bedrock_agentcore.types.evaluation_string_list.serialize_json(
            value["log_group_names"]
        )
    )
    if "filter_config" in value:
        import capo_bedrock_agentcore.types.cloud_watch_filter_config

        out["filterConfig"] = (
            capo_bedrock_agentcore.types.cloud_watch_filter_config.serialize_json(
                value["filter_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CloudWatchLogsSource:
    out: CloudWatchLogsSource = {}  # type: ignore[typeddict-item]
    if data.get("serviceNames") is not None:
        import capo_bedrock_agentcore.types.evaluation_string_list

        out["service_names"] = (
            capo_bedrock_agentcore.types.evaluation_string_list.deserialize_json(
                data["serviceNames"]
            )
        )
    else:
        raise DeserializationError("CloudWatchLogsSource.service_names required")
    if data.get("logGroupNames") is not None:
        import capo_bedrock_agentcore.types.evaluation_string_list

        out["log_group_names"] = (
            capo_bedrock_agentcore.types.evaluation_string_list.deserialize_json(
                data["logGroupNames"]
            )
        )
    else:
        raise DeserializationError("CloudWatchLogsSource.log_group_names required")
    if data.get("filterConfig") is not None:
        import capo_bedrock_agentcore.types.cloud_watch_filter_config

        out["filter_config"] = (
            capo_bedrock_agentcore.types.cloud_watch_filter_config.deserialize_json(
                data["filterConfig"]
            )
        )
    return out
