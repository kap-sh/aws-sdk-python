"""Generated from Smithy shape ``com.amazonaws.batch#EcsTaskProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.boolean
    import capo_batch.types.ephemeral_storage
    import capo_batch.types.list_task_container_properties
    import capo_batch.types.network_configuration
    import capo_batch.types.runtime_platform
    import capo_batch.types.string
    import capo_batch.types.volumes


class EcsTaskProperties(TypedDict, closed=True):
    containers: NotRequired[
        "capo_batch.types.list_task_container_properties.ListTaskContainerProperties"
    ]
    """<p>This object is a list of containers.</p>"""
    ephemeral_storage: NotRequired[
        "capo_batch.types.ephemeral_storage.EphemeralStorage"
    ]
    """<p>The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on Fargate.</p>"""
    execution_role_arn: NotRequired["capo_batch.types.string.String"]
    r"""<p>The Amazon Resource Name (ARN) of the execution role that Batch can assume. For jobs that run on Fargate resources, you must provide an execution role. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html\">Batch execution IAM role</a> in the <i>Batch User Guide</i>.</p>"""
    platform_version: NotRequired["capo_batch.types.string.String"]
    r"""<p>The Fargate platform version where the jobs are running. A platform version is specified only for jobs that are running on Fargate resources. If one isn't specified, the <code>LATEST</code> platform version is used by default. This uses a recent, approved version of the Fargate platform for compute resources. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html\">Fargate platform versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    ipc_mode: NotRequired["capo_batch.types.string.String"]
    r"""<p>The IPC resource namespace to use for the containers in the task. The valid values are <code>host</code>, <code>task</code>, or <code>none</code>.</p> <p>If <code>host</code> is specified, all containers within the tasks that specified the <code>host</code> IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance.</p> <p>If <code>task</code> is specified, all containers within the specified <code>task</code> share the same IPC resources.</p> <p>If <code>none</code> is specified, the IPC resources within the containers of a task are private, and are not shared with other containers in a task or on the container instance. </p> <p>If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance. For more information, see <a href=\"https://docs.docker.com/engine/reference/run/#ipc-settings---ipc\">IPC settings</a> in the Docker run reference.</p>"""
    task_role_arn: NotRequired["capo_batch.types.string.String"]
    r"""<p>The Amazon Resource Name (ARN) that's associated with the Amazon ECS task.</p> <note> <p>This is object is comparable to <a href=\"https://docs.aws.amazon.com/batch/latest/APIReference/API_ContainerProperties.html\">ContainerProperties:jobRoleArn</a>.</p> </note>"""
    pid_mode: NotRequired["capo_batch.types.string.String"]
    r"""<p>The process namespace to use for the containers in the task. The valid values are <code>host</code> or <code>task</code>. For example, monitoring sidecars might need <code>pidMode</code> to access information about other containers running in the same task.</p> <p>If <code>host</code> is specified, all containers within the tasks that specified the <code>host</code> PID mode on the same container instance share the process namespace with the host Amazon EC2 instance.</p> <p>If <code>task</code> is specified, all containers within the specified task share the same process namespace.</p> <p>If no value is specified, the default is a private namespace for each container. For more information, see <a href=\"https://docs.docker.com/engine/reference/run/#pid-settings---pid\">PID settings</a> in the Docker run reference.</p>"""
    network_configuration: NotRequired[
        "capo_batch.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.</p>"""
    runtime_platform: NotRequired["capo_batch.types.runtime_platform.RuntimePlatform"]
    """<p>An object that represents the compute environment architecture for Batch jobs on Fargate.</p>"""
    volumes: NotRequired["capo_batch.types.volumes.Volumes"]
    """<p>A list of volumes that are associated with the job.</p>"""
    enable_execute_command: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Determines whether execute command functionality is turned on for this task. If <code>true</code>, execute command functionality is turned on all the containers in the task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsTaskProperties) -> dict:
    out: dict = {}
    if "containers" in value:
        import capo_batch.types.list_task_container_properties

        out["containers"] = (
            capo_batch.types.list_task_container_properties.serialize_json(
                value["containers"]
            )
        )
    if "ephemeral_storage" in value:
        import capo_batch.types.ephemeral_storage

        out["ephemeralStorage"] = capo_batch.types.ephemeral_storage.serialize_json(
            value["ephemeral_storage"]
        )
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "platform_version" in value:
        out["platformVersion"] = value["platform_version"]
    if "ipc_mode" in value:
        out["ipcMode"] = value["ipc_mode"]
    if "task_role_arn" in value:
        out["taskRoleArn"] = value["task_role_arn"]
    if "pid_mode" in value:
        out["pidMode"] = value["pid_mode"]
    if "network_configuration" in value:
        import capo_batch.types.network_configuration

        out["networkConfiguration"] = (
            capo_batch.types.network_configuration.serialize_json(
                value["network_configuration"]
            )
        )
    if "runtime_platform" in value:
        import capo_batch.types.runtime_platform

        out["runtimePlatform"] = capo_batch.types.runtime_platform.serialize_json(
            value["runtime_platform"]
        )
    if "volumes" in value:
        import capo_batch.types.volumes

        out["volumes"] = capo_batch.types.volumes.serialize_json(value["volumes"])
    if "enable_execute_command" in value:
        out["enableExecuteCommand"] = value["enable_execute_command"]
    return out


def deserialize_json(data: dict) -> EcsTaskProperties:
    out: EcsTaskProperties = {}  # type: ignore[typeddict-item]
    if "containers" in data:
        import capo_batch.types.list_task_container_properties

        out["containers"] = (
            capo_batch.types.list_task_container_properties.deserialize_json(
                data["containers"]
            )
        )
    if "ephemeralStorage" in data:
        import capo_batch.types.ephemeral_storage

        out["ephemeral_storage"] = capo_batch.types.ephemeral_storage.deserialize_json(
            data["ephemeralStorage"]
        )
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    if "platformVersion" in data:
        out["platform_version"] = data["platformVersion"]
    if "ipcMode" in data:
        out["ipc_mode"] = data["ipcMode"]
    if "taskRoleArn" in data:
        out["task_role_arn"] = data["taskRoleArn"]
    if "pidMode" in data:
        out["pid_mode"] = data["pidMode"]
    if "networkConfiguration" in data:
        import capo_batch.types.network_configuration

        out["network_configuration"] = (
            capo_batch.types.network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    if "runtimePlatform" in data:
        import capo_batch.types.runtime_platform

        out["runtime_platform"] = capo_batch.types.runtime_platform.deserialize_json(
            data["runtimePlatform"]
        )
    if "volumes" in data:
        import capo_batch.types.volumes

        out["volumes"] = capo_batch.types.volumes.deserialize_json(data["volumes"])
    if "enableExecuteCommand" in data:
        out["enable_execute_command"] = data["enableExecuteCommand"]
    return out
