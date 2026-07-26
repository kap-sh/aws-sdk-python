"""Generated from Smithy shape ``com.amazonaws.transfer#StartRemoteDeleteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.connector_id
    import capo_transfer.types.file_path


class StartRemoteDeleteRequest(TypedDict, closed=True):
    connector_id: "capo_transfer.types.connector_id.ConnectorId"
    """<p>The unique identifier for the connector.</p>"""
    delete_path: "capo_transfer.types.file_path.FilePath"
    """<p>The absolute path of the file or directory to delete. You can only specify one path per call to this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRemoteDeleteRequest) -> dict:
    out: dict = {}
    out["ConnectorId"] = value["connector_id"]
    out["DeletePath"] = value["delete_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartRemoteDeleteRequest:
    out: StartRemoteDeleteRequest = {}  # type: ignore[typeddict-item]
    if "ConnectorId" in data:
        out["connector_id"] = data["ConnectorId"]
    else:
        raise DeserializationError("StartRemoteDeleteRequest.connector_id required")
    if "DeletePath" in data:
        out["delete_path"] = data["DeletePath"]
    else:
        raise DeserializationError("StartRemoteDeleteRequest.delete_path required")
    return out
