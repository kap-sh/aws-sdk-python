"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListPackageGroupsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.package_group_summary_list
    import capo_codeartifact.types.pagination_token


class ListPackageGroupsResult(TypedDict, closed=True):
    package_groups: NotRequired[
        "capo_codeartifact.types.package_group_summary_list.PackageGroupSummaryList"
    ]
    """<p> The list of package groups in the requested domain. </p>"""
    next_token: NotRequired["capo_codeartifact.types.pagination_token.PaginationToken"]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackageGroupsResult) -> dict:
    out: dict = {}
    if "package_groups" in value:
        import capo_codeartifact.types.package_group_summary_list

        out["packageGroups"] = (
            capo_codeartifact.types.package_group_summary_list.serialize_json(
                value["package_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPackageGroupsResult:
    out: ListPackageGroupsResult = {}  # type: ignore[typeddict-item]
    if "packageGroups" in data:
        import capo_codeartifact.types.package_group_summary_list

        out["package_groups"] = (
            capo_codeartifact.types.package_group_summary_list.deserialize_json(
                data["packageGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
