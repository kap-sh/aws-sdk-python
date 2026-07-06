"""Generated from Smithy shape ``com.amazonaws.networkmonitor#GetMonitorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_networkmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmonitor.types.aggregation_period
    import aws_sdk_networkmonitor.types.iso8601_timestamp
    import aws_sdk_networkmonitor.types.monitor_arn
    import aws_sdk_networkmonitor.types.monitor_state
    import aws_sdk_networkmonitor.types.probe_list
    import aws_sdk_networkmonitor.types.resource_name
    import aws_sdk_networkmonitor.types.tag_map


class GetMonitorOutput(TypedDict, closed=True):
    monitor_arn: "aws_sdk_networkmonitor.types.monitor_arn.MonitorArn"
    """<p>The ARN of the selected monitor.</p>"""
    monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor. </p>"""
    state: "aws_sdk_networkmonitor.types.monitor_state.MonitorState"
    """<p>Lists the status of the <code>state</code> of each monitor. </p>"""
    aggregation_period: (
        "aws_sdk_networkmonitor.types.aggregation_period.AggregationPeriod"
    )
    """<p>The aggregation period for the specified monitor.</p>"""
    tags: NotRequired["aws_sdk_networkmonitor.types.tag_map.TagMap"]
    """<p>The list of key-value pairs assigned to the monitor.</p>"""
    probes: NotRequired["aws_sdk_networkmonitor.types.probe_list.ProbeList"]
    """<p>The details about each probe associated with that monitor. </p>"""
    created_at: "aws_sdk_networkmonitor.types.iso8601_timestamp.Iso8601Timestamp"
    """<p>The time and date when the monitor was created.</p>"""
    modified_at: "aws_sdk_networkmonitor.types.iso8601_timestamp.Iso8601Timestamp"
    """<p>The time and date when the monitor was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMonitorOutput) -> dict:
    out: dict = {}
    out["monitorArn"] = value["monitor_arn"]
    out["monitorName"] = value["monitor_name"]
    import aws_sdk_networkmonitor.types.monitor_state

    out["state"] = aws_sdk_networkmonitor.types.monitor_state.serialize_json(
        value["state"]
    )
    out["aggregationPeriod"] = value["aggregation_period"]
    if "tags" in value:
        import aws_sdk_networkmonitor.types.tag_map

        out["tags"] = aws_sdk_networkmonitor.types.tag_map.serialize_json(value["tags"])
    if "probes" in value:
        import aws_sdk_networkmonitor.types.probe_list

        out["probes"] = aws_sdk_networkmonitor.types.probe_list.serialize_json(
            value["probes"]
        )
    import aws_sdk_networkmonitor.types.iso8601_timestamp

    out["createdAt"] = aws_sdk_networkmonitor.types.iso8601_timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_networkmonitor.types.iso8601_timestamp

    out["modifiedAt"] = aws_sdk_networkmonitor.types.iso8601_timestamp.serialize_json(
        value["modified_at"]
    )
    return out


def deserialize_json(data: dict) -> GetMonitorOutput:
    out: GetMonitorOutput = {}  # type: ignore[typeddict-item]
    if "monitorArn" in data:
        out["monitor_arn"] = data["monitorArn"]
    else:
        raise DeserializationError("GetMonitorOutput.monitor_arn required")
    if "monitorName" in data:
        out["monitor_name"] = data["monitorName"]
    else:
        raise DeserializationError("GetMonitorOutput.monitor_name required")
    if "state" in data:
        import aws_sdk_networkmonitor.types.monitor_state

        out["state"] = aws_sdk_networkmonitor.types.monitor_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("GetMonitorOutput.state required")
    if "aggregationPeriod" in data:
        out["aggregation_period"] = data["aggregationPeriod"]
    else:
        raise DeserializationError("GetMonitorOutput.aggregation_period required")
    if "tags" in data:
        import aws_sdk_networkmonitor.types.tag_map

        out["tags"] = aws_sdk_networkmonitor.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "probes" in data:
        import aws_sdk_networkmonitor.types.probe_list

        out["probes"] = aws_sdk_networkmonitor.types.probe_list.deserialize_json(
            data["probes"]
        )
    if "createdAt" in data:
        import aws_sdk_networkmonitor.types.iso8601_timestamp

        out["created_at"] = (
            aws_sdk_networkmonitor.types.iso8601_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetMonitorOutput.created_at required")
    if "modifiedAt" in data:
        import aws_sdk_networkmonitor.types.iso8601_timestamp

        out["modified_at"] = (
            aws_sdk_networkmonitor.types.iso8601_timestamp.deserialize_json(
                data["modifiedAt"]
            )
        )
    else:
        raise DeserializationError("GetMonitorOutput.modified_at required")
    return out
