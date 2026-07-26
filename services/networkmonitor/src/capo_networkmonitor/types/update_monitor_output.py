"""Generated from Smithy shape ``com.amazonaws.networkmonitor#UpdateMonitorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_networkmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_networkmonitor.types.aggregation_period
    import capo_networkmonitor.types.monitor_arn
    import capo_networkmonitor.types.monitor_state
    import capo_networkmonitor.types.resource_name
    import capo_networkmonitor.types.tag_map


class UpdateMonitorOutput(TypedDict, closed=True):
    monitor_arn: "capo_networkmonitor.types.monitor_arn.MonitorArn"
    """<p>The ARN of the monitor that was updated.</p>"""
    monitor_name: "capo_networkmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor that was updated.</p>"""
    state: "capo_networkmonitor.types.monitor_state.MonitorState"
    """<p>The state of the updated monitor.</p>"""
    aggregation_period: NotRequired[
        "capo_networkmonitor.types.aggregation_period.AggregationPeriod"
    ]
    """<p>The changed aggregation period.</p>"""
    tags: NotRequired["capo_networkmonitor.types.tag_map.TagMap"]
    """<p>The list of key-value pairs associated with the monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMonitorOutput) -> dict:
    out: dict = {}
    out["monitorArn"] = value["monitor_arn"]
    out["monitorName"] = value["monitor_name"]
    import capo_networkmonitor.types.monitor_state

    out["state"] = capo_networkmonitor.types.monitor_state.serialize_json(
        value["state"]
    )
    if "aggregation_period" in value:
        out["aggregationPeriod"] = value["aggregation_period"]
    if "tags" in value:
        import capo_networkmonitor.types.tag_map

        out["tags"] = capo_networkmonitor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> UpdateMonitorOutput:
    out: UpdateMonitorOutput = {}  # type: ignore[typeddict-item]
    if "monitorArn" in data:
        out["monitor_arn"] = data["monitorArn"]
    else:
        raise DeserializationError("UpdateMonitorOutput.monitor_arn required")
    if "monitorName" in data:
        out["monitor_name"] = data["monitorName"]
    else:
        raise DeserializationError("UpdateMonitorOutput.monitor_name required")
    if "state" in data:
        import capo_networkmonitor.types.monitor_state

        out["state"] = capo_networkmonitor.types.monitor_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("UpdateMonitorOutput.state required")
    if "aggregationPeriod" in data:
        out["aggregation_period"] = data["aggregationPeriod"]
    if "tags" in data:
        import capo_networkmonitor.types.tag_map

        out["tags"] = capo_networkmonitor.types.tag_map.deserialize_json(data["tags"])
    return out
