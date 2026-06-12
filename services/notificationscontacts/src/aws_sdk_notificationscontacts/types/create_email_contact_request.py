"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#CreateEmailContactRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_notificationscontacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notificationscontacts.types.email_contact_address
    import aws_sdk_notificationscontacts.types.email_contact_name
    import aws_sdk_notificationscontacts.types.tag_map


class CreateEmailContactRequest(TypedDict):
    name: "aws_sdk_notificationscontacts.types.email_contact_name.EmailContactName"
    """<p>The name of the email contact.</p>"""
    email_address: (
        "aws_sdk_notificationscontacts.types.email_contact_address.EmailContactAddress"
    )
    """<p>The email address this email contact points to. The activation email and any subscribed emails are sent here.</p> <note> <p>This email address can't receive emails until it's activated.</p> </note>"""
    tags: NotRequired["aws_sdk_notificationscontacts.types.tag_map.TagMap"]
    """<p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEmailContactRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["emailAddress"] = value["email_address"]
    if "tags" in value:
        import aws_sdk_notificationscontacts.types.tag_map

        out["tags"] = aws_sdk_notificationscontacts.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateEmailContactRequest:
    out: CreateEmailContactRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEmailContactRequest.name required")
    if "emailAddress" in data:
        out["email_address"] = data["emailAddress"]
    else:
        raise DeserializationError("CreateEmailContactRequest.email_address required")
    if "tags" in data:
        import aws_sdk_notificationscontacts.types.tag_map

        out["tags"] = aws_sdk_notificationscontacts.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
