"""Generated from Smithy shape ``com.amazonaws.finspace#DeleteKxUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.client_token
    import aws_sdk_finspace.types.id_type
    import aws_sdk_finspace.types.kx_user_name_string


class DeleteKxUserRequest(TypedDict):
    user_name: "aws_sdk_finspace.types.kx_user_name_string.KxUserNameString"
    """<p>A unique identifier for the user that you want to delete.</p>"""
    environment_id: "aws_sdk_finspace.types.id_type.IdType"
    """<p>A unique identifier for the kdb environment.</p>"""
    client_token: NotRequired["aws_sdk_finspace.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKxUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteKxUserRequest:
    out: DeleteKxUserRequest = {}  # type: ignore[typeddict-item]
    return out
