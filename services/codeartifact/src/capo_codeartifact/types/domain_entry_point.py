"""Generated from Smithy shape ``com.amazonaws.codeartifact#DomainEntryPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.external_connection_name
    import capo_codeartifact.types.repository_name


class DomainEntryPoint(TypedDict, closed=True):
    repository_name: NotRequired[
        "capo_codeartifact.types.repository_name.RepositoryName"
    ]
    """<p>The name of the repository that a package was originally published to.</p>"""
    external_connection_name: NotRequired[
        "capo_codeartifact.types.external_connection_name.ExternalConnectionName"
    ]
    """<p>The name of the external connection that a package was ingested from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainEntryPoint) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "external_connection_name" in value:
        out["externalConnectionName"] = value["external_connection_name"]
    return out


def deserialize_json(data: dict) -> DomainEntryPoint:
    out: DomainEntryPoint = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "externalConnectionName" in data:
        out["external_connection_name"] = data["externalConnectionName"]
    return out
