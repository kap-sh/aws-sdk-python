"""Generated from Smithy shape ``com.amazonaws.connect#UserIdentityInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_first_name
    import aws_sdk_connect.types.agent_last_name
    import aws_sdk_connect.types.email
    import aws_sdk_connect.types.phone_number


class UserIdentityInfo(TypedDict):
    first_name: NotRequired["aws_sdk_connect.types.agent_first_name.AgentFirstName"]
    """<p>The first name. This is required if you are using Connect Customer or SAML for identity management. Inputs must be in Unicode Normalization Form C (NFC). Text containing characters in a non-NFC form (for example, decomposed characters or combining marks) are not accepted.</p>"""
    last_name: NotRequired["aws_sdk_connect.types.agent_last_name.AgentLastName"]
    """<p>The last name. This is required if you are using Connect Customer or SAML for identity management. Inputs must be in Unicode Normalization Form C (NFC). Text containing characters in a non-NFC form (for example, decomposed characters or combining marks) are not accepted.</p>"""
    email: NotRequired["aws_sdk_connect.types.email.Email"]
    """<p>The email address. If you are using SAML for identity management and include this parameter, an error is returned.</p>"""
    secondary_email: NotRequired["aws_sdk_connect.types.email.Email"]
    """<p>The user's secondary email address. If you provide a secondary email, the user receives email notifications - other than password reset notifications - to this email address instead of to their primary email address.</p> <p>Pattern: <code>(?=^.{0,265}$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,63}</code> </p>"""
    mobile: NotRequired["aws_sdk_connect.types.phone_number.PhoneNumber"]
    """<p>The user's mobile number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserIdentityInfo) -> dict:
    out: dict = {}
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    if "email" in value:
        out["Email"] = value["email"]
    if "secondary_email" in value:
        out["SecondaryEmail"] = value["secondary_email"]
    if "mobile" in value:
        out["Mobile"] = value["mobile"]
    return out


def deserialize_json(data: dict) -> UserIdentityInfo:
    out: UserIdentityInfo = {}  # type: ignore[typeddict-item]
    if "FirstName" in data:
        out["first_name"] = data["FirstName"]
    if "LastName" in data:
        out["last_name"] = data["LastName"]
    if "Email" in data:
        out["email"] = data["Email"]
    if "SecondaryEmail" in data:
        out["secondary_email"] = data["SecondaryEmail"]
    if "Mobile" in data:
        out["mobile"] = data["Mobile"]
    return out
