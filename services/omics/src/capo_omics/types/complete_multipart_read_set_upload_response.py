"""Generated from Smithy shape ``com.amazonaws.omics#CompleteMultipartReadSetUploadResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.read_set_id


class CompleteMultipartReadSetUploadResponse(TypedDict, closed=True):
    read_set_id: "capo_omics.types.read_set_id.ReadSetId"
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
