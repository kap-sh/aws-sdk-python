"""Generated from Smithy shape ``com.amazonaws.codeartifact#UpstreamRepositoryInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.repository_name


class UpstreamRepositoryInfo(TypedDict, closed=True):
    repository_name: NotRequired[
        "capo_codeartifact.types.repository_name.RepositoryName"
    ]
    """<p> The name of an upstream repository. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpstreamRepositoryInfo) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    return out


def deserialize_json(data: dict) -> UpstreamRepositoryInfo:
    out: UpstreamRepositoryInfo = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    return out
