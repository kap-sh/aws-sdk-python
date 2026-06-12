"""Generated from Smithy shape ``com.amazonaws.transfer#StartFileTransferResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.transfer_id


class StartFileTransferResponse(TypedDict):
    transfer_id: "aws_sdk_transfer.types.transfer_id.TransferId"
    """<p>Returns the unique identifier for the file transfer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartFileTransferResponse) -> dict:
    out: dict = {}
    out["TransferId"] = value["transfer_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartFileTransferResponse:
    out: StartFileTransferResponse = {}  # type: ignore[typeddict-item]
    if "TransferId" in data:
        out["transfer_id"] = data["TransferId"]
    else:
        raise DeserializationError("StartFileTransferResponse.transfer_id required")
    return out
