"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerRestartPolicy``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_boolean
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.integer_list


class ContainerRestartPolicy(TypedDict):
    enabled: "aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"
    """<p>Specifies whether a restart policy is enabled for the container.</p>"""
    ignored_exit_codes: NotRequired["aws_sdk_ecs.types.integer_list.IntegerList"]
    """<p>A list of exit codes that Amazon ECS will ignore and not attempt a restart on. You can specify a maximum of 50 container exit codes. By default, Amazon ECS does not ignore any exit codes.</p>"""
    restart_attempt_period: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>A period of time (in seconds) that the container must run for before a restart can be attempted. A container can be restarted only once every <code>restartAttemptPeriod</code> seconds. If a container isn't able to run for this time period and exits early, it will not be restarted. You can set a minimum <code>restartAttemptPeriod</code> of 60 seconds and a maximum <code>restartAttemptPeriod</code> of 1800 seconds. By default, a container must run for 300 seconds before it can be restarted.</p>"""
