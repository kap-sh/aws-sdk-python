"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationAssociationMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.iso_country_code
    import capo_pinpoint_sms_voice_v2.types.phone_number


class RegistrationAssociationMetadata(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the origination identity that is associated with the registration. </p>"""
    resource_id: "str"
    """<p>The unique identifier for the origination identity. For example this could be a <b>PhoneNumberId</b> or <b>SenderId</b>.</p>"""
    resource_type: "str"
    """<p>The origination identity type.</p>"""
    iso_country_code: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    ]
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>"""
    phone_number: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    ]
    """<p>The phone number associated with the registration in E.164 format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationAssociationMetadata) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    if "iso_country_code" in value:
        out["IsoCountryCode"] = value["iso_country_code"]
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RegistrationAssociationMetadata:
    out: RegistrationAssociationMetadata = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "RegistrationAssociationMetadata.resource_arn required"
        )
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "RegistrationAssociationMetadata.resource_id required"
        )
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError(
            "RegistrationAssociationMetadata.resource_type required"
        )
    if "IsoCountryCode" in data:
        out["iso_country_code"] = data["IsoCountryCode"]
    if "PhoneNumber" in data:
        out["phone_number"] = data["PhoneNumber"]
    return out
