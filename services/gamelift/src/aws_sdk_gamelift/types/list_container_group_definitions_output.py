"""Generated from Smithy shape ``com.amazonaws.gamelift#ListContainerGroupDefinitionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_group_definition_list
    import aws_sdk_gamelift.types.non_zero_and_max_string


class ListContainerGroupDefinitionsOutput(TypedDict, closed=True):
    container_group_definitions: NotRequired[
        "aws_sdk_gamelift.types.container_group_definition_list.ContainerGroupDefinitionList"
    ]
    """<p>A result set of container group definitions that match the request.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListContainerGroupDefinitionsOutput) -> dict:
    out: dict = {}
    if "container_group_definitions" in value:
        import aws_sdk_gamelift.types.container_group_definition_list

        out["ContainerGroupDefinitions"] = (
            aws_sdk_gamelift.types.container_group_definition_list.serialize_aws_json_1_1(
                value["container_group_definitions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListContainerGroupDefinitionsOutput:
    out: ListContainerGroupDefinitionsOutput = {}  # type: ignore[typeddict-item]
    if "ContainerGroupDefinitions" in data:
        import aws_sdk_gamelift.types.container_group_definition_list

        out["container_group_definitions"] = (
            aws_sdk_gamelift.types.container_group_definition_list.deserialize_aws_json_1_1(
                data["ContainerGroupDefinitions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
