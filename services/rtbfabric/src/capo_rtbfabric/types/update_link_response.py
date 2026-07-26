"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UpdateLinkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.link_id
    import capo_rtbfabric.types.link_status


class UpdateLinkResponse(TypedDict, closed=True):
    link_id: "capo_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    status: "capo_rtbfabric.types.link_status.LinkStatus"
    """<p>The status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLinkResponse) -> dict:
    out: dict = {}
    out["linkId"] = value["link_id"]
    import capo_rtbfabric.types.link_status

    out["status"] = capo_rtbfabric.types.link_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> UpdateLinkResponse:
    out: UpdateLinkResponse = {}  # type: ignore[typeddict-item]
    if "linkId" in data:
        out["link_id"] = data["linkId"]
    else:
        raise DeserializationError("UpdateLinkResponse.link_id required")
    if "status" in data:
        import capo_rtbfabric.types.link_status

        out["status"] = capo_rtbfabric.types.link_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateLinkResponse.status required")
    return out
