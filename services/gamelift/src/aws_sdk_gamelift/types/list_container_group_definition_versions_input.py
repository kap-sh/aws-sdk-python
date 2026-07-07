"""Generated from Smithy shape ``com.amazonaws.gamelift#ListContainerGroupDefinitionVersionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_group_definition_name_or_arn
    import aws_sdk_gamelift.types.list_container_group_definition_versions_limit
    import aws_sdk_gamelift.types.non_zero_and_max_string


class ListContainerGroupDefinitionVersionsInput(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
    ]
    """<p>The unique identifier for the container group definition to retrieve properties for. You can use either the <code>Name</code> or <code>ARN</code> value.</p>"""
    limit: NotRequired[
        "aws_sdk_gamelift.types.list_container_group_definition_versions_limit.ListContainerGroupDefinitionVersionsLimit"
    ]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListContainerGroupDefinitionVersionsInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListContainerGroupDefinitionVersionsInput:
    out: ListContainerGroupDefinitionVersionsInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
