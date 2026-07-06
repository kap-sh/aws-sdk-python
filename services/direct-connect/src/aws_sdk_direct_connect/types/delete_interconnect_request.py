"""Generated from Smithy shape ``com.amazonaws.directconnect#DeleteInterconnectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.interconnect_id


class DeleteInterconnectRequest(TypedDict, closed=True):
    interconnect_id: "aws_sdk_direct_connect.types.interconnect_id.InterconnectId"
    """<p>The ID of the interconnect.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteInterconnectRequest) -> dict:
    out: dict = {}
    out["interconnectId"] = value["interconnect_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteInterconnectRequest:
    out: DeleteInterconnectRequest = {}  # type: ignore[typeddict-item]
    if "interconnectId" in data:
        out["interconnect_id"] = data["interconnectId"]
    else:
        raise DeserializationError("DeleteInterconnectRequest.interconnect_id required")
    return out
