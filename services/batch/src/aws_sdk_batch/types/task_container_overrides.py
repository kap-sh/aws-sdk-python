"""Generated from Smithy shape ``com.amazonaws.batch#TaskContainerOverrides``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.environment_variables
    import aws_sdk_batch.types.resource_requirements
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.string_list


class TaskContainerOverrides(TypedDict):
    command: NotRequired["aws_sdk_batch.types.string_list.StringList"]
    """<p>The command to send to the container that overrides the default command from the Docker image or the job definition.</p> <note> <p>This parameter can't contain an empty string.</p> </note>"""
    environment: NotRequired[
        "aws_sdk_batch.types.environment_variables.EnvironmentVariables"
    ]
    """<p>The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the job definition.</p> <note> <p>Environment variables cannot start with <code>AWS_BATCH</code>. This naming convention is reserved for variables that Batch sets.</p> </note>"""
    name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>A pointer to the container that you want to override. The container's name provides a unique identifier for the container being used.</p>"""
    resource_requirements: NotRequired[
        "aws_sdk_batch.types.resource_requirements.ResourceRequirements"
    ]
    """<p>The type and amount of resources to assign to a container. This overrides the settings in the job definition. The supported resources include <code>GPU</code>, <code>MEMORY</code>, and <code>VCPU</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskContainerOverrides) -> dict:
    out: dict = {}
    if "command" in value:
        import aws_sdk_batch.types.string_list

        out["command"] = aws_sdk_batch.types.string_list.serialize_json(
            value["command"]
        )
    if "environment" in value:
        import aws_sdk_batch.types.environment_variables

        out["environment"] = aws_sdk_batch.types.environment_variables.serialize_json(
            value["environment"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "resource_requirements" in value:
        import aws_sdk_batch.types.resource_requirements

        out["resourceRequirements"] = (
            aws_sdk_batch.types.resource_requirements.serialize_json(
                value["resource_requirements"]
            )
        )
    return out


def deserialize_json(data: dict) -> TaskContainerOverrides:
    out: TaskContainerOverrides = {}  # type: ignore[typeddict-item]
    if "command" in data:
        import aws_sdk_batch.types.string_list

        out["command"] = aws_sdk_batch.types.string_list.deserialize_json(
            data["command"]
        )
    if "environment" in data:
        import aws_sdk_batch.types.environment_variables

        out["environment"] = aws_sdk_batch.types.environment_variables.deserialize_json(
            data["environment"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "resourceRequirements" in data:
        import aws_sdk_batch.types.resource_requirements

        out["resource_requirements"] = (
            aws_sdk_batch.types.resource_requirements.deserialize_json(
                data["resourceRequirements"]
            )
        )
    return out
