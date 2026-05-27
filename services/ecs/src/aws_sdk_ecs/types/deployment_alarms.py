"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentAlarms``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.string_list


class DeploymentAlarms(TypedDict):
    alarm_names: "aws_sdk_ecs.types.string_list.StringList"
    """<p>One or more CloudWatch alarm names. Use a \",\" to separate the alarms.</p>"""
    rollback: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether to configure Amazon ECS to roll back the service if a service deployment fails. If rollback is used, when a service deployment fails, the service is rolled back to the last deployment that completed successfully.</p>"""
    enable: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether to use the CloudWatch alarm option in the service deployment process.</p>"""
