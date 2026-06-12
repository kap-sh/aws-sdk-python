"""Generated from Smithy shape ``com.amazonaws.socialmessaging#LinkedWhatsAppBusinessAccountSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_arn
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_id
    import aws_sdk_socialmessaging.types.registration_status
    import aws_sdk_socialmessaging.types.whats_app_business_account_event_destinations
    import aws_sdk_socialmessaging.types.whats_app_business_account_id
    import aws_sdk_socialmessaging.types.whats_app_business_account_link_date
    import aws_sdk_socialmessaging.types.whats_app_business_account_marketing_messages_onboarding_status
    import aws_sdk_socialmessaging.types.whats_app_business_account_name


class LinkedWhatsAppBusinessAccountSummary(TypedDict):
    arn: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_arn.LinkedWhatsAppBusinessAccountArn"
    """<p>The ARN of the linked WhatsApp Business Account.</p>"""
    id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the linked WhatsApp Business Account, formatted as <code>waba-01234567890123456789012345678901</code>.</p>"""
    waba_id: "aws_sdk_socialmessaging.types.whats_app_business_account_id.WhatsAppBusinessAccountId"
    """<p>The WhatsApp Business Account ID provided by Meta.</p>"""
    registration_status: (
        "aws_sdk_socialmessaging.types.registration_status.RegistrationStatus"
    )
    """<p>The registration status of the linked WhatsApp Business Account.</p>"""
    link_date: "aws_sdk_socialmessaging.types.whats_app_business_account_link_date.WhatsAppBusinessAccountLinkDate"
    """<p>The date the WhatsApp Business Account was linked.</p>"""
    waba_name: "aws_sdk_socialmessaging.types.whats_app_business_account_name.WhatsAppBusinessAccountName"
    """<p>The name of the linked WhatsApp Business Account.</p>"""
    event_destinations: "aws_sdk_socialmessaging.types.whats_app_business_account_event_destinations.WhatsAppBusinessAccountEventDestinations"
    """<p>The event destinations for the linked WhatsApp Business Account.</p>"""
    marketing_messages_onboarding_status: NotRequired[
        "aws_sdk_socialmessaging.types.whats_app_business_account_marketing_messages_onboarding_status.WhatsAppBusinessAccountMarketingMessagesOnboardingStatus"
    ]
    """<p>The onboarding status for the Marketing Messages API. This value is fetched from Meta and indicates whether the WhatsApp Business Account is onboarded for Meta's Marketing Messages API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkedWhatsAppBusinessAccountSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["wabaId"] = value["waba_id"]
    import aws_sdk_socialmessaging.types.registration_status

    out["registrationStatus"] = (
        aws_sdk_socialmessaging.types.registration_status.serialize_json(
            value["registration_status"]
        )
    )
    import aws_sdk_socialmessaging.types.whats_app_business_account_link_date

    out["linkDate"] = (
        aws_sdk_socialmessaging.types.whats_app_business_account_link_date.serialize_json(
            value["link_date"]
        )
    )
    out["wabaName"] = value["waba_name"]
    import aws_sdk_socialmessaging.types.whats_app_business_account_event_destinations

    out["eventDestinations"] = (
        aws_sdk_socialmessaging.types.whats_app_business_account_event_destinations.serialize_json(
            value["event_destinations"]
        )
    )
    if "marketing_messages_onboarding_status" in value:
        out["marketingMessagesOnboardingStatus"] = value[
            "marketing_messages_onboarding_status"
        ]
    return out


def deserialize_json(data: dict) -> LinkedWhatsAppBusinessAccountSummary:
    out: LinkedWhatsAppBusinessAccountSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("LinkedWhatsAppBusinessAccountSummary.arn required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("LinkedWhatsAppBusinessAccountSummary.id required")
    if "wabaId" in data:
        out["waba_id"] = data["wabaId"]
    else:
        raise DeserializationError(
            "LinkedWhatsAppBusinessAccountSummary.waba_id required"
        )
    if "registrationStatus" in data:
        import aws_sdk_socialmessaging.types.registration_status

        out["registration_status"] = (
            aws_sdk_socialmessaging.types.registration_status.deserialize_json(
                data["registrationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "LinkedWhatsAppBusinessAccountSummary.registration_status required"
        )
    if "linkDate" in data:
        import aws_sdk_socialmessaging.types.whats_app_business_account_link_date

        out["link_date"] = (
            aws_sdk_socialmessaging.types.whats_app_business_account_link_date.deserialize_json(
                data["linkDate"]
            )
        )
    else:
        raise DeserializationError(
            "LinkedWhatsAppBusinessAccountSummary.link_date required"
        )
    if "wabaName" in data:
        out["waba_name"] = data["wabaName"]
    else:
        raise DeserializationError(
            "LinkedWhatsAppBusinessAccountSummary.waba_name required"
        )
    if "eventDestinations" in data:
        import aws_sdk_socialmessaging.types.whats_app_business_account_event_destinations

        out["event_destinations"] = (
            aws_sdk_socialmessaging.types.whats_app_business_account_event_destinations.deserialize_json(
                data["eventDestinations"]
            )
        )
    else:
        raise DeserializationError(
            "LinkedWhatsAppBusinessAccountSummary.event_destinations required"
        )
    if "marketingMessagesOnboardingStatus" in data:
        out["marketing_messages_onboarding_status"] = data[
            "marketingMessagesOnboardingStatus"
        ]
    return out
