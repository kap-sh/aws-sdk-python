"""Generated from Smithy shape ``com.amazonaws.batch#AttemptContainerDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.network_interface_list
    import aws_sdk_batch.types.string


class AttemptContainerDetail(TypedDict, closed=True):
    container_instance_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon ECS container instance that hosts the job attempt.</p>"""
    task_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon ECS task that's associated with the job attempt. Each container attempt receives a task ARN when they reach the <code>STARTING</code> status.</p>"""
    exit_code: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The exit code for the job attempt. A non-zero exit code is considered failed.</p>"""
    reason: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>A short (255 max characters) human-readable string to provide additional details for a running or stopped container.</p>"""
    log_stream_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the CloudWatch Logs log stream that's associated with the container. The log group for Batch jobs is <code>/aws/batch/job</code>. Each container attempt receives a log stream name when they reach the <code>RUNNING</code> status.</p>"""
    network_interfaces: NotRequired[
        "aws_sdk_batch.types.network_interface_list.NetworkInterfaceList"
    ]
    """<p>The network interfaces that are associated with the job attempt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttemptContainerDetail) -> dict:
    out: dict = {}
    if "container_instance_arn" in value:
        out["containerInstanceArn"] = value["container_instance_arn"]
    if "task_arn" in value:
        out["taskArn"] = value["task_arn"]
    if "exit_code" in value:
        out["exitCode"] = value["exit_code"]
    if "reason" in value:
        out["reason"] = value["reason"]
    if "log_stream_name" in value:
        out["logStreamName"] = value["log_stream_name"]
    if "network_interfaces" in value:
        import aws_sdk_batch.types.network_interface_list

        out["networkInterfaces"] = (
            aws_sdk_batch.types.network_interface_list.serialize_json(
                value["network_interfaces"]
            )
        )
    return out


def deserialize_json(data: dict) -> AttemptContainerDetail:
    out: AttemptContainerDetail = {}  # type: ignore[typeddict-item]
    if "containerInstanceArn" in data:
        out["container_instance_arn"] = data["containerInstanceArn"]
    if "taskArn" in data:
        out["task_arn"] = data["taskArn"]
    if "exitCode" in data:
        out["exit_code"] = data["exitCode"]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "logStreamName" in data:
        out["log_stream_name"] = data["logStreamName"]
    if "networkInterfaces" in data:
        import aws_sdk_batch.types.network_interface_list

        out["network_interfaces"] = (
            aws_sdk_batch.types.network_interface_list.deserialize_json(
                data["networkInterfaces"]
            )
        )
    return out
