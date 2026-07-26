"""Generated from Smithy shape ``com.amazonaws.codeartifact#GetRepositoryEndpointResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.string


class GetRepositoryEndpointResult(TypedDict, closed=True):
    repository_endpoint: NotRequired["capo_codeartifact.types.string.String"]
    """<p> A string that specifies the URL of the returned endpoint. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRepositoryEndpointResult) -> dict:
    out: dict = {}
    if "repository_endpoint" in value:
        out["repositoryEndpoint"] = value["repository_endpoint"]
    return out


def deserialize_json(data: dict) -> GetRepositoryEndpointResult:
    out: GetRepositoryEndpointResult = {}  # type: ignore[typeddict-item]
    if "repositoryEndpoint" in data:
        out["repository_endpoint"] = data["repositoryEndpoint"]
    return out
