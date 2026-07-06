"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#OriginationIdentityMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code
    import aws_sdk_pinpoint_sms_voice_v2.types.number_capability_list
    import aws_sdk_pinpoint_sms_voice_v2.types.phone_number


class OriginationIdentityMetadata(TypedDict, closed=True):
    origination_identity_arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the origination identity.</p>"""
    origination_identity: "str"
    """<p>The unique identifier of the origination identity.</p>"""
    iso_country_code: (
        "aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    )
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region. This field is optional and may not be present for origination identity types that are not country-specific, such as RCS agents.</p>"""
    number_capabilities: "aws_sdk_pinpoint_sms_voice_v2.types.number_capability_list.NumberCapabilityList"
    """<p>Describes if the origination identity can be used for text messages, voice calls or both.</p>"""
    phone_number: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    ]
    """<p>The phone number in E.164 format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OriginationIdentityMetadata) -> dict:
    out: dict = {}
    out["OriginationIdentityArn"] = value["origination_identity_arn"]
    out["OriginationIdentity"] = value["origination_identity"]
    out["IsoCountryCode"] = value["iso_country_code"]
    import aws_sdk_pinpoint_sms_voice_v2.types.number_capability_list

    out["NumberCapabilities"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.number_capability_list.serialize_aws_json_1_0(
            value["number_capabilities"]
        )
    )
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    return out


def deserialize_aws_json_1_0(data: dict) -> OriginationIdentityMetadata:
    out: OriginationIdentityMetadata = {}  # type: ignore[typeddict-item]
    if "OriginationIdentityArn" in data:
        out["origination_identity_arn"] = data["OriginationIdentityArn"]
    else:
        raise DeserializationError(
            "OriginationIdentityMetadata.origination_identity_arn required"
        )
    if "OriginationIdentity" in data:
        out["origination_identity"] = data["OriginationIdentity"]
    else:
        raise DeserializationError(
            "OriginationIdentityMetadata.origination_identity required"
        )
    if "IsoCountryCode" in data:
        out["iso_country_code"] = data["IsoCountryCode"]
    else:
        raise DeserializationError(
            "OriginationIdentityMetadata.iso_country_code required"
        )
    if "NumberCapabilities" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.number_capability_list

        out["number_capabilities"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.number_capability_list.deserialize_aws_json_1_0(
                data["NumberCapabilities"]
            )
        )
    else:
        raise DeserializationError(
            "OriginationIdentityMetadata.number_capabilities required"
        )
    if "PhoneNumber" in data:
        out["phone_number"] = data["PhoneNumber"]
    return out
