"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppPhoneNumberDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.iso_country_code
    import capo_socialmessaging.types.linked_whats_app_phone_number_arn
    import capo_socialmessaging.types.phone_number
    import capo_socialmessaging.types.whats_app_display_phone_number
    import capo_socialmessaging.types.whats_app_phone_number
    import capo_socialmessaging.types.whats_app_phone_number_id
    import capo_socialmessaging.types.whats_app_phone_number_name
    import capo_socialmessaging.types.whats_app_phone_number_quality_rating


class WhatsAppPhoneNumberDetail(TypedDict, closed=True):
    arn: "capo_socialmessaging.types.linked_whats_app_phone_number_arn.LinkedWhatsAppPhoneNumberArn"
    """<p>The ARN of the WhatsApp phone number.</p>"""
    phone_number: "capo_socialmessaging.types.phone_number.PhoneNumber"
    """<p>The phone number for sending WhatsApp.</p>"""
    phone_number_id: (
        "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId"
    )
    """<p>The phone number ID. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. </p>"""
    meta_phone_number_id: (
        "capo_socialmessaging.types.whats_app_phone_number.WhatsAppPhoneNumber"
    )
    """<p>The phone number ID from Meta.</p>"""
    display_phone_number_name: (
        "capo_socialmessaging.types.whats_app_phone_number_name.WhatsAppPhoneNumberName"
    )
    """<p>The display name for this phone number.</p>"""
    display_phone_number: "capo_socialmessaging.types.whats_app_display_phone_number.WhatsAppDisplayPhoneNumber"
    """<p>The phone number that appears in the recipients display.</p>"""
    quality_rating: "capo_socialmessaging.types.whats_app_phone_number_quality_rating.WhatsAppPhoneNumberQualityRating"
    """<p>The quality rating of the phone number.</p>"""
    data_localization_region: NotRequired[
        "capo_socialmessaging.types.iso_country_code.IsoCountryCode"
    ]
    """<p>The geographic region where the WhatsApp phone number's data is stored and processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppPhoneNumberDetail) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["phoneNumber"] = value["phone_number"]
    out["phoneNumberId"] = value["phone_number_id"]
    out["metaPhoneNumberId"] = value["meta_phone_number_id"]
    out["displayPhoneNumberName"] = value["display_phone_number_name"]
    out["displayPhoneNumber"] = value["display_phone_number"]
    out["qualityRating"] = value["quality_rating"]
    if "data_localization_region" in value:
        out["dataLocalizationRegion"] = value["data_localization_region"]
    return out


def deserialize_json(data: dict) -> WhatsAppPhoneNumberDetail:
    out: WhatsAppPhoneNumberDetail = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("WhatsAppPhoneNumberDetail.arn required")
    if "phoneNumber" in data:
        out["phone_number"] = data["phoneNumber"]
    else:
        raise DeserializationError("WhatsAppPhoneNumberDetail.phone_number required")
    if "phoneNumberId" in data:
        out["phone_number_id"] = data["phoneNumberId"]
    else:
        raise DeserializationError("WhatsAppPhoneNumberDetail.phone_number_id required")
    if "metaPhoneNumberId" in data:
        out["meta_phone_number_id"] = data["metaPhoneNumberId"]
    else:
        raise DeserializationError(
            "WhatsAppPhoneNumberDetail.meta_phone_number_id required"
        )
    if "displayPhoneNumberName" in data:
        out["display_phone_number_name"] = data["displayPhoneNumberName"]
    else:
        raise DeserializationError(
            "WhatsAppPhoneNumberDetail.display_phone_number_name required"
        )
    if "displayPhoneNumber" in data:
        out["display_phone_number"] = data["displayPhoneNumber"]
    else:
        raise DeserializationError(
            "WhatsAppPhoneNumberDetail.display_phone_number required"
        )
    if "qualityRating" in data:
        out["quality_rating"] = data["qualityRating"]
    else:
        raise DeserializationError("WhatsAppPhoneNumberDetail.quality_rating required")
    if "dataLocalizationRegion" in data:
        out["data_localization_region"] = data["dataLocalizationRegion"]
    return out
