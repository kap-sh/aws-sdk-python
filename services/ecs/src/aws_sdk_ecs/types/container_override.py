"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.environment_files
    import aws_sdk_ecs.types.environment_variables
    import aws_sdk_ecs.types.resource_requirements
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class ContainerOverride(TypedDict, closed=True):
    name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the container that receives the override. This parameter is required if any override is specified.</p>"""
    command: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.</p>"""
    environment: NotRequired[
        "aws_sdk_ecs.types.environment_variables.EnvironmentVariables"
    ]
    """<p>The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.</p>"""
    environment_files: NotRequired[
        "aws_sdk_ecs.types.environment_files.EnvironmentFiles"
    ]
    """<p>A list of files containing the environment variables to pass to a container, instead of the value from the container definition.</p>"""
    cpu: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The number of <code>cpu</code> units reserved for the container, instead of the default value from the task definition. You must also specify a container name.</p>"""
    memory: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.</p>"""
    memory_reservation: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.</p>"""
    resource_requirements: NotRequired[
        "aws_sdk_ecs.types.resource_requirements.ResourceRequirements"
    ]
    """<p>The type and amount of a resource to assign to a container, instead of the default value from the task definition. The supported resources are GPUs and Neuron devices.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerOverride) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "command" in value:
        import aws_sdk_ecs.types.string_list

        out["command"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
            value["command"]
        )
    if "environment" in value:
        import aws_sdk_ecs.types.environment_variables

        out["environment"] = (
            aws_sdk_ecs.types.environment_variables.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "environment_files" in value:
        import aws_sdk_ecs.types.environment_files

        out["environmentFiles"] = (
            aws_sdk_ecs.types.environment_files.serialize_aws_json_1_1(
                value["environment_files"]
            )
        )
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "memory_reservation" in value:
        out["memoryReservation"] = value["memory_reservation"]
    if "resource_requirements" in value:
        import aws_sdk_ecs.types.resource_requirements

        out["resourceRequirements"] = (
            aws_sdk_ecs.types.resource_requirements.serialize_aws_json_1_1(
                value["resource_requirements"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerOverride:
    out: ContainerOverride = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "command" in data:
        import aws_sdk_ecs.types.string_list

        out["command"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["command"]
        )
    if "environment" in data:
        import aws_sdk_ecs.types.environment_variables

        out["environment"] = (
            aws_sdk_ecs.types.environment_variables.deserialize_aws_json_1_1(
                data["environment"]
            )
        )
    if "environmentFiles" in data:
        import aws_sdk_ecs.types.environment_files

        out["environment_files"] = (
            aws_sdk_ecs.types.environment_files.deserialize_aws_json_1_1(
                data["environmentFiles"]
            )
        )
    if "cpu" in data:
        out["cpu"] = data["cpu"]
    if "memory" in data:
        out["memory"] = data["memory"]
    if "memoryReservation" in data:
        out["memory_reservation"] = data["memoryReservation"]
    if "resourceRequirements" in data:
        import aws_sdk_ecs.types.resource_requirements

        out["resource_requirements"] = (
            aws_sdk_ecs.types.resource_requirements.deserialize_aws_json_1_1(
                data["resourceRequirements"]
            )
        )
    return out
