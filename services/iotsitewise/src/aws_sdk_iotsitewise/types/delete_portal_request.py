"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeletePortalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.id


class DeletePortalRequest(TypedDict, closed=True):
    portal_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the portal to delete.</p>"""
    client_token: NotRequired["aws_sdk_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePortalRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePortalRequest:
    out: DeletePortalRequest = {}  # type: ignore[typeddict-item]
    return out
