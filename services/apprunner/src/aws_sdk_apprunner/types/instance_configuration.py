"""Generated from Smithy shape ``com.amazonaws.apprunner#InstanceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.cpu
    import aws_sdk_apprunner.types.memory
    import aws_sdk_apprunner.types.role_arn


class InstanceConfiguration(TypedDict, closed=True):
    cpu: NotRequired["aws_sdk_apprunner.types.cpu.Cpu"]
    """<p>The number of CPU units reserved for each instance of your App Runner service.</p> <p>Default: <code>1 vCPU</code> </p>"""
    memory: NotRequired["aws_sdk_apprunner.types.memory.Memory"]
    """<p>The amount of memory, in MB or GB, reserved for each instance of your App Runner service.</p> <p>Default: <code>2 GB</code> </p>"""
    instance_role_arn: NotRequired["aws_sdk_apprunner.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that provides permissions to your App Runner service. These are permissions that your code needs when it calls any Amazon Web Services APIs.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceConfiguration) -> dict:
    out: dict = {}
    if "cpu" in value:
        out["Cpu"] = value["cpu"]
    if "memory" in value:
        out["Memory"] = value["memory"]
    if "instance_role_arn" in value:
        out["InstanceRoleArn"] = value["instance_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceConfiguration:
    out: InstanceConfiguration = {}  # type: ignore[typeddict-item]
    if "Cpu" in data:
        out["cpu"] = data["Cpu"]
    if "Memory" in data:
        out["memory"] = data["Memory"]
    if "InstanceRoleArn" in data:
        out["instance_role_arn"] = data["InstanceRoleArn"]
    return out
