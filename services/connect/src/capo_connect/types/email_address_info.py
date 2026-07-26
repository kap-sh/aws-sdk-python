"""Generated from Smithy shape ``com.amazonaws.connect#EmailAddressInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.email_address
    import capo_connect.types.email_address_display_name


class EmailAddressInfo(TypedDict, closed=True):
    email_address: "capo_connect.types.email_address.EmailAddress"
    """<p>The email address, including the domain.</p>"""
    display_name: NotRequired[
        "capo_connect.types.email_address_display_name.EmailAddressDisplayName"
    ]
    """<p>The display name of email address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressInfo) -> dict:
    out: dict = {}
    out["EmailAddress"] = value["email_address"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> EmailAddressInfo:
    out: EmailAddressInfo = {}  # type: ignore[typeddict-item]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    else:
        raise DeserializationError("EmailAddressInfo.email_address required")
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    return out
