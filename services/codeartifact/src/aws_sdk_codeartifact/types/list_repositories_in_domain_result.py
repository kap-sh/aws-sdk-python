"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListRepositoriesInDomainResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.pagination_token
    import aws_sdk_codeartifact.types.repository_summary_list


class ListRepositoriesInDomainResult(TypedDict, closed=True):
    repositories: NotRequired[
        "aws_sdk_codeartifact.types.repository_summary_list.RepositorySummaryList"
    ]
    """<p> The returned list of repositories. </p>"""
    next_token: NotRequired[
        "aws_sdk_codeartifact.types.pagination_token.PaginationToken"
    ]
    """<p> If there are additional results, this is the token for the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRepositoriesInDomainResult) -> dict:
    out: dict = {}
    if "repositories" in value:
        import aws_sdk_codeartifact.types.repository_summary_list

        out["repositories"] = (
            aws_sdk_codeartifact.types.repository_summary_list.serialize_json(
                value["repositories"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRepositoriesInDomainResult:
    out: ListRepositoriesInDomainResult = {}  # type: ignore[typeddict-item]
    if "repositories" in data:
        import aws_sdk_codeartifact.types.repository_summary_list

        out["repositories"] = (
            aws_sdk_codeartifact.types.repository_summary_list.deserialize_json(
                data["repositories"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
