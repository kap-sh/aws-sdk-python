"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeImageAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.image_resource_association_list


class DescribeImageAssociationsResult(TypedDict, closed=True):
    associations: NotRequired[
        "aws_sdk_workspaces.types.image_resource_association_list.ImageResourceAssociationList"
    ]
    """<p>List of information about the specified associations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImageAssociationsResult) -> dict:
    out: dict = {}
    if "associations" in value:
        import aws_sdk_workspaces.types.image_resource_association_list

        out["Associations"] = (
            aws_sdk_workspaces.types.image_resource_association_list.serialize_aws_json_1_1(
                value["associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImageAssociationsResult:
    out: DescribeImageAssociationsResult = {}  # type: ignore[typeddict-item]
    if "Associations" in data:
        import aws_sdk_workspaces.types.image_resource_association_list

        out["associations"] = (
            aws_sdk_workspaces.types.image_resource_association_list.deserialize_aws_json_1_1(
                data["Associations"]
            )
        )
    return out
