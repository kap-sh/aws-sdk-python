"""Generated from Smithy shape ``com.amazonaws.networkmonitor#CreateMonitorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_networkmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmonitor.types.aggregation_period
    import aws_sdk_networkmonitor.types.create_monitor_probe_input_list
    import aws_sdk_networkmonitor.types.resource_name
    import aws_sdk_networkmonitor.types.tag_map


class CreateMonitorInput(TypedDict, closed=True):
    monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName"
    """<p>The name identifying the monitor. It can contain only letters, underscores (_), or dashes (-), and can be up to 200 characters.</p>"""
    probes: NotRequired[
        "aws_sdk_networkmonitor.types.create_monitor_probe_input_list.CreateMonitorProbeInputList"
    ]
    """<p>Displays a list of all of the probes created for a monitor.</p>"""
    aggregation_period: NotRequired[
        "aws_sdk_networkmonitor.types.aggregation_period.AggregationPeriod"
    ]
    """<p>The time, in seconds, that metrics are aggregated and sent to Amazon CloudWatch. Valid values are either <code>30</code> or <code>60</code>. <code>60</code> is the default if no period is chosen.</p>"""
    client_token: NotRequired["str"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>"""
    tags: NotRequired["aws_sdk_networkmonitor.types.tag_map.TagMap"]
    """<p>The list of key-value pairs created and assigned to the monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMonitorInput) -> dict:
    out: dict = {}
    out["monitorName"] = value["monitor_name"]
    if "probes" in value:
        import aws_sdk_networkmonitor.types.create_monitor_probe_input_list

        out["probes"] = (
            aws_sdk_networkmonitor.types.create_monitor_probe_input_list.serialize_json(
                value["probes"]
            )
        )
    if "aggregation_period" in value:
        out["aggregationPeriod"] = value["aggregation_period"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_networkmonitor.types.tag_map

        out["tags"] = aws_sdk_networkmonitor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMonitorInput:
    out: CreateMonitorInput = {}  # type: ignore[typeddict-item]
    if "monitorName" in data:
        out["monitor_name"] = data["monitorName"]
    else:
        raise DeserializationError("CreateMonitorInput.monitor_name required")
    if "probes" in data:
        import aws_sdk_networkmonitor.types.create_monitor_probe_input_list

        out["probes"] = (
            aws_sdk_networkmonitor.types.create_monitor_probe_input_list.deserialize_json(
                data["probes"]
            )
        )
    if "aggregationPeriod" in data:
        out["aggregation_period"] = data["aggregationPeriod"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_networkmonitor.types.tag_map

        out["tags"] = aws_sdk_networkmonitor.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
