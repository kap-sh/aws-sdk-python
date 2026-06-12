"""Generated from Smithy shape ``com.amazonaws.sesv2#ContactList``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.contact_list_name
    import aws_sdk_sesv2.types.timestamp


class ContactList(TypedDict):
    contact_list_name: NotRequired[
        "aws_sdk_sesv2.types.contact_list_name.ContactListName"
    ]
    """<p>The name of the contact list.</p>"""
    last_updated_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>A timestamp noting the last time the contact list was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactList) -> dict:
    out: dict = {}
    if "contact_list_name" in value:
        out["ContactListName"] = value["contact_list_name"]
    if "last_updated_timestamp" in value:
        import aws_sdk_sesv2.types.timestamp

        out["LastUpdatedTimestamp"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["last_updated_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> ContactList:
    out: ContactList = {}  # type: ignore[typeddict-item]
    if "ContactListName" in data:
        out["contact_list_name"] = data["ContactListName"]
    if "LastUpdatedTimestamp" in data:
        import aws_sdk_sesv2.types.timestamp

        out["last_updated_timestamp"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["LastUpdatedTimestamp"]
        )
    return out
