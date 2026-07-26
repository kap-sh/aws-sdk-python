"""Generated from Smithy shape ``com.amazonaws.omics#AcceptShareResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.share_status


class AcceptShareResponse(TypedDict, closed=True):
    status: NotRequired["capo_omics.types.share_status.ShareStatus"]
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
