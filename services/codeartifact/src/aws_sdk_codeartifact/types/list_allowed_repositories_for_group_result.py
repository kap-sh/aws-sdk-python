"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListAllowedRepositoriesForGroupResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.pagination_token
    import aws_sdk_codeartifact.types.repository_name_list


class ListAllowedRepositoriesForGroupResult(TypedDict):
    allowed_repositories: NotRequired[
        "aws_sdk_codeartifact.types.repository_name_list.RepositoryNameList"
    ]
    """<p>The list of allowed repositories for the package group and origin configuration restriction type.</p>"""
    next_token: NotRequired[
        "aws_sdk_codeartifact.types.pagination_token.PaginationToken"
    ]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAllowedRepositoriesForGroupResult) -> dict:
    out: dict = {}
    if "allowed_repositories" in value:
        import aws_sdk_codeartifact.types.repository_name_list

        out["allowedRepositories"] = (
            aws_sdk_codeartifact.types.repository_name_list.serialize_json(
                value["allowed_repositories"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAllowedRepositoriesForGroupResult:
    out: ListAllowedRepositoriesForGroupResult = {}  # type: ignore[typeddict-item]
    if "allowedRepositories" in data:
        import aws_sdk_codeartifact.types.repository_name_list

        out["allowed_repositories"] = (
            aws_sdk_codeartifact.types.repository_name_list.deserialize_json(
                data["allowedRepositories"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
