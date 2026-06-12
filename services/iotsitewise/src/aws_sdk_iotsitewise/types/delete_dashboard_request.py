"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteDashboardRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.id


class DeleteDashboardRequest(TypedDict):
    dashboard_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the dashboard to delete.</p>"""
    client_token: NotRequired["aws_sdk_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDashboardRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDashboardRequest:
    out: DeleteDashboardRequest = {}  # type: ignore[typeddict-item]
    return out
