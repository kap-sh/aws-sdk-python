"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.user


class UpdateUserResponse(TypedDict, closed=True):
    user: NotRequired["capo_quicksight.types.user.User"]
    """<p>The Amazon Quick Sight user.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import capo_quicksight.types.user

        out["User"] = capo_quicksight.types.user.serialize_json(value["user"])
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateUserResponse:
    out: UpdateUserResponse = {}  # type: ignore[typeddict-item]
    if "User" in data:
        import capo_quicksight.types.user

        out["user"] = capo_quicksight.types.user.deserialize_json(data["User"])
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
