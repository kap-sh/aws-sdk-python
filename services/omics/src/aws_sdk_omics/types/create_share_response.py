"""Generated from Smithy shape ``com.amazonaws.omics#CreateShareResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.share_name
    import aws_sdk_omics.types.share_status


class CreateShareResponse(TypedDict, closed=True):
    share_id: NotRequired["str"]
    """<p>The ID that HealthOmics generates for the share.</p>"""
    status: NotRequired["aws_sdk_omics.types.share_status.ShareStatus"]
    """<p>The status of the share.</p>"""
    share_name: NotRequired["aws_sdk_omics.types.share_name.ShareName"]
    """<p>The name of the share.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateShareResponse) -> dict:
    out: dict = {}
    if "share_id" in value:
        out["shareId"] = value["share_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "share_name" in value:
        out["shareName"] = value["share_name"]
    return out


def deserialize_json(data: dict) -> CreateShareResponse:
    out: CreateShareResponse = {}  # type: ignore[typeddict-item]
    if "shareId" in data:
        out["share_id"] = data["shareId"]
    if "status" in data:
        out["status"] = data["status"]
    if "shareName" in data:
        out["share_name"] = data["shareName"]
    return out
