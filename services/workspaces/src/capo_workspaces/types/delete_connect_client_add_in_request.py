"""Generated from Smithy shape ``com.amazonaws.workspaces#DeleteConnectClientAddInRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.amazon_uuid
    import capo_workspaces.types.directory_id


class DeleteConnectClientAddInRequest(TypedDict, closed=True):
    add_in_id: "capo_workspaces.types.amazon_uuid.AmazonUuid"
    """<p>The identifier of the client add-in to delete.</p>"""
    resource_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The directory identifier for which the client add-in is configured.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConnectClientAddInRequest) -> dict:
    out: dict = {}
    out["AddInId"] = value["add_in_id"]
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConnectClientAddInRequest:
    out: DeleteConnectClientAddInRequest = {}  # type: ignore[typeddict-item]
    if "AddInId" in data:
        out["add_in_id"] = data["AddInId"]
    else:
        raise DeserializationError("DeleteConnectClientAddInRequest.add_in_id required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "DeleteConnectClientAddInRequest.resource_id required"
        )
    return out
