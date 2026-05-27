"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonAlarmConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.string_list


class DaemonAlarmConfiguration(TypedDict):
    alarm_names: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The CloudWatch alarm names to monitor during a daemon deployment.</p>"""
    enable: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether to use the CloudWatch alarm option in the daemon deployment process. The default value is <code>false</code>.</p>"""
