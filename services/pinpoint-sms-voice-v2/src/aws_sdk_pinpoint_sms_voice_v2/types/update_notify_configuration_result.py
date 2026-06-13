"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#UpdateNotifyConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_display_name
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_id
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_status
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_tier
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_use_case
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_template_id
    import aws_sdk_pinpoint_sms_voice_v2.types.tier_upgrade_status


class UpdateNotifyConfigurationResult(TypedDict):
    notify_configuration_arn: "aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_arn.NotifyConfigurationArn"
    """<p>The Amazon Resource Name (ARN) for the notify configuration.</p>"""
    notify_configuration_id: "aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_id.NotifyConfigurationId"
    """<p>The unique identifier for the notify configuration.</p>"""
    display_name: "aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_display_name.NotifyConfigurationDisplayName"
    """<p>The display name associated with the notify configuration.</p>"""
    use_case: "aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_use_case.NotifyConfigurationUseCase"
    """<p>The use case for the notify configuration.</p>"""
    default_template_id: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.notify_template_id.NotifyTemplateId"
    ]
    """<p>The default template identifier associated with the notify configuration.</p>"""
    pool_id: NotRequired["str"]
    """<p>The identifier of the pool associated with the notify configuration.</p>"""
    enabled_countries: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list.IsoCountryCodeList"
    ]
    """<p>An array of two-character ISO country codes, in ISO 3166-1 alpha-2 format, that are enabled for the notify configuration.</p>"""
    enabled_channels: "aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.NotifyEnabledChannelsList"
    """<p>An array of channels enabled for the notify configuration. Supported values include <code>SMS</code> and <code>VOICE</code>.</p>"""
    tier: "aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_tier.NotifyConfigurationTier"
    """<p>The tier of the notify configuration.</p>"""
    tier_upgrade_status: (
        "aws_sdk_pinpoint_sms_voice_v2.types.tier_upgrade_status.TierUpgradeStatus"
    )
    """<p>The tier upgrade status of the notify configuration.</p>"""
    status: "aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_status.NotifyConfigurationStatus"
    """<p>The current status of the notify configuration.</p>"""
    rejection_reason: NotRequired["str"]
    """<p>The reason the notify configuration was rejected, if applicable.</p>"""
    deletion_protection_enabled: "bool"
    """<p>When set to true deletion protection is enabled. By default this is set to false. </p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the notify configuration was created, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateNotifyConfigurationResult) -> dict:
    out: dict = {}
    out["NotifyConfigurationArn"] = value["notify_configuration_arn"]
    out["NotifyConfigurationId"] = value["notify_configuration_id"]
    out["DisplayName"] = value["display_name"]
    out["UseCase"] = value["use_case"]
    if "default_template_id" in value:
        out["DefaultTemplateId"] = value["default_template_id"]
    if "pool_id" in value:
        out["PoolId"] = value["pool_id"]
    if "enabled_countries" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list

        out["EnabledCountries"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list.serialize_aws_json_1_0(
                value["enabled_countries"]
            )
        )
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list

    out["EnabledChannels"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.serialize_aws_json_1_0(
            value["enabled_channels"]
        )
    )
    out["Tier"] = value["tier"]
    out["TierUpgradeStatus"] = value["tier_upgrade_status"]
    out["Status"] = value["status"]
    if "rejection_reason" in value:
        out["RejectionReason"] = value["rejection_reason"]
    out["DeletionProtectionEnabled"] = value.get("deletion_protection_enabled", False)
    import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateNotifyConfigurationResult:
    out: UpdateNotifyConfigurationResult = {}  # type: ignore[typeddict-item]
    if "NotifyConfigurationArn" in data:
        out["notify_configuration_arn"] = data["NotifyConfigurationArn"]
    else:
        raise DeserializationError(
            "UpdateNotifyConfigurationResult.notify_configuration_arn required"
        )
    if "NotifyConfigurationId" in data:
        out["notify_configuration_id"] = data["NotifyConfigurationId"]
    else:
        raise DeserializationError(
            "UpdateNotifyConfigurationResult.notify_configuration_id required"
        )
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    else:
        raise DeserializationError(
            "UpdateNotifyConfigurationResult.display_name required"
        )
    if "UseCase" in data:
        out["use_case"] = data["UseCase"]
    else:
        raise DeserializationError("UpdateNotifyConfigurationResult.use_case required")
    if "DefaultTemplateId" in data:
        out["default_template_id"] = data["DefaultTemplateId"]
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
    if "EnabledCountries" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list

        out["enabled_countries"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list.deserialize_aws_json_1_0(
                data["EnabledCountries"]
            )
        )
    if "EnabledChannels" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list

        out["enabled_channels"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.deserialize_aws_json_1_0(
                data["EnabledChannels"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateNotifyConfigurationResult.enabled_channels required"
        )
    if "Tier" in data:
        out["tier"] = data["Tier"]
    else:
        raise DeserializationError("UpdateNotifyConfigurationResult.tier required")
    if "TierUpgradeStatus" in data:
        out["tier_upgrade_status"] = data["TierUpgradeStatus"]
    else:
        raise DeserializationError(
            "UpdateNotifyConfigurationResult.tier_upgrade_status required"
        )
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("UpdateNotifyConfigurationResult.status required")
    if "RejectionReason" in data:
        out["rejection_reason"] = data["RejectionReason"]
    if "DeletionProtectionEnabled" in data:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    else:
        out["deletion_protection_enabled"] = False
    if "CreatedTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateNotifyConfigurationResult.created_timestamp required"
        )
    return out
