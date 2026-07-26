"""Generated from Smithy shape ``com.amazonaws.socialmessaging#LinkedWhatsAppBusinessAccountIdMetaData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.registration_status
    import capo_socialmessaging.types.whats_app_business_account_name
    import capo_socialmessaging.types.whats_app_phone_number_detail_list


class LinkedWhatsAppBusinessAccountIdMetaData(TypedDict, closed=True):
    account_name: NotRequired[
        "capo_socialmessaging.types.whats_app_business_account_name.WhatsAppBusinessAccountName"
    ]
    """<p>The name of your account.</p>"""
    registration_status: NotRequired[
        "capo_socialmessaging.types.registration_status.RegistrationStatus"
    ]
    """<p>The registration status of the linked WhatsApp Business Account.</p>"""
    unregistered_whats_app_phone_numbers: NotRequired[
        "capo_socialmessaging.types.whats_app_phone_number_detail_list.WhatsAppPhoneNumberDetailList"
    ]
    """<p>The details for unregistered WhatsApp phone numbers.</p>"""
    waba_id: NotRequired[
        "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    ]
    """<p>The Amazon Resource Name (ARN) of the WhatsApp Business Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkedWhatsAppBusinessAccountIdMetaData) -> dict:
    out: dict = {}
    if "account_name" in value:
        out["accountName"] = value["account_name"]
    if "registration_status" in value:
        import capo_socialmessaging.types.registration_status

        out["registrationStatus"] = (
            capo_socialmessaging.types.registration_status.serialize_json(
                value["registration_status"]
            )
        )
    if "unregistered_whats_app_phone_numbers" in value:
        import capo_socialmessaging.types.whats_app_phone_number_detail_list

        out["unregisteredWhatsAppPhoneNumbers"] = (
            capo_socialmessaging.types.whats_app_phone_number_detail_list.serialize_json(
                value["unregistered_whats_app_phone_numbers"]
            )
        )
    if "waba_id" in value:
        out["wabaId"] = value["waba_id"]
    return out


def deserialize_json(data: dict) -> LinkedWhatsAppBusinessAccountIdMetaData:
    out: LinkedWhatsAppBusinessAccountIdMetaData = {}  # type: ignore[typeddict-item]
    if "accountName" in data:
        out["account_name"] = data["accountName"]
    if "registrationStatus" in data:
        import capo_socialmessaging.types.registration_status

        out["registration_status"] = (
            capo_socialmessaging.types.registration_status.deserialize_json(
                data["registrationStatus"]
            )
        )
    if "unregisteredWhatsAppPhoneNumbers" in data:
        import capo_socialmessaging.types.whats_app_phone_number_detail_list

        out["unregistered_whats_app_phone_numbers"] = (
            capo_socialmessaging.types.whats_app_phone_number_detail_list.deserialize_json(
                data["unregisteredWhatsAppPhoneNumbers"]
            )
        )
    if "wabaId" in data:
        out["waba_id"] = data["wabaId"]
    return out
