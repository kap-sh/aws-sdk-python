"""Generated from Smithy shape ``com.amazonaws.pipes#BatchContainerOverrides``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pipes.types.batch_environment_variable_list
    import aws_sdk_pipes.types.batch_resource_requirements_list
    import aws_sdk_pipes.types.string_list


class BatchContainerOverrides(TypedDict):
    command: NotRequired["aws_sdk_pipes.types.string_list.StringList"]
    """<p>The command to send to the container that overrides the default command from the Docker image or the task definition.</p>"""
    environment: NotRequired[
        "aws_sdk_pipes.types.batch_environment_variable_list.BatchEnvironmentVariableList"
    ]
    r"""<p>The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition.</p> <note> <p>Environment variables cannot start with \"<code>Batch</code>\". This naming convention is reserved for variables that Batch sets.</p> </note>"""
    instance_type: NotRequired["str"]
    """<p>The instance type to use for a multi-node parallel job.</p> <note> <p>This parameter isn't applicable to single-node container jobs or jobs that run on Fargate resources, and shouldn't be provided.</p> </note>"""
    resource_requirements: NotRequired[
        "aws_sdk_pipes.types.batch_resource_requirements_list.BatchResourceRequirementsList"
    ]
    """<p>The type and amount of resources to assign to a container. This overrides the settings in the job definition. The supported resources include <code>GPU</code>, <code>MEMORY</code>, and <code>VCPU</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchContainerOverrides) -> dict:
    out: dict = {}
    if "command" in value:
        import aws_sdk_pipes.types.string_list

        out["Command"] = aws_sdk_pipes.types.string_list.serialize_json(
            value["command"]
        )
    if "environment" in value:
        import aws_sdk_pipes.types.batch_environment_variable_list

        out["Environment"] = (
            aws_sdk_pipes.types.batch_environment_variable_list.serialize_json(
                value["environment"]
            )
        )
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "resource_requirements" in value:
        import aws_sdk_pipes.types.batch_resource_requirements_list

        out["ResourceRequirements"] = (
            aws_sdk_pipes.types.batch_resource_requirements_list.serialize_json(
                value["resource_requirements"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchContainerOverrides:
    out: BatchContainerOverrides = {}  # type: ignore[typeddict-item]
    if "Command" in data:
        import aws_sdk_pipes.types.string_list

        out["command"] = aws_sdk_pipes.types.string_list.deserialize_json(
            data["Command"]
        )
    if "Environment" in data:
        import aws_sdk_pipes.types.batch_environment_variable_list

        out["environment"] = (
            aws_sdk_pipes.types.batch_environment_variable_list.deserialize_json(
                data["Environment"]
            )
        )
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "ResourceRequirements" in data:
        import aws_sdk_pipes.types.batch_resource_requirements_list

        out["resource_requirements"] = (
            aws_sdk_pipes.types.batch_resource_requirements_list.deserialize_json(
                data["ResourceRequirements"]
            )
        )
    return out
