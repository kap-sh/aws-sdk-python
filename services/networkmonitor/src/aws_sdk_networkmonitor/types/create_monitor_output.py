"""Generated from Smithy shape ``com.amazonaws.networkmonitor#CreateMonitorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_networkmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmonitor.types.aggregation_period
    import aws_sdk_networkmonitor.types.monitor_arn
    import aws_sdk_networkmonitor.types.monitor_state
    import aws_sdk_networkmonitor.types.resource_name
    import aws_sdk_networkmonitor.types.tag_map


class CreateMonitorOutput(TypedDict, closed=True):
    monitor_arn: "aws_sdk_networkmonitor.types.monitor_arn.MonitorArn"
    """<p>The ARN of the monitor.</p>"""
    monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    state: "aws_sdk_networkmonitor.types.monitor_state.MonitorState"
    """<p>The state of the monitor.</p>"""
    aggregation_period: NotRequired[
        "aws_sdk_networkmonitor.types.aggregation_period.AggregationPeriod"
    ]
    """<p>The number of seconds that metrics are aggregated by and sent to Amazon CloudWatch. This will be either <code>30</code> or <code>60</code>. </p>"""
    tags: NotRequired["aws_sdk_networkmonitor.types.tag_map.TagMap"]
    """<p>The list of key-value pairs assigned to the monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMonitorOutput) -> dict:
    out: dict = {}
    out["monitorArn"] = value["monitor_arn"]
    out["monitorName"] = value["monitor_name"]
    import aws_sdk_networkmonitor.types.monitor_state

    out["state"] = aws_sdk_networkmonitor.types.monitor_state.serialize_json(
        value["state"]
    )
    if "aggregation_period" in value:
        out["aggregationPeriod"] = value["aggregation_period"]
    if "tags" in value:
        import aws_sdk_networkmonitor.types.tag_map

        out["tags"] = aws_sdk_networkmonitor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMonitorOutput:
    out: CreateMonitorOutput = {}  # type: ignore[typeddict-item]
    if "monitorArn" in data:
        out["monitor_arn"] = data["monitorArn"]
    else:
        raise DeserializationError("CreateMonitorOutput.monitor_arn required")
    if "monitorName" in data:
        out["monitor_name"] = data["monitorName"]
    else:
        raise DeserializationError("CreateMonitorOutput.monitor_name required")
    if "state" in data:
        import aws_sdk_networkmonitor.types.monitor_state

        out["state"] = aws_sdk_networkmonitor.types.monitor_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("CreateMonitorOutput.state required")
    if "aggregationPeriod" in data:
        out["aggregation_period"] = data["aggregationPeriod"]
    if "tags" in data:
        import aws_sdk_networkmonitor.types.tag_map

        out["tags"] = aws_sdk_networkmonitor.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
