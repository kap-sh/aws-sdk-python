"""Generated from Smithy shape ``com.amazonaws.gamelift#ListContainerGroupDefinitionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_group_type
    import aws_sdk_gamelift.types.list_container_group_definitions_limit
    import aws_sdk_gamelift.types.non_zero_and_max_string


class ListContainerGroupDefinitionsInput(TypedDict, closed=True):
    container_group_type: NotRequired[
        "aws_sdk_gamelift.types.container_group_type.ContainerGroupType"
    ]
    """<p>The type of container group to retrieve. Container group type determines how Amazon GameLift Servers deploys the container group on each fleet instance.</p>"""
    limit: NotRequired[
        "aws_sdk_gamelift.types.list_container_group_definitions_limit.ListContainerGroupDefinitionsLimit"
    ]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListContainerGroupDefinitionsInput) -> dict:
    out: dict = {}
    if "container_group_type" in value:
        import aws_sdk_gamelift.types.container_group_type

        out["ContainerGroupType"] = (
            aws_sdk_gamelift.types.container_group_type.serialize_aws_json_1_1(
                value["container_group_type"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListContainerGroupDefinitionsInput:
    out: ListContainerGroupDefinitionsInput = {}  # type: ignore[typeddict-item]
    if "ContainerGroupType" in data:
        import aws_sdk_gamelift.types.container_group_type

        out["container_group_type"] = (
            aws_sdk_gamelift.types.container_group_type.deserialize_aws_json_1_1(
                data["ContainerGroupType"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
