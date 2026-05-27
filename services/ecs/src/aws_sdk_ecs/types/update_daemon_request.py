"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateDaemonRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.daemon_deployment_configuration
    import aws_sdk_ecs.types.daemon_propagate_tags
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class UpdateDaemonRequest(TypedDict):
    daemon_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the daemon to update.</p>"""
    daemon_task_definition_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the daemon task definition to use for the updated daemon.</p>"""
    capacity_provider_arns: "aws_sdk_ecs.types.string_list.StringList"
    """<p>The Amazon Resource Names (ARNs) of the capacity providers to associate with the daemon.</p>"""
    deployment_configuration: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_configuration.DaemonDeploymentConfiguration"
    ]
    """<p>Optional deployment parameters that control how the daemon rolls out updates, including the drain percentage, alarm-based rollback, and bake time.</p>"""
    propagate_tags: NotRequired[
        "aws_sdk_ecs.types.daemon_propagate_tags.DaemonPropagateTags"
    ]
    """<p>Specifies whether to propagate the tags from the daemon to the daemon tasks. If you don't specify a value, the tags aren't propagated. You can only propagate tags to daemon tasks during task creation.</p>"""
    enable_ecs_managed_tags: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Specifies whether to turn on Amazon ECS managed tags for the tasks in the daemon. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html\">Tagging your Amazon ECS resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    enable_execute_command: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>If <code>true</code>, the execute command functionality is turned on for all tasks in the daemon. If <code>false</code>, the execute command functionality is turned off.</p>"""
