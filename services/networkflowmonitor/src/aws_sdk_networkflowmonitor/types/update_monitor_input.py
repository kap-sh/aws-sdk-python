"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#UpdateMonitorInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.monitor_local_resources
    import aws_sdk_networkflowmonitor.types.monitor_remote_resources
    import aws_sdk_networkflowmonitor.types.resource_name
    import aws_sdk_networkflowmonitor.types.uuid_string


class UpdateMonitorInput(TypedDict):
    monitor_name: "aws_sdk_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    local_resources_to_add: NotRequired[
        "aws_sdk_networkflowmonitor.types.monitor_local_resources.MonitorLocalResources"
    ]
    """<p>Additional local resources to specify network flows for a monitor, as an array of resources with identifiers and types. A local resource in a workload is the location of hosts where the Network Flow Monitor agent is installed. </p>"""
    local_resources_to_remove: NotRequired[
        "aws_sdk_networkflowmonitor.types.monitor_local_resources.MonitorLocalResources"
    ]
    """<p>The local resources to remove, as an array of resources with identifiers and types.</p>"""
    remote_resources_to_add: NotRequired[
        "aws_sdk_networkflowmonitor.types.monitor_remote_resources.MonitorRemoteResources"
    ]
    """<p>The remote resources to add, as an array of resources with identifiers and types.</p> <p>A remote resource is the other endpoint in the flow of a workload, with a local resource. For example, Amazon Dynamo DB can be a remote resource. </p>"""
    remote_resources_to_remove: NotRequired[
        "aws_sdk_networkflowmonitor.types.monitor_remote_resources.MonitorRemoteResources"
    ]
    """<p>The remote resources to remove, as an array of resources with identifiers and types.</p> <p>A remote resource is the other endpoint specified for the network flow of a workload, with a local resource. For example, Amazon Dynamo DB can be a remote resource. </p>"""
    client_token: NotRequired["aws_sdk_networkflowmonitor.types.uuid_string.UuidString"]
    """<p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Don't reuse the same client token for other API requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMonitorInput) -> dict:
    out: dict = {}
    if "local_resources_to_add" in value:
        import aws_sdk_networkflowmonitor.types.monitor_local_resources

        out["localResourcesToAdd"] = (
            aws_sdk_networkflowmonitor.types.monitor_local_resources.serialize_json(
                value["local_resources_to_add"]
            )
        )
    if "local_resources_to_remove" in value:
        import aws_sdk_networkflowmonitor.types.monitor_local_resources

        out["localResourcesToRemove"] = (
            aws_sdk_networkflowmonitor.types.monitor_local_resources.serialize_json(
                value["local_resources_to_remove"]
            )
        )
    if "remote_resources_to_add" in value:
        import aws_sdk_networkflowmonitor.types.monitor_remote_resources

        out["remoteResourcesToAdd"] = (
            aws_sdk_networkflowmonitor.types.monitor_remote_resources.serialize_json(
                value["remote_resources_to_add"]
            )
        )
    if "remote_resources_to_remove" in value:
        import aws_sdk_networkflowmonitor.types.monitor_remote_resources

        out["remoteResourcesToRemove"] = (
            aws_sdk_networkflowmonitor.types.monitor_remote_resources.serialize_json(
                value["remote_resources_to_remove"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateMonitorInput:
    out: UpdateMonitorInput = {}  # type: ignore[typeddict-item]
    if "localResourcesToAdd" in data:
        import aws_sdk_networkflowmonitor.types.monitor_local_resources

        out["local_resources_to_add"] = (
            aws_sdk_networkflowmonitor.types.monitor_local_resources.deserialize_json(
                data["localResourcesToAdd"]
            )
        )
    if "localResourcesToRemove" in data:
        import aws_sdk_networkflowmonitor.types.monitor_local_resources

        out["local_resources_to_remove"] = (
            aws_sdk_networkflowmonitor.types.monitor_local_resources.deserialize_json(
                data["localResourcesToRemove"]
            )
        )
    if "remoteResourcesToAdd" in data:
        import aws_sdk_networkflowmonitor.types.monitor_remote_resources

        out["remote_resources_to_add"] = (
            aws_sdk_networkflowmonitor.types.monitor_remote_resources.deserialize_json(
                data["remoteResourcesToAdd"]
            )
        )
    if "remoteResourcesToRemove" in data:
        import aws_sdk_networkflowmonitor.types.monitor_remote_resources

        out["remote_resources_to_remove"] = (
            aws_sdk_networkflowmonitor.types.monitor_remote_resources.deserialize_json(
                data["remoteResourcesToRemove"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
