"""Generated from Smithy shape ``com.amazonaws.finspacedata#ResetUserPasswordRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.client_token
    import aws_sdk_finspace_data.types.user_id


class ResetUserPasswordRequest(TypedDict):
    user_id: "aws_sdk_finspace_data.types.user_id.UserId"
    """<p>The unique identifier of the user that a temporary password is requested for.</p>"""
    client_token: NotRequired["aws_sdk_finspace_data.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetUserPasswordRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ResetUserPasswordRequest:
    out: ResetUserPasswordRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
