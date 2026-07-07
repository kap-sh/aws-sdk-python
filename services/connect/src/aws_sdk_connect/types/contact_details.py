"""Generated from Smithy shape ``com.amazonaws.connect#ContactDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_detail_description
    import aws_sdk_connect.types.contact_detail_name


class ContactDetails(TypedDict, closed=True):
    name: NotRequired["aws_sdk_connect.types.contact_detail_name.ContactDetailName"]
    """<p>The name of the contact details.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.contact_detail_description.ContactDetailDescription"
    ]
    """<p>Teh description of the contact details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ContactDetails:
    out: ContactDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
