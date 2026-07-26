"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CloudWatchLogsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.cloud_watch_logs_filter_operator
    import capo_bedrock_agentcore.types.filter_value


class CloudWatchLogsFilter(TypedDict, closed=True):
    key: "str"
    """<p>The key or field name to filter on within the agent trace data.</p>"""
    operator: "capo_bedrock_agentcore.types.cloud_watch_logs_filter_operator.CloudWatchLogsFilterOperator"
    """<p>The comparison operator to use for filtering.</p>"""
    value: "capo_bedrock_agentcore.types.filter_value.FilterValue"
    """<p>The value to compare against using the specified operator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogsFilter) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_bedrock_agentcore.types.cloud_watch_logs_filter_operator

    out["operator"] = (
        capo_bedrock_agentcore.types.cloud_watch_logs_filter_operator.serialize_json(
            value["operator"]
        )
    )
    import capo_bedrock_agentcore.types.filter_value

    out["value"] = capo_bedrock_agentcore.types.filter_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> CloudWatchLogsFilter:
    out: CloudWatchLogsFilter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("CloudWatchLogsFilter.key required")
    if "operator" in data:
        import capo_bedrock_agentcore.types.cloud_watch_logs_filter_operator

        out["operator"] = (
            capo_bedrock_agentcore.types.cloud_watch_logs_filter_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        raise DeserializationError("CloudWatchLogsFilter.operator required")
    if "value" in data:
        import capo_bedrock_agentcore.types.filter_value

        out["value"] = capo_bedrock_agentcore.types.filter_value.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("CloudWatchLogsFilter.value required")
    return out
