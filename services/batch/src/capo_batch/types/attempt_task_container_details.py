"""Generated from Smithy shape ``com.amazonaws.batch#AttemptTaskContainerDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer
    import capo_batch.types.network_interface_list
    import capo_batch.types.string


class AttemptTaskContainerDetails(TypedDict, closed=True):
    exit_code: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The exit code for the container’s attempt. A non-zero exit code is considered failed.</p>"""
    name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of a container.</p>"""
    reason: NotRequired["capo_batch.types.string.String"]
    """<p>A short (255 max characters) string that's easy to understand and provides additional details for a running or stopped container.</p>"""
    log_stream_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the Amazon CloudWatch Logs log stream that's associated with the container. The log group for Batch jobs is <code>/aws/batch/job</code>. Each container attempt receives a log stream name when they reach the <code>RUNNING</code> status.</p>"""
    network_interfaces: NotRequired[
        "capo_batch.types.network_interface_list.NetworkInterfaceList"
    ]
    """<p>The network interfaces that are associated with the job attempt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttemptTaskContainerDetails) -> dict:
    out: dict = {}
    if "exit_code" in value:
        out["exitCode"] = value["exit_code"]
    if "name" in value:
        out["name"] = value["name"]
    if "reason" in value:
        out["reason"] = value["reason"]
    if "log_stream_name" in value:
        out["logStreamName"] = value["log_stream_name"]
    if "network_interfaces" in value:
        import capo_batch.types.network_interface_list

        out["networkInterfaces"] = (
            capo_batch.types.network_interface_list.serialize_json(
                value["network_interfaces"]
            )
        )
    return out


def deserialize_json(data: dict) -> AttemptTaskContainerDetails:
    out: AttemptTaskContainerDetails = {}  # type: ignore[typeddict-item]
    if "exitCode" in data:
        out["exit_code"] = data["exitCode"]
    if "name" in data:
        out["name"] = data["name"]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "logStreamName" in data:
        out["log_stream_name"] = data["logStreamName"]
    if "networkInterfaces" in data:
        import capo_batch.types.network_interface_list

        out["network_interfaces"] = (
            capo_batch.types.network_interface_list.deserialize_json(
                data["networkInterfaces"]
            )
        )
    return out
