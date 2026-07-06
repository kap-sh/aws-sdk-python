"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetLinkedWhatsAppBusinessAccountPhoneNumberOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_id
    import aws_sdk_socialmessaging.types.whats_app_phone_number_detail


class GetLinkedWhatsAppBusinessAccountPhoneNumberOutput(TypedDict, closed=True):
    phone_number: NotRequired[
        "aws_sdk_socialmessaging.types.whats_app_phone_number_detail.WhatsAppPhoneNumberDetail"
    ]
    linked_whats_app_business_account_id: NotRequired[
        "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    ]
    """<p>The WABA identifier linked to the phone number, formatted as <code>waba-01234567890123456789012345678901</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLinkedWhatsAppBusinessAccountPhoneNumberOutput) -> dict:
    out: dict = {}
    if "phone_number" in value:
        import aws_sdk_socialmessaging.types.whats_app_phone_number_detail

        out["phoneNumber"] = (
            aws_sdk_socialmessaging.types.whats_app_phone_number_detail.serialize_json(
                value["phone_number"]
            )
        )
    if "linked_whats_app_business_account_id" in value:
        out["linkedWhatsAppBusinessAccountId"] = value[
            "linked_whats_app_business_account_id"
        ]
    return out


def deserialize_json(data: dict) -> GetLinkedWhatsAppBusinessAccountPhoneNumberOutput:
    out: GetLinkedWhatsAppBusinessAccountPhoneNumberOutput = {}  # type: ignore[typeddict-item]
    if "phoneNumber" in data:
        import aws_sdk_socialmessaging.types.whats_app_phone_number_detail

        out["phone_number"] = (
            aws_sdk_socialmessaging.types.whats_app_phone_number_detail.deserialize_json(
                data["phoneNumber"]
            )
        )
    if "linkedWhatsAppBusinessAccountId" in data:
        out["linked_whats_app_business_account_id"] = data[
            "linkedWhatsAppBusinessAccountId"
        ]
    return out
