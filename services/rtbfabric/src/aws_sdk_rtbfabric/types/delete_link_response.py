"""Generated from Smithy shape ``com.amazonaws.rtbfabric#DeleteLinkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.link_id
    import aws_sdk_rtbfabric.types.link_status


class DeleteLinkResponse(TypedDict, closed=True):
    link_id: "aws_sdk_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    status: "aws_sdk_rtbfabric.types.link_status.LinkStatus"
    """<p>The status of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLinkResponse) -> dict:
    out: dict = {}
    out["linkId"] = value["link_id"]
    import aws_sdk_rtbfabric.types.link_status

    out["status"] = aws_sdk_rtbfabric.types.link_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DeleteLinkResponse:
    out: DeleteLinkResponse = {}  # type: ignore[typeddict-item]
    if "linkId" in data:
        out["link_id"] = data["linkId"]
    else:
        raise DeserializationError("DeleteLinkResponse.link_id required")
    if "status" in data:
        import aws_sdk_rtbfabric.types.link_status

        out["status"] = aws_sdk_rtbfabric.types.link_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DeleteLinkResponse.status required")
    return out
