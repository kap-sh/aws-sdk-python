"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#CreateDirectoryRegistrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.client_token
    import capo_pca_connector_ad.types.directory_id
    import capo_pca_connector_ad.types.tags


class CreateDirectoryRegistrationRequest(TypedDict, closed=True):
    directory_id: "capo_pca_connector_ad.types.directory_id.DirectoryId"
    """<p> The identifier of the Active Directory.</p>"""
    client_token: NotRequired["capo_pca_connector_ad.types.client_token.ClientToken"]
    """<p>Idempotency token.</p>"""
    tags: NotRequired["capo_pca_connector_ad.types.tags.Tags"]
    """<p>Metadata assigned to a directory registration consisting of a key-value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDirectoryRegistrationRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_pca_connector_ad.types.tags

        out["Tags"] = capo_pca_connector_ad.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDirectoryRegistrationRequest:
    out: CreateDirectoryRegistrationRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError(
            "CreateDirectoryRegistrationRequest.directory_id required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Tags" in data:
        import capo_pca_connector_ad.types.tags

        out["tags"] = capo_pca_connector_ad.types.tags.deserialize_json(data["Tags"])
    return out
