"""Generated from Smithy shape ``com.amazonaws.finspacedata#GetUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.user_id


class GetUserRequest(TypedDict, closed=True):
    user_id: "aws_sdk_finspace_data.types.user_id.UserId"
    """<p>The unique identifier of the user to get data for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUserRequest:
    out: GetUserRequest = {}  # type: ignore[typeddict-item]
    return out
