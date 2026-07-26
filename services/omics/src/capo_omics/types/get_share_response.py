"""Generated from Smithy shape ``com.amazonaws.omics#GetShareResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.share_details


class GetShareResponse(TypedDict, closed=True):
    share: NotRequired["capo_omics.types.share_details.ShareDetails"]
    """<p>A resource share details object. The object includes the status, the resourceArn, and ownerId.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetShareResponse) -> dict:
    out: dict = {}
    if "share" in value:
        import capo_omics.types.share_details

        out["share"] = capo_omics.types.share_details.serialize_json(value["share"])
    return out


def deserialize_json(data: dict) -> GetShareResponse:
    out: GetShareResponse = {}  # type: ignore[typeddict-item]
    if "share" in data:
        import capo_omics.types.share_details

        out["share"] = capo_omics.types.share_details.deserialize_json(data["share"])
    return out
