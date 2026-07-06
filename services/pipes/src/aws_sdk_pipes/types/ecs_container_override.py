"""Generated from Smithy shape ``com.amazonaws.pipes#EcsContainerOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pipes.types.ecs_environment_file_list
    import aws_sdk_pipes.types.ecs_environment_variable_list
    import aws_sdk_pipes.types.ecs_resource_requirements_list
    import aws_sdk_pipes.types.string
    import aws_sdk_pipes.types.string_list


class EcsContainerOverride(TypedDict, closed=True):
    command: NotRequired["aws_sdk_pipes.types.string_list.StringList"]
    """<p>The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.</p>"""
    cpu: NotRequired["int"]
    """<p>The number of <code>cpu</code> units reserved for the container, instead of the default value from the task definition. You must also specify a container name.</p>"""
    environment: NotRequired[
        "aws_sdk_pipes.types.ecs_environment_variable_list.EcsEnvironmentVariableList"
    ]
    """<p>The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.</p>"""
    environment_files: NotRequired[
        "aws_sdk_pipes.types.ecs_environment_file_list.EcsEnvironmentFileList"
    ]
    """<p>A list of files containing the environment variables to pass to a container, instead of the value from the container definition.</p>"""
    memory: NotRequired["int"]
    """<p>The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.</p>"""
    memory_reservation: NotRequired["int"]
    """<p>The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.</p>"""
    name: NotRequired["aws_sdk_pipes.types.string.String"]
    """<p>The name of the container that receives the override. This parameter is required if any override is specified.</p>"""
    resource_requirements: NotRequired[
        "aws_sdk_pipes.types.ecs_resource_requirements_list.EcsResourceRequirementsList"
    ]
    """<p>The type and amount of a resource to assign to a container, instead of the default value from the task definition. The only supported resource is a GPU.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsContainerOverride) -> dict:
    out: dict = {}
    if "command" in value:
        import aws_sdk_pipes.types.string_list

        out["Command"] = aws_sdk_pipes.types.string_list.serialize_json(
            value["command"]
        )
    if "cpu" in value:
        out["Cpu"] = value["cpu"]
    if "environment" in value:
        import aws_sdk_pipes.types.ecs_environment_variable_list

        out["Environment"] = (
            aws_sdk_pipes.types.ecs_environment_variable_list.serialize_json(
                value["environment"]
            )
        )
    if "environment_files" in value:
        import aws_sdk_pipes.types.ecs_environment_file_list

        out["EnvironmentFiles"] = (
            aws_sdk_pipes.types.ecs_environment_file_list.serialize_json(
                value["environment_files"]
            )
        )
    if "memory" in value:
        out["Memory"] = value["memory"]
    if "memory_reservation" in value:
        out["MemoryReservation"] = value["memory_reservation"]
    if "name" in value:
        out["Name"] = value["name"]
    if "resource_requirements" in value:
        import aws_sdk_pipes.types.ecs_resource_requirements_list

        out["ResourceRequirements"] = (
            aws_sdk_pipes.types.ecs_resource_requirements_list.serialize_json(
                value["resource_requirements"]
            )
        )
    return out


def deserialize_json(data: dict) -> EcsContainerOverride:
    out: EcsContainerOverride = {}  # type: ignore[typeddict-item]
    if "Command" in data:
        import aws_sdk_pipes.types.string_list

        out["command"] = aws_sdk_pipes.types.string_list.deserialize_json(
            data["Command"]
        )
    if "Cpu" in data:
        out["cpu"] = data["Cpu"]
    if "Environment" in data:
        import aws_sdk_pipes.types.ecs_environment_variable_list

        out["environment"] = (
            aws_sdk_pipes.types.ecs_environment_variable_list.deserialize_json(
                data["Environment"]
            )
        )
    if "EnvironmentFiles" in data:
        import aws_sdk_pipes.types.ecs_environment_file_list

        out["environment_files"] = (
            aws_sdk_pipes.types.ecs_environment_file_list.deserialize_json(
                data["EnvironmentFiles"]
            )
        )
    if "Memory" in data:
        out["memory"] = data["Memory"]
    if "MemoryReservation" in data:
        out["memory_reservation"] = data["MemoryReservation"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ResourceRequirements" in data:
        import aws_sdk_pipes.types.ecs_resource_requirements_list

        out["resource_requirements"] = (
            aws_sdk_pipes.types.ecs_resource_requirements_list.deserialize_json(
                data["ResourceRequirements"]
            )
        )
    return out
