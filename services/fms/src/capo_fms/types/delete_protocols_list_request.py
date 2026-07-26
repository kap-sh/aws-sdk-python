"""Generated from Smithy shape ``com.amazonaws.fms#DeleteProtocolsListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.list_id


class DeleteProtocolsListRequest(TypedDict, closed=True):
    list_id: "capo_fms.types.list_id.ListId"
    """<p>The ID of the protocols list that you want to delete. You can retrieve this ID from <code>PutProtocolsList</code>, <code>ListProtocolsLists</code>, and <code>GetProtocolsLost</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProtocolsListRequest) -> dict:
    out: dict = {}
    out["ListId"] = value["list_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProtocolsListRequest:
    out: DeleteProtocolsListRequest = {}  # type: ignore[typeddict-item]
    if "ListId" in data:
        out["list_id"] = data["ListId"]
    else:
        raise DeserializationError("DeleteProtocolsListRequest.list_id required")
    return out
