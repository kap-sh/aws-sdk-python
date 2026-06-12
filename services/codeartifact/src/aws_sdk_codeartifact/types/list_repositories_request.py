"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListRepositoriesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.list_repositories_max_results
    import aws_sdk_codeartifact.types.pagination_token
    import aws_sdk_codeartifact.types.repository_name


class ListRepositoriesRequest(TypedDict):
    repository_prefix: NotRequired[
        "aws_sdk_codeartifact.types.repository_name.RepositoryName"
    ]
    """<p> A prefix used to filter returned repositories. Only repositories with names that start with <code>repositoryPrefix</code> are returned.</p>"""
    max_results: NotRequired[
        "aws_sdk_codeartifact.types.list_repositories_max_results.ListRepositoriesMaxResults"
    ]
    """<p> The maximum number of results to return per page. </p>"""
    next_token: NotRequired[
        "aws_sdk_codeartifact.types.pagination_token.PaginationToken"
    ]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRepositoriesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRepositoriesRequest:
    out: ListRepositoriesRequest = {}  # type: ignore[typeddict-item]
    return out
