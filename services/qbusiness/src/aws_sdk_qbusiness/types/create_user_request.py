"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateUserRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_qbusiness.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.client_token
    import aws_sdk_qbusiness.types.string
    import aws_sdk_qbusiness.types.user_aliases

class CreateUserRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application for which the user mapping will be created.</p>"""
    user_id: "aws_sdk_qbusiness.types.string.String"
    """<p>The user emails attached to a user mapping.</p>"""
    user_aliases: NotRequired["aws_sdk_qbusiness.types.user_aliases.UserAliases"]
    """<p>The list of user aliases in the mapping.</p>"""
    client_token: NotRequired["aws_sdk_qbusiness.types.client_token.ClientToken"]
    """<p>A token that you provide to identify the request to create your Amazon Q Business user mapping.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateUserRequest) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    if "user_aliases" in value:
        import aws_sdk_qbusiness.types.user_aliases
        out["userAliases"] = aws_sdk_qbusiness.types.user_aliases.serialize_json(value["user_aliases"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateUserRequest:
    out: CreateUserRequest = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("CreateUserRequest.user_id required")
    if "userAliases" in data:
        import aws_sdk_qbusiness.types.user_aliases
        out["user_aliases"] = aws_sdk_qbusiness.types.user_aliases.deserialize_json(data["userAliases"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out