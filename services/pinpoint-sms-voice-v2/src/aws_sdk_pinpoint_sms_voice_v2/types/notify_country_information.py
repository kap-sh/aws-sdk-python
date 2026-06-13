"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyCountryInformation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_tier_list
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_use_case_list


class NotifyCountryInformation(TypedDict):
    iso_country_code: (
        "aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    )
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>"""
    country_name: "str"
    """<p>The name of the country.</p>"""
    supported_channels: "aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.NotifyEnabledChannelsList"
    """<p>An array of supported channels for the country. Supported values include <code>SMS</code> and <code>VOICE</code>.</p>"""
    supported_use_cases: (
        "aws_sdk_pinpoint_sms_voice_v2.types.notify_use_case_list.NotifyUseCaseList"
    )
    """<p>An array of supported use cases for the country.</p>"""
    supported_tiers: (
        "aws_sdk_pinpoint_sms_voice_v2.types.notify_tier_list.NotifyTierList"
    )
    """<p>An array of supported tiers for the country.</p>"""
    customer_owned_identity_required: "bool"
    """<p>Whether a customer-owned identity is required to send notify messages to this country.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotifyCountryInformation) -> dict:
    out: dict = {}
    out["IsoCountryCode"] = value["iso_country_code"]
    out["CountryName"] = value["country_name"]
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list

    out["SupportedChannels"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.serialize_aws_json_1_0(
            value["supported_channels"]
        )
    )
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_use_case_list

    out["SupportedUseCases"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.notify_use_case_list.serialize_aws_json_1_0(
            value["supported_use_cases"]
        )
    )
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_tier_list

    out["SupportedTiers"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.notify_tier_list.serialize_aws_json_1_0(
            value["supported_tiers"]
        )
    )
    out["CustomerOwnedIdentityRequired"] = value.get(
        "customer_owned_identity_required", False
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> NotifyCountryInformation:
    out: NotifyCountryInformation = {}  # type: ignore[typeddict-item]
    if "IsoCountryCode" in data:
        out["iso_country_code"] = data["IsoCountryCode"]
    else:
        raise DeserializationError("NotifyCountryInformation.iso_country_code required")
    if "CountryName" in data:
        out["country_name"] = data["CountryName"]
    else:
        raise DeserializationError("NotifyCountryInformation.country_name required")
    if "SupportedChannels" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list

        out["supported_channels"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.deserialize_aws_json_1_0(
                data["SupportedChannels"]
            )
        )
    else:
        raise DeserializationError(
            "NotifyCountryInformation.supported_channels required"
        )
    if "SupportedUseCases" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.notify_use_case_list

        out["supported_use_cases"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.notify_use_case_list.deserialize_aws_json_1_0(
                data["SupportedUseCases"]
            )
        )
    else:
        raise DeserializationError(
            "NotifyCountryInformation.supported_use_cases required"
        )
    if "SupportedTiers" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.notify_tier_list

        out["supported_tiers"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.notify_tier_list.deserialize_aws_json_1_0(
                data["SupportedTiers"]
            )
        )
    else:
        raise DeserializationError("NotifyCountryInformation.supported_tiers required")
    if "CustomerOwnedIdentityRequired" in data:
        out["customer_owned_identity_required"] = data["CustomerOwnedIdentityRequired"]
    else:
        out["customer_owned_identity_required"] = False
    return out
