"""Generated from Smithy shape ``com.amazonaws.socialmessaging#LinkedWhatsAppBusinessAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_arn
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.registration_status
    import capo_socialmessaging.types.whats_app_business_account_event_destinations
    import capo_socialmessaging.types.whats_app_business_account_id
    import capo_socialmessaging.types.whats_app_business_account_link_date
    import capo_socialmessaging.types.whats_app_business_account_marketing_messages_onboarding_status
    import capo_socialmessaging.types.whats_app_business_account_name
    import capo_socialmessaging.types.whats_app_phone_number_summary_list


class LinkedWhatsAppBusinessAccount(TypedDict, closed=True):
    arn: "capo_socialmessaging.types.linked_whats_app_business_account_arn.LinkedWhatsAppBusinessAccountArn"
    """<p>The ARN of the linked WhatsApp Business Account.</p>"""
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the linked WhatsApp Business Account, formatted as <code>waba-01234567890123456789012345678901</code>.</p>"""
    waba_id: "capo_socialmessaging.types.whats_app_business_account_id.WhatsAppBusinessAccountId"
    """<p>The WhatsApp Business Account ID from meta.</p>"""
    registration_status: (
        "capo_socialmessaging.types.registration_status.RegistrationStatus"
    )
    """<p>The registration status of the linked WhatsApp Business Account.</p>"""
    link_date: "capo_socialmessaging.types.whats_app_business_account_link_date.WhatsAppBusinessAccountLinkDate"
    """<p>The date the WhatsApp Business Account was linked.</p>"""
    waba_name: "capo_socialmessaging.types.whats_app_business_account_name.WhatsAppBusinessAccountName"
    """<p>The name of the linked WhatsApp Business Account.</p>"""
    event_destinations: "capo_socialmessaging.types.whats_app_business_account_event_destinations.WhatsAppBusinessAccountEventDestinations"
    """<p>The event destinations for the linked WhatsApp Business Account.</p>"""
    marketing_messages_onboarding_status: NotRequired[
        "capo_socialmessaging.types.whats_app_business_account_marketing_messages_onboarding_status.WhatsAppBusinessAccountMarketingMessagesOnboardingStatus"
    ]
    """<p>The onboarding status for the Marketing Messages API. This value is fetched from Meta and indicates whether the WhatsApp Business Account is onboarded for Meta's Marketing Messages API.</p>"""
    phone_numbers: "capo_socialmessaging.types.whats_app_phone_number_summary_list.WhatsAppPhoneNumberSummaryList"
    """<p>The phone numbers associated with the Linked WhatsApp Business Account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkedWhatsAppBusinessAccount) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["wabaId"] = value["waba_id"]
    import capo_socialmessaging.types.registration_status

    out["registrationStatus"] = (
        capo_socialmessaging.types.registration_status.serialize_json(
            value["registration_status"]
        )
    )
    import capo_socialmessaging.types.whats_app_business_account_link_date

    out["linkDate"] = (
        capo_socialmessaging.types.whats_app_business_account_link_date.serialize_json(
            value["link_date"]
        )
    )
    out["wabaName"] = value["waba_name"]
    import capo_socialmessaging.types.whats_app_business_account_event_destinations

    out["eventDestinations"] = (
        capo_socialmessaging.types.whats_app_business_account_event_destinations.serialize_json(
            value["event_destinations"]
        )
    )
    if "marketing_messages_onboarding_status" in value:
        out["marketingMessagesOnboardingStatus"] = value[
            "marketing_messages_onboarding_status"
        ]
    import capo_socialmessaging.types.whats_app_phone_number_summary_list

    out["phoneNumbers"] = (
        capo_socialmessaging.types.whats_app_phone_number_summary_list.serialize_json(
            value["phone_numbers"]
        )
    )
    return out


def deserialize_json(data: dict) -> LinkedWhatsAppBusinessAccount:
    out: LinkedWhatsAppBusinessAccount = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("LinkedWhatsAppBusinessAccount.arn required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("LinkedWhatsAppBusinessAccount.id required")
    if "wabaId" in data:
        out["waba_id"] = data["wabaId"]
    else:
        raise DeserializationError("LinkedWhatsAppBusinessAccount.waba_id required")
    if "registrationStatus" in data:
        import capo_socialmessaging.types.registration_status

        out["registration_status"] = (
            capo_socialmessaging.types.registration_status.deserialize_json(
                data["registrationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "LinkedWhatsAppBusinessAccount.registration_status required"
        )
    if "linkDate" in data:
        import capo_socialmessaging.types.whats_app_business_account_link_date

        out["link_date"] = (
            capo_socialmessaging.types.whats_app_business_account_link_date.deserialize_json(
                data["linkDate"]
            )
        )
    else:
        raise DeserializationError("LinkedWhatsAppBusinessAccount.link_date required")
    if "wabaName" in data:
        out["waba_name"] = data["wabaName"]
    else:
        raise DeserializationError("LinkedWhatsAppBusinessAccount.waba_name required")
    if "eventDestinations" in data:
        import capo_socialmessaging.types.whats_app_business_account_event_destinations

        out["event_destinations"] = (
            capo_socialmessaging.types.whats_app_business_account_event_destinations.deserialize_json(
                data["eventDestinations"]
            )
        )
    else:
        raise DeserializationError(
            "LinkedWhatsAppBusinessAccount.event_destinations required"
        )
    if "marketingMessagesOnboardingStatus" in data:
        out["marketing_messages_onboarding_status"] = data[
            "marketingMessagesOnboardingStatus"
        ]
    if "phoneNumbers" in data:
        import capo_socialmessaging.types.whats_app_phone_number_summary_list

        out["phone_numbers"] = (
            capo_socialmessaging.types.whats_app_phone_number_summary_list.deserialize_json(
                data["phoneNumbers"]
            )
        )
    else:
        raise DeserializationError(
            "LinkedWhatsAppBusinessAccount.phone_numbers required"
        )
    return out
