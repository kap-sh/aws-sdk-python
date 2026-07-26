"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CloudWatchLogsTraceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.cloud_watch_logs_rule
    import capo_bedrock_agentcore.types.log_group_arn_list
    import capo_bedrock_agentcore.types.service_name_list


class CloudWatchLogsTraceConfig(TypedDict, closed=True):
    log_group_arns: "capo_bedrock_agentcore.types.log_group_arn_list.LogGroupArnList"
    """<p>The list of CloudWatch log group ARNs to read agent traces from.</p>"""
    service_names: "capo_bedrock_agentcore.types.service_name_list.ServiceNameList"
    """<p>The list of service names to filter traces within the specified log groups.</p>"""
    start_time: "datetime.datetime"
    """<p>The start time of the time range to read traces from.</p>"""
    end_time: "datetime.datetime"
    """<p>The end time of the time range to read traces from.</p>"""
    rule: NotRequired[
        "capo_bedrock_agentcore.types.cloud_watch_logs_rule.CloudWatchLogsRule"
    ]
    """<p>Optional rule configuration for filtering traces.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogsTraceConfig) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.log_group_arn_list

    out["logGroupArns"] = (
        capo_bedrock_agentcore.types.log_group_arn_list.serialize_json(
            value["log_group_arns"]
        )
    )
    import capo_bedrock_agentcore.types.service_name_list

    out["serviceNames"] = capo_bedrock_agentcore.types.service_name_list.serialize_json(
        value["service_names"]
    )
    import capo_bedrock_agentcore.types._prelude.timestamp

    out["startTime"] = capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_bedrock_agentcore.types._prelude.timestamp

    out["endTime"] = capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    if "rule" in value:
        import capo_bedrock_agentcore.types.cloud_watch_logs_rule

        out["rule"] = capo_bedrock_agentcore.types.cloud_watch_logs_rule.serialize_json(
            value["rule"]
        )
    return out


def deserialize_json(data: dict) -> CloudWatchLogsTraceConfig:
    out: CloudWatchLogsTraceConfig = {}  # type: ignore[typeddict-item]
    if "logGroupArns" in data:
        import capo_bedrock_agentcore.types.log_group_arn_list

        out["log_group_arns"] = (
            capo_bedrock_agentcore.types.log_group_arn_list.deserialize_json(
                data["logGroupArns"]
            )
        )
    else:
        raise DeserializationError("CloudWatchLogsTraceConfig.log_group_arns required")
    if "serviceNames" in data:
        import capo_bedrock_agentcore.types.service_name_list

        out["service_names"] = (
            capo_bedrock_agentcore.types.service_name_list.deserialize_json(
                data["serviceNames"]
            )
        )
    else:
        raise DeserializationError("CloudWatchLogsTraceConfig.service_names required")
    if "startTime" in data:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["start_time"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("CloudWatchLogsTraceConfig.start_time required")
    if "endTime" in data:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["end_time"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    else:
        raise DeserializationError("CloudWatchLogsTraceConfig.end_time required")
    if "rule" in data:
        import capo_bedrock_agentcore.types.cloud_watch_logs_rule

        out["rule"] = (
            capo_bedrock_agentcore.types.cloud_watch_logs_rule.deserialize_json(
                data["rule"]
            )
        )
    return out
