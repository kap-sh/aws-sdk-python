"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteAccountSettingRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.setting_name
    import aws_sdk_ecs.types.string


class DeleteAccountSettingRequest(TypedDict):
    name: "aws_sdk_ecs.types.setting_name.SettingName"
    """<p>The resource name to disable the account setting for. If <code>serviceLongArnFormat</code> is specified, the ARN for your Amazon ECS services is affected. If <code>taskLongArnFormat</code> is specified, the ARN and resource ID for your Amazon ECS tasks is affected. If <code>containerInstanceLongArnFormat</code> is specified, the ARN and resource ID for your Amazon ECS container instances is affected. If <code>awsvpcTrunking</code> is specified, the ENI limit for your Amazon ECS container instances is affected.</p>"""
    principal_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the principal. It can be a user, role, or the root user. If you specify the root user, it disables the account setting for all users, roles, and the root user of the account unless a user or role explicitly overrides these settings. If this field is omitted, the setting is changed only for the authenticated user.</p> <p>In order to use this parameter, you must be the root user, or the principal.</p>"""
