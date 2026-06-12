"""Generated from Smithy shape ``com.amazonaws.codeartifact#GetRepositoryEndpointResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.string


class GetRepositoryEndpointResult(TypedDict):
    repository_endpoint: NotRequired["aws_sdk_codeartifact.types.string.String"]
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
