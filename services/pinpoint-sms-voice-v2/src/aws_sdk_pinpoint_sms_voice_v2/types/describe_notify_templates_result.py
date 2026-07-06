"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeNotifyTemplatesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_template_information_list


class DescribeNotifyTemplatesResult(TypedDict, closed=True):
    notify_templates: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.notify_template_information_list.NotifyTemplateInformationList"
    ]
    """<p>An array of NotifyTemplateInformation objects that contain the results.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. If this field is empty then there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeNotifyTemplatesResult) -> dict:
    out: dict = {}
    if "notify_templates" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.notify_template_information_list

        out["NotifyTemplates"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.notify_template_information_list.serialize_aws_json_1_0(
                value["notify_templates"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeNotifyTemplatesResult:
    out: DescribeNotifyTemplatesResult = {}  # type: ignore[typeddict-item]
    if "NotifyTemplates" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.notify_template_information_list

        out["notify_templates"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.notify_template_information_list.deserialize_aws_json_1_0(
                data["NotifyTemplates"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
