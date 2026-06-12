"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListSubPackageGroupsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_group_summary_list
    import aws_sdk_codeartifact.types.pagination_token


class ListSubPackageGroupsResult(TypedDict):
    package_groups: NotRequired[
        "aws_sdk_codeartifact.types.package_group_summary_list.PackageGroupSummaryList"
    ]
    """<p> A list of sub package groups for the requested package group. </p>"""
    next_token: NotRequired[
        "aws_sdk_codeartifact.types.pagination_token.PaginationToken"
    ]
    """<p> If there are additional results, this is the token for the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubPackageGroupsResult) -> dict:
    out: dict = {}
    if "package_groups" in value:
        import aws_sdk_codeartifact.types.package_group_summary_list

        out["packageGroups"] = (
            aws_sdk_codeartifact.types.package_group_summary_list.serialize_json(
                value["package_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSubPackageGroupsResult:
    out: ListSubPackageGroupsResult = {}  # type: ignore[typeddict-item]
    if "packageGroups" in data:
        import aws_sdk_codeartifact.types.package_group_summary_list

        out["package_groups"] = (
            aws_sdk_codeartifact.types.package_group_summary_list.deserialize_json(
                data["packageGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
