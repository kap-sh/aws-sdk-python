"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.id_type
    import aws_sdk_finspace.types.kx_user_name_string


class GetKxUserRequest(TypedDict, closed=True):
    user_name: "aws_sdk_finspace.types.kx_user_name_string.KxUserNameString"
    """<p>A unique identifier for the user.</p>"""
    environment_id: "aws_sdk_finspace.types.id_type.IdType"
    """<p>A unique identifier for the kdb environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetKxUserRequest:
    out: GetKxUserRequest = {}  # type: ignore[typeddict-item]
    return out
