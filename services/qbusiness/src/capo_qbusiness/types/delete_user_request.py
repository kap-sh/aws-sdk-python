"""Generated from Smithy shape ``com.amazonaws.qbusiness#DeleteUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.string


class DeleteUserRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application from which the user is being deleted.</p>"""
    user_id: "capo_qbusiness.types.string.String"
    """<p>The user email being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteUserRequest:
    out: DeleteUserRequest = {}  # type: ignore[typeddict-item]
    return out
