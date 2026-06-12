"""Generated from Smithy shape ``com.amazonaws.codecatalyst#GetUserDetailsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.email_address


class GetUserDetailsResponse(TypedDict):
    user_id: NotRequired["str"]
    """<p>The system-generated unique ID of the user.</p>"""
    user_name: NotRequired["str"]
    """<p>The name of the user as displayed in Amazon CodeCatalyst.</p>"""
    display_name: NotRequired["str"]
    """<p>The friendly name displayed for the user in Amazon CodeCatalyst.</p>"""
    primary_email: NotRequired["aws_sdk_codecatalyst.types.email_address.EmailAddress"]
    """<p>The email address provided by the user when they signed up.</p>"""
    version: NotRequired["str"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserDetailsResponse) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "user_name" in value:
        out["userName"] = value["user_name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "primary_email" in value:
        import aws_sdk_codecatalyst.types.email_address

        out["primaryEmail"] = aws_sdk_codecatalyst.types.email_address.serialize_json(
            value["primary_email"]
        )
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> GetUserDetailsResponse:
    out: GetUserDetailsResponse = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    if "userName" in data:
        out["user_name"] = data["userName"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "primaryEmail" in data:
        import aws_sdk_codecatalyst.types.email_address

        out["primary_email"] = (
            aws_sdk_codecatalyst.types.email_address.deserialize_json(
                data["primaryEmail"]
            )
        )
    if "version" in data:
        out["version"] = data["version"]
    return out
