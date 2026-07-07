"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#CreateMonitorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_networkflowmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.iso8601_timestamp
    import aws_sdk_networkflowmonitor.types.monitor_arn
    import aws_sdk_networkflowmonitor.types.monitor_local_resources
    import aws_sdk_networkflowmonitor.types.monitor_remote_resources
    import aws_sdk_networkflowmonitor.types.monitor_status
    import aws_sdk_networkflowmonitor.types.resource_name
    import aws_sdk_networkflowmonitor.types.tag_map


class CreateMonitorOutput(TypedDict, closed=True):
    monitor_arn: "aws_sdk_networkflowmonitor.types.monitor_arn.MonitorArn"
    """<p>The Amazon Resource Name (ARN) of the monitor.</p>"""
    monitor_name: "aws_sdk_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor. </p>"""
    monitor_status: "aws_sdk_networkflowmonitor.types.monitor_status.MonitorStatus"
    """<p>The status of a monitor. The status can be one of the following</p> <ul> <li> <p> <code>PENDING</code>: The monitor is in the process of being created.</p> </li> <li> <p> <code>ACTIVE</code>: The monitor is active.</p> </li> <li> <p> <code>INACTIVE</code>: The monitor is inactive.</p> </li> <li> <p> <code>ERROR</code>: Monitor creation failed due to an error.</p> </li> <li> <p> <code>DELETING</code>: The monitor is in the process of being deleted.</p> </li> </ul>"""
    local_resources: (
        "aws_sdk_networkflowmonitor.types.monitor_local_resources.MonitorLocalResources"
    )
    """<p>The local resources to monitor. A local resource in a workload is the location of hosts where the Network Flow Monitor agent is installed. </p>"""
    remote_resources: "aws_sdk_networkflowmonitor.types.monitor_remote_resources.MonitorRemoteResources"
    """<p>The remote resources to monitor. A remote resource is the other endpoint specified for the network flow of a workload, with a local resource. For example, Amazon Dynamo DB can be a remote resource. </p>"""
    created_at: "aws_sdk_networkflowmonitor.types.iso8601_timestamp.Iso8601Timestamp"
    """<p>The date and time when the monitor was created.</p>"""
    modified_at: "aws_sdk_networkflowmonitor.types.iso8601_timestamp.Iso8601Timestamp"
    """<p>The last date and time that the monitor was modified.</p>"""
    tags: NotRequired["aws_sdk_networkflowmonitor.types.tag_map.TagMap"]
    """<p>The tags for a monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMonitorOutput) -> dict:
    out: dict = {}
    out["monitorArn"] = value["monitor_arn"]
    out["monitorName"] = value["monitor_name"]
    import aws_sdk_networkflowmonitor.types.monitor_status

    out["monitorStatus"] = (
        aws_sdk_networkflowmonitor.types.monitor_status.serialize_json(
            value["monitor_status"]
        )
    )
    import aws_sdk_networkflowmonitor.types.monitor_local_resources

    out["localResources"] = (
        aws_sdk_networkflowmonitor.types.monitor_local_resources.serialize_json(
            value["local_resources"]
        )
    )
    import aws_sdk_networkflowmonitor.types.monitor_remote_resources

    out["remoteResources"] = (
        aws_sdk_networkflowmonitor.types.monitor_remote_resources.serialize_json(
            value["remote_resources"]
        )
    )
    import aws_sdk_networkflowmonitor.types.iso8601_timestamp

    out["createdAt"] = (
        aws_sdk_networkflowmonitor.types.iso8601_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_networkflowmonitor.types.iso8601_timestamp

    out["modifiedAt"] = (
        aws_sdk_networkflowmonitor.types.iso8601_timestamp.serialize_json(
            value["modified_at"]
        )
    )
    if "tags" in value:
        import aws_sdk_networkflowmonitor.types.tag_map

        out["tags"] = aws_sdk_networkflowmonitor.types.tag_map.serialize_json(
            value["tags"]
        )
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
    if "monitorStatus" in data:
        import aws_sdk_networkflowmonitor.types.monitor_status

        out["monitor_status"] = (
            aws_sdk_networkflowmonitor.types.monitor_status.deserialize_json(
                data["monitorStatus"]
            )
        )
    else:
        raise DeserializationError("CreateMonitorOutput.monitor_status required")
    if "localResources" in data:
        import aws_sdk_networkflowmonitor.types.monitor_local_resources

        out["local_resources"] = (
            aws_sdk_networkflowmonitor.types.monitor_local_resources.deserialize_json(
                data["localResources"]
            )
        )
    else:
        raise DeserializationError("CreateMonitorOutput.local_resources required")
    if "remoteResources" in data:
        import aws_sdk_networkflowmonitor.types.monitor_remote_resources

        out["remote_resources"] = (
            aws_sdk_networkflowmonitor.types.monitor_remote_resources.deserialize_json(
                data["remoteResources"]
            )
        )
    else:
        raise DeserializationError("CreateMonitorOutput.remote_resources required")
    if "createdAt" in data:
        import aws_sdk_networkflowmonitor.types.iso8601_timestamp

        out["created_at"] = (
            aws_sdk_networkflowmonitor.types.iso8601_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreateMonitorOutput.created_at required")
    if "modifiedAt" in data:
        import aws_sdk_networkflowmonitor.types.iso8601_timestamp

        out["modified_at"] = (
            aws_sdk_networkflowmonitor.types.iso8601_timestamp.deserialize_json(
                data["modifiedAt"]
            )
        )
    else:
        raise DeserializationError("CreateMonitorOutput.modified_at required")
    if "tags" in data:
        import aws_sdk_networkflowmonitor.types.tag_map

        out["tags"] = aws_sdk_networkflowmonitor.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
