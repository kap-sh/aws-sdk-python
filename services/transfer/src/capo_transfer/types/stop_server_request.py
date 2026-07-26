"""Generated from Smithy shape ``com.amazonaws.transfer#StopServerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.server_id


class StopServerRequest(TypedDict, closed=True):
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a server that you stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopServerRequest) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopServerRequest:
    out: StopServerRequest = {}  # type: ignore[typeddict-item]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("StopServerRequest.server_id required")
    return out
