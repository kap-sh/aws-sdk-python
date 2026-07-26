"""Generated from Smithy shape ``com.amazonaws.proton#ListRepositorySyncDefinitionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.empty_next_token
    import capo_proton.types.repository_name
    import capo_proton.types.repository_provider
    import capo_proton.types.sync_type


class ListRepositorySyncDefinitionsInput(TypedDict, closed=True):
    repository_name: "capo_proton.types.repository_name.RepositoryName"
    """<p>The repository name.</p>"""
    repository_provider: "capo_proton.types.repository_provider.RepositoryProvider"
    """<p>The repository provider.</p>"""
    sync_type: "capo_proton.types.sync_type.SyncType"
    """<p>The sync type. The only supported value is <code>TEMPLATE_SYNC</code>.</p>"""
    next_token: NotRequired["capo_proton.types.empty_next_token.EmptyNextToken"]
    """<p>A token that indicates the location of the next repository sync definition in the array of repository sync definitions, after the list of repository sync definitions previously requested.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRepositorySyncDefinitionsInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["repositoryProvider"] = value["repository_provider"]
    out["syncType"] = value["sync_type"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRepositorySyncDefinitionsInput:
    out: ListRepositorySyncDefinitionsInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "ListRepositorySyncDefinitionsInput.repository_name required"
        )
    if "repositoryProvider" in data:
        out["repository_provider"] = data["repositoryProvider"]
    else:
        raise DeserializationError(
            "ListRepositorySyncDefinitionsInput.repository_provider required"
        )
    if "syncType" in data:
        out["sync_type"] = data["syncType"]
    else:
        raise DeserializationError(
            "ListRepositorySyncDefinitionsInput.sync_type required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
