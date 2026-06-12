"""Generated from Smithy shape ``com.amazonaws.pinpointemail#Destination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.email_address_list


class Destination(TypedDict):
    to_addresses: NotRequired[
        "aws_sdk_pinpoint_email.types.email_address_list.EmailAddressList"
    ]
    """<p>An array that contains the email addresses of the \"To\" recipients for the email.</p>"""
    cc_addresses: NotRequired[
        "aws_sdk_pinpoint_email.types.email_address_list.EmailAddressList"
    ]
    """<p>An array that contains the email addresses of the \"CC\" (carbon copy) recipients for the email.</p>"""
    bcc_addresses: NotRequired[
        "aws_sdk_pinpoint_email.types.email_address_list.EmailAddressList"
    ]
    """<p>An array that contains the email addresses of the \"BCC\" (blind carbon copy) recipients for the email.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    out: dict = {}
    if "to_addresses" in value:
        import aws_sdk_pinpoint_email.types.email_address_list

        out["ToAddresses"] = (
            aws_sdk_pinpoint_email.types.email_address_list.serialize_json(
                value["to_addresses"]
            )
        )
    if "cc_addresses" in value:
        import aws_sdk_pinpoint_email.types.email_address_list

        out["CcAddresses"] = (
            aws_sdk_pinpoint_email.types.email_address_list.serialize_json(
                value["cc_addresses"]
            )
        )
    if "bcc_addresses" in value:
        import aws_sdk_pinpoint_email.types.email_address_list

        out["BccAddresses"] = (
            aws_sdk_pinpoint_email.types.email_address_list.serialize_json(
                value["bcc_addresses"]
            )
        )
    return out


def deserialize_json(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if "ToAddresses" in data:
        import aws_sdk_pinpoint_email.types.email_address_list

        out["to_addresses"] = (
            aws_sdk_pinpoint_email.types.email_address_list.deserialize_json(
                data["ToAddresses"]
            )
        )
    if "CcAddresses" in data:
        import aws_sdk_pinpoint_email.types.email_address_list

        out["cc_addresses"] = (
            aws_sdk_pinpoint_email.types.email_address_list.deserialize_json(
                data["CcAddresses"]
            )
        )
    if "BccAddresses" in data:
        import aws_sdk_pinpoint_email.types.email_address_list

        out["bcc_addresses"] = (
            aws_sdk_pinpoint_email.types.email_address_list.deserialize_json(
                data["BccAddresses"]
            )
        )
    return out
