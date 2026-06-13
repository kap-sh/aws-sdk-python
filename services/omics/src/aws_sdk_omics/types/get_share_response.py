"""Generated from Smithy shape ``com.amazonaws.omics#GetShareResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.share_details


class GetShareResponse(TypedDict):
    share: NotRequired["aws_sdk_omics.types.share_details.ShareDetails"]
    """<p>A resource share details object. The object includes the status, the resourceArn, and ownerId.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetShareResponse) -> dict:
    out: dict = {}
    if "share" in value:
        import aws_sdk_omics.types.share_details

        out["share"] = aws_sdk_omics.types.share_details.serialize_json(value["share"])
    return out


def deserialize_json(data: dict) -> GetShareResponse:
    out: GetShareResponse = {}  # type: ignore[typeddict-item]
    if "share" in data:
        import aws_sdk_omics.types.share_details

        out["share"] = aws_sdk_omics.types.share_details.deserialize_json(data["share"])
    return out
