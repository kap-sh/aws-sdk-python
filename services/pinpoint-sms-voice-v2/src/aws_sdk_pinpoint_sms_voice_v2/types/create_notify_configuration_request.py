"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateNotifyConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.client_token
    import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_display_name
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_use_case
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_template_id
    import aws_sdk_pinpoint_sms_voice_v2.types.pool_id_or_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.tag_list


class CreateNotifyConfigurationRequest(TypedDict):
    display_name: "aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_display_name.NotifyConfigurationDisplayName"
    """<p>The display name to associate with the notify configuration.</p>"""
    use_case: "aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_use_case.NotifyConfigurationUseCase"
    """<p>The use case for the notify configuration.</p>"""
    default_template_id: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.notify_template_id.NotifyTemplateId"
    ]
    """<p>The default template identifier to associate with the notify configuration. If specified, this template is used when sending messages without an explicit template identifier.</p>"""
    pool_id: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn"
    ]
    """<p>The identifier of the pool to associate with the notify configuration.</p>"""
    enabled_countries: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list.IsoCountryCodeList"
    ]
    """<p>An array of two-character ISO country codes, in ISO 3166-1 alpha-2 format, that are enabled for the notify configuration.</p>"""
    enabled_channels: "aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.NotifyEnabledChannelsList"
    """<p>An array of channels to enable for the notify configuration. Supported values include <code>SMS</code> and <code>VOICE</code>.</p>"""
    deletion_protection_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to true the notify configuration can't be deleted. You can change this value using the <a>UpdateNotifyConfiguration</a> action.</p>"""
    client_token: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""
    tags: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of tags (key and value pairs) associated with the notify configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateNotifyConfigurationRequest) -> dict:
    out: dict = {}
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
    if "deletion_protection_enabled" in value:
        out["DeletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateNotifyConfigurationRequest:
    out: CreateNotifyConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    else:
        raise DeserializationError(
            "CreateNotifyConfigurationRequest.display_name required"
        )
    if "UseCase" in data:
        out["use_case"] = data["UseCase"]
    else:
        raise DeserializationError("CreateNotifyConfigurationRequest.use_case required")
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
            "CreateNotifyConfigurationRequest.enabled_channels required"
        )
    if "DeletionProtectionEnabled" in data:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Tags" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    return out
