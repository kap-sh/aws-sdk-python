"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CreateAccessPreviewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.access_preview_id


class CreateAccessPreviewResponse(TypedDict, closed=True):
    id: "aws_sdk_accessanalyzer.types.access_preview_id.AccessPreviewId"
    """<p>The unique ID for the access preview.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessPreviewResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateAccessPreviewResponse:
    out: CreateAccessPreviewResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateAccessPreviewResponse.id required")
    return out
