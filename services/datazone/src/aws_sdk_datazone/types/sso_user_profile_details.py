"""Generated from Smithy shape ``com.amazonaws.datazone#SsoUserProfileDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.first_name
    import aws_sdk_datazone.types.last_name
    import aws_sdk_datazone.types.user_profile_name


class SsoUserProfileDetails(TypedDict, closed=True):
    username: NotRequired["aws_sdk_datazone.types.user_profile_name.UserProfileName"]
    """<p>The username as part of the SSO user profile detail. </p>"""
    first_name: NotRequired["aws_sdk_datazone.types.first_name.FirstName"]
    """<p>The first name as part of the SSO user profile detail.</p>"""
    last_name: NotRequired["aws_sdk_datazone.types.last_name.LastName"]
    """<p>The last name as part of the SSO user profile detail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SsoUserProfileDetails) -> dict:
    out: dict = {}
    if "username" in value:
        out["username"] = value["username"]
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    return out


def deserialize_json(data: dict) -> SsoUserProfileDetails:
    out: SsoUserProfileDetails = {}  # type: ignore[typeddict-item]
    if "username" in data:
        out["username"] = data["username"]
    if "firstName" in data:
        out["first_name"] = data["firstName"]
    if "lastName" in data:
        out["last_name"] = data["lastName"]
    return out
