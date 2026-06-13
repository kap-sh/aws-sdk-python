"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateConfigurationSetResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name
    import aws_sdk_pinpoint_sms_voice_v2.types.tag_list


class CreateConfigurationSetResult(TypedDict):
    configuration_set_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the newly created configuration set.</p>"""
    configuration_set_name: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The name of the new configuration set.</p>"""
    tags: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of key and value pair tags that's associated with the configuration set.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The time when the configuration set was created, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateConfigurationSetResult) -> dict:
    out: dict = {}
    if "configuration_set_arn" in value:
        out["ConfigurationSetArn"] = value["configuration_set_arn"]
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "tags" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    if "created_timestamp" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateConfigurationSetResult:
    out: CreateConfigurationSetResult = {}  # type: ignore[typeddict-item]
    if "ConfigurationSetArn" in data:
        out["configuration_set_arn"] = data["ConfigurationSetArn"]
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if "Tags" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    return out
