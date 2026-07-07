"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeContainerGroupDefinitionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_group_definition_name_or_arn
    import aws_sdk_gamelift.types.positive_integer


class DescribeContainerGroupDefinitionInput(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
    ]
    """<p>The unique identifier for the container group definition to retrieve properties for. You can use either the <code>Name</code> or <code>ARN</code> value.</p>"""
    version_number: NotRequired[
        "aws_sdk_gamelift.types.positive_integer.PositiveInteger"
    ]
    """<p>The specific version to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeContainerGroupDefinitionInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeContainerGroupDefinitionInput:
    out: DescribeContainerGroupDefinitionInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    return out
