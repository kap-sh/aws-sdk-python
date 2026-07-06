"""Generated from Smithy shape ``com.amazonaws.supportapp#CreateSlackChannelConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_support_app.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support_app.types.boolean_value
    import aws_sdk_support_app.types.channel_id
    import aws_sdk_support_app.types.channel_name
    import aws_sdk_support_app.types.notification_severity_level
    import aws_sdk_support_app.types.role_arn
    import aws_sdk_support_app.types.team_id


class CreateSlackChannelConfigurationRequest(TypedDict, closed=True):
    team_id: "aws_sdk_support_app.types.team_id.teamId"
    """<p>The team ID in Slack. This ID uniquely identifies a Slack workspace, such as <code>T012ABCDEFG</code>.</p>"""
    channel_id: "aws_sdk_support_app.types.channel_id.channelId"
    """<p>The channel ID in Slack. This ID identifies a channel within a Slack workspace.</p>"""
    channel_name: NotRequired["aws_sdk_support_app.types.channel_name.channelName"]
    """<p>The name of the Slack channel that you configure for the Amazon Web Services Support App.</p>"""
    notify_on_create_or_reopen_case: NotRequired[
        "aws_sdk_support_app.types.boolean_value.booleanValue"
    ]
    """<p>Whether you want to get notified when a support case is created or reopened.</p>"""
    notify_on_add_correspondence_to_case: NotRequired[
        "aws_sdk_support_app.types.boolean_value.booleanValue"
    ]
    """<p>Whether you want to get notified when a support case has a new correspondence.</p>"""
    notify_on_resolve_case: NotRequired[
        "aws_sdk_support_app.types.boolean_value.booleanValue"
    ]
    """<p>Whether you want to get notified when a support case is resolved.</p>"""
    notify_on_case_severity: "aws_sdk_support_app.types.notification_severity_level.NotificationSeverityLevel"
    """<p>The case severity for a support case that you want to receive notifications.</p> <p>If you specify <code>high</code> or <code>all</code>, you must specify <code>true</code> for at least one of the following parameters:</p> <ul> <li> <p> <code>notifyOnAddCorrespondenceToCase</code> </p> </li> <li> <p> <code>notifyOnCreateOrReopenCase</code> </p> </li> <li> <p> <code>notifyOnResolveCase</code> </p> </li> </ul> <p>If you specify <code>none</code>, the following parameters must be null or <code>false</code>:</p> <ul> <li> <p> <code>notifyOnAddCorrespondenceToCase</code> </p> </li> <li> <p> <code>notifyOnCreateOrReopenCase</code> </p> </li> <li> <p> <code>notifyOnResolveCase</code> </p> </li> </ul> <note> <p>If you don't specify these parameters in your request, they default to <code>false</code>.</p> </note>"""
    channel_role_arn: "aws_sdk_support_app.types.role_arn.roleArn"
    r"""<p>The Amazon Resource Name (ARN) of an IAM role that you want to use to perform operations on Amazon Web Services. For more information, see <a href=\"https://docs.aws.amazon.com/awssupport/latest/user/support-app-permissions.html\">Managing access to the Amazon Web Services Support App</a> in the <i>Amazon Web Services Support User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSlackChannelConfigurationRequest) -> dict:
    out: dict = {}
    out["teamId"] = value["team_id"]
    out["channelId"] = value["channel_id"]
    if "channel_name" in value:
        out["channelName"] = value["channel_name"]
    if "notify_on_create_or_reopen_case" in value:
        out["notifyOnCreateOrReopenCase"] = value["notify_on_create_or_reopen_case"]
    if "notify_on_add_correspondence_to_case" in value:
        out["notifyOnAddCorrespondenceToCase"] = value[
            "notify_on_add_correspondence_to_case"
        ]
    if "notify_on_resolve_case" in value:
        out["notifyOnResolveCase"] = value["notify_on_resolve_case"]
    out["notifyOnCaseSeverity"] = value["notify_on_case_severity"]
    out["channelRoleArn"] = value["channel_role_arn"]
    return out


def deserialize_json(data: dict) -> CreateSlackChannelConfigurationRequest:
    out: CreateSlackChannelConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "teamId" in data:
        out["team_id"] = data["teamId"]
    else:
        raise DeserializationError(
            "CreateSlackChannelConfigurationRequest.team_id required"
        )
    if "channelId" in data:
        out["channel_id"] = data["channelId"]
    else:
        raise DeserializationError(
            "CreateSlackChannelConfigurationRequest.channel_id required"
        )
    if "channelName" in data:
        out["channel_name"] = data["channelName"]
    if "notifyOnCreateOrReopenCase" in data:
        out["notify_on_create_or_reopen_case"] = data["notifyOnCreateOrReopenCase"]
    if "notifyOnAddCorrespondenceToCase" in data:
        out["notify_on_add_correspondence_to_case"] = data[
            "notifyOnAddCorrespondenceToCase"
        ]
    if "notifyOnResolveCase" in data:
        out["notify_on_resolve_case"] = data["notifyOnResolveCase"]
    if "notifyOnCaseSeverity" in data:
        out["notify_on_case_severity"] = data["notifyOnCaseSeverity"]
    else:
        raise DeserializationError(
            "CreateSlackChannelConfigurationRequest.notify_on_case_severity required"
        )
    if "channelRoleArn" in data:
        out["channel_role_arn"] = data["channelRoleArn"]
    else:
        raise DeserializationError(
            "CreateSlackChannelConfigurationRequest.channel_role_arn required"
        )
    return out
