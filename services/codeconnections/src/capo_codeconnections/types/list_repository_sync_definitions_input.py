"""Generated from Smithy shape ``com.amazonaws.codeconnections#ListRepositorySyncDefinitionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeconnections.types.repository_link_id
    import capo_codeconnections.types.sync_configuration_type


class ListRepositorySyncDefinitionsInput(TypedDict, closed=True):
    repository_link_id: "capo_codeconnections.types.repository_link_id.RepositoryLinkId"
    """<p>The ID of the repository link for the sync definition for which you want to retrieve information.</p>"""
    sync_type: (
        "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType"
    )
    """<p>The sync type of the repository link for the the sync definition for which you want to retrieve information.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRepositorySyncDefinitionsInput) -> dict:
    out: dict = {}
    out["RepositoryLinkId"] = value["repository_link_id"]
    import capo_codeconnections.types.sync_configuration_type

    out["SyncType"] = (
        capo_codeconnections.types.sync_configuration_type.serialize_aws_json_1_0(
            value["sync_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRepositorySyncDefinitionsInput:
    out: ListRepositorySyncDefinitionsInput = {}  # type: ignore[typeddict-item]
    if "RepositoryLinkId" in data:
        out["repository_link_id"] = data["RepositoryLinkId"]
    else:
        raise DeserializationError(
            "ListRepositorySyncDefinitionsInput.repository_link_id required"
        )
    if "SyncType" in data:
        import capo_codeconnections.types.sync_configuration_type

        out["sync_type"] = (
            capo_codeconnections.types.sync_configuration_type.deserialize_aws_json_1_0(
                data["SyncType"]
            )
        )
    else:
        raise DeserializationError(
            "ListRepositorySyncDefinitionsInput.sync_type required"
        )
    return out
