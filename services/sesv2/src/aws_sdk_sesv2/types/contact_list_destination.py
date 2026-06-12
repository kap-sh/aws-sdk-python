"""Generated from Smithy shape ``com.amazonaws.sesv2#ContactListDestination``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.contact_list_import_action
    import aws_sdk_sesv2.types.contact_list_name


class ContactListDestination(TypedDict):
    contact_list_name: "aws_sdk_sesv2.types.contact_list_name.ContactListName"
    """<p>The name of the contact list.</p>"""
    contact_list_import_action: (
        "aws_sdk_sesv2.types.contact_list_import_action.ContactListImportAction"
    )
    """<p>>The type of action to perform on the addresses. The following are the possible values:</p> <ul> <li> <p>PUT: add the addresses to the contact list. If the record already exists, it will override it with the new value.</p> </li> <li> <p>DELETE: remove the addresses from the contact list.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactListDestination) -> dict:
    out: dict = {}
    out["ContactListName"] = value["contact_list_name"]
    import aws_sdk_sesv2.types.contact_list_import_action

    out["ContactListImportAction"] = (
        aws_sdk_sesv2.types.contact_list_import_action.serialize_json(
            value["contact_list_import_action"]
        )
    )
    return out


def deserialize_json(data: dict) -> ContactListDestination:
    out: ContactListDestination = {}  # type: ignore[typeddict-item]
    if "ContactListName" in data:
        out["contact_list_name"] = data["ContactListName"]
    else:
        raise DeserializationError("ContactListDestination.contact_list_name required")
    if "ContactListImportAction" in data:
        import aws_sdk_sesv2.types.contact_list_import_action

        out["contact_list_import_action"] = (
            aws_sdk_sesv2.types.contact_list_import_action.deserialize_json(
                data["ContactListImportAction"]
            )
        )
    else:
        raise DeserializationError(
            "ContactListDestination.contact_list_import_action required"
        )
    return out
