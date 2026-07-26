"""Generated from Smithy shape ``com.amazonaws.guardduty#LoginAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.integer
    import capo_guardduty.types.string


class LoginAttribute(TypedDict, closed=True):
    user: NotRequired["capo_guardduty.types.string.String"]
    """<p>Indicates the user name which attempted to log in.</p>"""
    application: NotRequired["capo_guardduty.types.string.String"]
    """<p>Indicates the application name used to attempt log in.</p>"""
    failed_login_attempts: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>Represents the sum of failed (unsuccessful) login attempts made to establish a connection to the database instance.</p>"""
    successful_login_attempts: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>Represents the sum of successful connections (a correct combination of login attributes) made to the database instance by the actor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoginAttribute) -> dict:
    out: dict = {}
    if "user" in value:
        out["user"] = value["user"]
    if "application" in value:
        out["application"] = value["application"]
    if "failed_login_attempts" in value:
        out["failedLoginAttempts"] = value["failed_login_attempts"]
    if "successful_login_attempts" in value:
        out["successfulLoginAttempts"] = value["successful_login_attempts"]
    return out


def deserialize_json(data: dict) -> LoginAttribute:
    out: LoginAttribute = {}  # type: ignore[typeddict-item]
    if "user" in data:
        out["user"] = data["user"]
    if "application" in data:
        out["application"] = data["application"]
    if "failedLoginAttempts" in data:
        out["failed_login_attempts"] = data["failedLoginAttempts"]
    if "successfulLoginAttempts" in data:
        out["successful_login_attempts"] = data["successfulLoginAttempts"]
    return out
