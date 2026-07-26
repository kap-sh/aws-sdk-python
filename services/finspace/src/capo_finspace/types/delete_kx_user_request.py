"""Generated from Smithy shape ``com.amazonaws.finspace#DeleteKxUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.client_token
    import capo_finspace.types.id_type
    import capo_finspace.types.kx_user_name_string


class DeleteKxUserRequest(TypedDict, closed=True):
    user_name: "capo_finspace.types.kx_user_name_string.KxUserNameString"
    """<p>A unique identifier for the user that you want to delete.</p>"""
    environment_id: "capo_finspace.types.id_type.IdType"
    """<p>A unique identifier for the kdb environment.</p>"""
    client_token: NotRequired["capo_finspace.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKxUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteKxUserRequest:
    out: DeleteKxUserRequest = {}  # type: ignore[typeddict-item]
    return out
