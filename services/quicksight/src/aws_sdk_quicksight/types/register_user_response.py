"""Generated from Smithy shape ``com.amazonaws.quicksight#RegisterUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.user


class RegisterUserResponse(TypedDict, closed=True):
    user: NotRequired["aws_sdk_quicksight.types.user.User"]
    """<p>The user's user name.</p>"""
    user_invitation_url: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The URL the user visits to complete registration and provide a password. This is returned only for users with an identity type of <code>QUICKSIGHT</code>.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import aws_sdk_quicksight.types.user

        out["User"] = aws_sdk_quicksight.types.user.serialize_json(value["user"])
    if "user_invitation_url" in value:
        out["UserInvitationUrl"] = value["user_invitation_url"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> RegisterUserResponse:
    out: RegisterUserResponse = {}  # type: ignore[typeddict-item]
    if "User" in data:
        import aws_sdk_quicksight.types.user

        out["user"] = aws_sdk_quicksight.types.user.deserialize_json(data["User"])
    if "UserInvitationUrl" in data:
        out["user_invitation_url"] = data["UserInvitationUrl"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
