"""Generated from Smithy shape ``com.amazonaws.ecs#Setting``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.setting_name
    import aws_sdk_ecs.types.setting_type
    import aws_sdk_ecs.types.string


class Setting(TypedDict):
    name: NotRequired["aws_sdk_ecs.types.setting_name.SettingName"]
    """<p>The Amazon ECS resource name.</p>"""
    value: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Determines whether the account setting is on or off for the specified resource.</p>"""
    principal_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the principal. It can be a user, role, or the root user. If this field is omitted, the authenticated user is assumed.</p>"""
    type: NotRequired["aws_sdk_ecs.types.setting_type.SettingType"]
    """<p>Indicates whether Amazon Web Services manages the account setting, or if the user manages it.</p> <p> <code>aws_managed</code> account settings are read-only, as Amazon Web Services manages such on the customer's behalf. Currently, the <code>guardDutyActivate</code> account setting is the only one Amazon Web Services manages.</p>"""
