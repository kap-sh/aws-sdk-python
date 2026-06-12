"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#EmailContact``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_notificationscontacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notificationscontacts.types.creation_time
    import aws_sdk_notificationscontacts.types.email_contact_arn
    import aws_sdk_notificationscontacts.types.email_contact_name
    import aws_sdk_notificationscontacts.types.email_contact_status
    import aws_sdk_notificationscontacts.types.sensitive_email_contact_address
    import aws_sdk_notificationscontacts.types.update_time


class EmailContact(TypedDict):
    arn: "aws_sdk_notificationscontacts.types.email_contact_arn.EmailContactArn"
    """<p>The Amazon Resource Name (ARN) of the email contact.</p>"""
    name: "aws_sdk_notificationscontacts.types.email_contact_name.EmailContactName"
    """<p>The name of the email contact.</p>"""
    address: "aws_sdk_notificationscontacts.types.sensitive_email_contact_address.SensitiveEmailContactAddress"
    """<p>The email address this email contact points to. The activation email and any subscribed emails are sent here.</p>"""
    status: (
        "aws_sdk_notificationscontacts.types.email_contact_status.EmailContactStatus"
    )
    """<p>The status of the email contact. Only activated email contacts receive emails.</p>"""
    creation_time: "aws_sdk_notificationscontacts.types.creation_time.CreationTime"
    """<p>The creation time of the resource.</p>"""
    update_time: "aws_sdk_notificationscontacts.types.update_time.UpdateTime"
    """<p>The time the resource was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailContact) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["address"] = value["address"]
    out["status"] = value["status"]
    import aws_sdk_notificationscontacts.types.creation_time

    out["creationTime"] = (
        aws_sdk_notificationscontacts.types.creation_time.serialize_json(
            value["creation_time"]
        )
    )
    import aws_sdk_notificationscontacts.types.update_time

    out["updateTime"] = aws_sdk_notificationscontacts.types.update_time.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> EmailContact:
    out: EmailContact = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("EmailContact.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("EmailContact.name required")
    if "address" in data:
        out["address"] = data["address"]
    else:
        raise DeserializationError("EmailContact.address required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("EmailContact.status required")
    if "creationTime" in data:
        import aws_sdk_notificationscontacts.types.creation_time

        out["creation_time"] = (
            aws_sdk_notificationscontacts.types.creation_time.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("EmailContact.creation_time required")
    if "updateTime" in data:
        import aws_sdk_notificationscontacts.types.update_time

        out["update_time"] = (
            aws_sdk_notificationscontacts.types.update_time.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("EmailContact.update_time required")
    return out
