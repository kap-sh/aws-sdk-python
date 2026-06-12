"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeApplicationAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.application_resource_association_list
    import aws_sdk_workspaces.types.pagination_token


class DescribeApplicationAssociationsResult(TypedDict):
    associations: NotRequired[
        "aws_sdk_workspaces.types.application_resource_association_list.ApplicationResourceAssociationList"
    ]
    """<p>List of associations and information about them.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationAssociationsResult) -> dict:
    out: dict = {}
    if "associations" in value:
        import aws_sdk_workspaces.types.application_resource_association_list

        out["Associations"] = (
            aws_sdk_workspaces.types.application_resource_association_list.serialize_aws_json_1_1(
                value["associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationAssociationsResult:
    out: DescribeApplicationAssociationsResult = {}  # type: ignore[typeddict-item]
    if "Associations" in data:
        import aws_sdk_workspaces.types.application_resource_association_list

        out["associations"] = (
            aws_sdk_workspaces.types.application_resource_association_list.deserialize_aws_json_1_1(
                data["Associations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
