"""Generated from Smithy shape ``com.amazonaws.omics#AcceptShareResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_omics.types.share_status

class AcceptShareResponse(TypedDict):
    status: NotRequired["aws_sdk_omics.types.share_status.ShareStatus"]
    """<p>The status of the resource share.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AcceptShareResponse) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AcceptShareResponse:
    out: AcceptShareResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    return out