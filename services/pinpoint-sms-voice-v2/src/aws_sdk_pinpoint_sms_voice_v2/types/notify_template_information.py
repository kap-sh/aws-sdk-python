"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyTemplateInformation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_tier_list
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_language_code
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_template_id
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_template_status
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_template_type
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_template_version
    import aws_sdk_pinpoint_sms_voice_v2.types.number_capability_list
    import aws_sdk_pinpoint_sms_voice_v2.types.template_content
    import aws_sdk_pinpoint_sms_voice_v2.types.template_variables_map
    import aws_sdk_pinpoint_sms_voice_v2.types.voice_id_list


class NotifyTemplateInformation(TypedDict):
    template_id: (
        "aws_sdk_pinpoint_sms_voice_v2.types.notify_template_id.NotifyTemplateId"
    )
    """<p>The unique identifier for the template.</p>"""
    version: "aws_sdk_pinpoint_sms_voice_v2.types.notify_template_version.NotifyTemplateVersion"
    """<p>The version of the template.</p>"""
    template_type: (
        "aws_sdk_pinpoint_sms_voice_v2.types.notify_template_type.NotifyTemplateType"
    )
    """<p>The type of the template.</p>"""
    channels: "aws_sdk_pinpoint_sms_voice_v2.types.number_capability_list.NumberCapabilityList"
    """<p>The channels for the template. Supported values are <code>SMS</code> and <code>VOICE</code>.</p>"""
    tier_access: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_tier_list.NotifyConfigurationTierList"
    ]
    """<p>The tier access level for the template.</p>"""
    status: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.notify_template_status.NotifyTemplateStatus"
    ]
    """<p>The current status of the template.</p>"""
    supported_countries: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list.IsoCountryCodeList"
    ]
    """<p>An array of supported country codes for the template.</p>"""
    language_code: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.notify_language_code.NotifyLanguageCode"
    ]
    """<p>The language code for the template.</p>"""
    content: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.template_content.TemplateContent"
    ]
    """<p>The content of the template.</p>"""
    variables: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.template_variables_map.TemplateVariablesMap"
    ]
    """<p>An array of template variable metadata for the template.</p>"""
    supported_voice_ids: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.voice_id_list.VoiceIdList"
    ]
    """<p>An array of supported voice IDs for voice templates.</p>"""
    created_timestamp: "datetime.datetime"
    r"""<p>The time when the notify template was created, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotifyTemplateInformation) -> dict:
    out: dict = {}
    out["TemplateId"] = value["template_id"]
    out["Version"] = value["version"]
    out["TemplateType"] = value["template_type"]
    import aws_sdk_pinpoint_sms_voice_v2.types.number_capability_list

    out["Channels"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.number_capability_list.serialize_aws_json_1_0(
            value["channels"]
        )
    )
    if "tier_access" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_tier_list

        out["TierAccess"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_tier_list.serialize_aws_json_1_0(
                value["tier_access"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "supported_countries" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list

        out["SupportedCountries"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list.serialize_aws_json_1_0(
                value["supported_countries"]
            )
        )
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    if "content" in value:
        out["Content"] = value["content"]
    if "variables" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.template_variables_map

        out["Variables"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.template_variables_map.serialize_aws_json_1_0(
                value["variables"]
            )
        )
    if "supported_voice_ids" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.voice_id_list

        out["SupportedVoiceIds"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.voice_id_list.serialize_aws_json_1_0(
                value["supported_voice_ids"]
            )
        )
    import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> NotifyTemplateInformation:
    out: NotifyTemplateInformation = {}  # type: ignore[typeddict-item]
    if "TemplateId" in data:
        out["template_id"] = data["TemplateId"]
    else:
        raise DeserializationError("NotifyTemplateInformation.template_id required")
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        raise DeserializationError("NotifyTemplateInformation.version required")
    if "TemplateType" in data:
        out["template_type"] = data["TemplateType"]
    else:
        raise DeserializationError("NotifyTemplateInformation.template_type required")
    if "Channels" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.number_capability_list

        out["channels"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.number_capability_list.deserialize_aws_json_1_0(
                data["Channels"]
            )
        )
    else:
        raise DeserializationError("NotifyTemplateInformation.channels required")
    if "TierAccess" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_tier_list

        out["tier_access"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_tier_list.deserialize_aws_json_1_0(
                data["TierAccess"]
            )
        )
    if "Status" in data:
        out["status"] = data["Status"]
    if "SupportedCountries" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list

        out["supported_countries"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list.deserialize_aws_json_1_0(
                data["SupportedCountries"]
            )
        )
    if "LanguageCode" in data:
        out["language_code"] = data["LanguageCode"]
    if "Content" in data:
        out["content"] = data["Content"]
    if "Variables" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.template_variables_map

        out["variables"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.template_variables_map.deserialize_aws_json_1_0(
                data["Variables"]
            )
        )
    if "SupportedVoiceIds" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.voice_id_list

        out["supported_voice_ids"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.voice_id_list.deserialize_aws_json_1_0(
                data["SupportedVoiceIds"]
            )
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "NotifyTemplateInformation.created_timestamp required"
        )
    return out
