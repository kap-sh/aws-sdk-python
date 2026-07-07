"""Generated from Smithy shape ``com.amazonaws.omics#DeleteShareResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.share_status


class DeleteShareResponse(TypedDict, closed=True):
    status: NotRequired["aws_sdk_omics.types.share_status.ShareStatus"]
    """<p>The status of the share being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteShareResponse) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> DeleteShareResponse:
    out: DeleteShareResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    return out
