"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeContainerGroupDefinitionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_group_definition


class DescribeContainerGroupDefinitionOutput(TypedDict):
    container_group_definition: NotRequired[
        "aws_sdk_gamelift.types.container_group_definition.ContainerGroupDefinition"
    ]
    """<p>The properties of the requested container group definition resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeContainerGroupDefinitionOutput) -> dict:
    out: dict = {}
    if "container_group_definition" in value:
        import aws_sdk_gamelift.types.container_group_definition

        out["ContainerGroupDefinition"] = (
            aws_sdk_gamelift.types.container_group_definition.serialize_aws_json_1_1(
                value["container_group_definition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeContainerGroupDefinitionOutput:
    out: DescribeContainerGroupDefinitionOutput = {}  # type: ignore[typeddict-item]
    if "ContainerGroupDefinition" in data:
        import aws_sdk_gamelift.types.container_group_definition

        out["container_group_definition"] = (
            aws_sdk_gamelift.types.container_group_definition.deserialize_aws_json_1_1(
                data["ContainerGroupDefinition"]
            )
        )
    return out
