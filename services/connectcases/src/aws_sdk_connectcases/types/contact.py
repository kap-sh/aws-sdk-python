"""Generated from Smithy shape ``com.amazonaws.connectcases#Contact``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.contact_arn


class Contact(TypedDict, closed=True):
    contact_arn: "aws_sdk_connectcases.types.contact_arn.ContactArn"
    """<p>A unique identifier of a contact in Amazon Connect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Contact) -> dict:
    out: dict = {}
    out["contactArn"] = value["contact_arn"]
    return out


def deserialize_json(data: dict) -> Contact:
    out: Contact = {}  # type: ignore[typeddict-item]
    if "contactArn" in data:
        out["contact_arn"] = data["contactArn"]
    else:
        raise DeserializationError("Contact.contact_arn required")
    return out
