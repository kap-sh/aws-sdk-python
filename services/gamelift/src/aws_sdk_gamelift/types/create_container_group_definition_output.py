"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateContainerGroupDefinitionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_group_definition


class CreateContainerGroupDefinitionOutput(TypedDict, closed=True):
    container_group_definition: NotRequired[
        "aws_sdk_gamelift.types.container_group_definition.ContainerGroupDefinition"
    ]
    """<p>The properties of the new container group definition resource. You can use this resource to create a container fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContainerGroupDefinitionOutput) -> dict:
    out: dict = {}
    if "container_group_definition" in value:
        import aws_sdk_gamelift.types.container_group_definition

        out["ContainerGroupDefinition"] = (
            aws_sdk_gamelift.types.container_group_definition.serialize_aws_json_1_1(
                value["container_group_definition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContainerGroupDefinitionOutput:
    out: CreateContainerGroupDefinitionOutput = {}  # type: ignore[typeddict-item]
    if "ContainerGroupDefinition" in data:
        import aws_sdk_gamelift.types.container_group_definition

        out["container_group_definition"] = (
            aws_sdk_gamelift.types.container_group_definition.deserialize_aws_json_1_1(
                data["ContainerGroupDefinition"]
            )
        )
    return out
