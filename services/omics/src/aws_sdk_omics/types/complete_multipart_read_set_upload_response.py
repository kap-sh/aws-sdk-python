"""Generated from Smithy shape ``com.amazonaws.omics#CompleteMultipartReadSetUploadResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.read_set_id


class CompleteMultipartReadSetUploadResponse(TypedDict):
    read_set_id: "aws_sdk_omics.types.read_set_id.ReadSetId"
    """<p>The read set ID created for an uploaded read set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompleteMultipartReadSetUploadResponse) -> dict:
    out: dict = {}
    out["readSetId"] = value["read_set_id"]
    return out


def deserialize_json(data: dict) -> CompleteMultipartReadSetUploadResponse:
    out: CompleteMultipartReadSetUploadResponse = {}  # type: ignore[typeddict-item]
    if "readSetId" in data:
        out["read_set_id"] = data["readSetId"]
    else:
        raise DeserializationError(
            "CompleteMultipartReadSetUploadResponse.read_set_id required"
        )
    return out
