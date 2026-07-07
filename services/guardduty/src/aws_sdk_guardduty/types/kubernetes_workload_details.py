"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesWorkloadDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.boolean
    import aws_sdk_guardduty.types.containers
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.volumes


class KubernetesWorkloadDetails(TypedDict, closed=True):
    name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Kubernetes workload name.</p>"""
    type: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Kubernetes workload type (e.g. Pod, Deployment, etc.).</p>"""
    uid: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Kubernetes workload ID.</p>"""
    namespace: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Kubernetes namespace that the workload is part of.</p>"""
    host_network: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>Whether the hostNetwork flag is enabled for the pods included in the workload.</p>"""
    service_account_name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The service account name that is associated with a Kubernetes workload.</p>"""
    containers: NotRequired["aws_sdk_guardduty.types.containers.Containers"]
    """<p>Containers running as part of the Kubernetes workload.</p>"""
    volumes: NotRequired["aws_sdk_guardduty.types.volumes.Volumes"]
    """<p>Volumes used by the Kubernetes workload.</p>"""
    host_ipc: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>Whether the host IPC flag is enabled for the pods in the workload.</p>"""
    host_pid: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>Whether the host PID flag is enabled for the pods in the workload. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesWorkloadDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "uid" in value:
        out["uid"] = value["uid"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "host_network" in value:
        out["hostNetwork"] = value["host_network"]
    if "service_account_name" in value:
        out["serviceAccountName"] = value["service_account_name"]
    if "containers" in value:
        import aws_sdk_guardduty.types.containers

        out["containers"] = aws_sdk_guardduty.types.containers.serialize_json(
            value["containers"]
        )
    if "volumes" in value:
        import aws_sdk_guardduty.types.volumes

        out["volumes"] = aws_sdk_guardduty.types.volumes.serialize_json(
            value["volumes"]
        )
    if "host_ipc" in value:
        out["hostIPC"] = value["host_ipc"]
    if "host_pid" in value:
        out["hostPID"] = value["host_pid"]
    return out


def deserialize_json(data: dict) -> KubernetesWorkloadDetails:
    out: KubernetesWorkloadDetails = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        out["type"] = data["type"]
    if "uid" in data:
        out["uid"] = data["uid"]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "hostNetwork" in data:
        out["host_network"] = data["hostNetwork"]
    if "serviceAccountName" in data:
        out["service_account_name"] = data["serviceAccountName"]
    if "containers" in data:
        import aws_sdk_guardduty.types.containers

        out["containers"] = aws_sdk_guardduty.types.containers.deserialize_json(
            data["containers"]
        )
    if "volumes" in data:
        import aws_sdk_guardduty.types.volumes

        out["volumes"] = aws_sdk_guardduty.types.volumes.deserialize_json(
            data["volumes"]
        )
    if "hostIPC" in data:
        out["host_ipc"] = data["hostIPC"]
    if "hostPID" in data:
        out["host_pid"] = data["hostPID"]
    return out
