"""Generated from Smithy shape ``com.amazonaws.ecs#HealthCheck``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.string_list


class HealthCheck(TypedDict):
    command: "aws_sdk_ecs.types.string_list.StringList"
    """<p>A string array representing the command that the container runs to determine if it is healthy. The string array must start with <code>CMD</code> to run the command arguments directly, or <code>CMD-SHELL</code> to run the command with the container's default shell. </p> <p> When you use the Amazon Web Services Management Console JSON panel, the Command Line Interface, or the APIs, enclose the list of commands in double quotes and brackets.</p> <p> <code>[ \"CMD-SHELL\", \"curl -f http://localhost/ || exit 1\" ]</code> </p> <p>You don't include the double quotes and brackets when you use the Amazon Web Services Management Console.</p> <p> <code> CMD-SHELL, curl -f http://localhost/ || exit 1</code> </p> <p>An exit code of 0 indicates success, and non-zero exit code indicates failure. For more information, see <code>HealthCheck</code> in the docker container create command.</p>"""
    interval: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The time period in seconds between each health check execution. You may specify between 5 and 300 seconds. The default value is 30 seconds. This value applies only when you specify a <code>command</code>. </p>"""
    timeout: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The time period in seconds to wait for a health check to succeed before it is considered a failure. You may specify between 2 and 60 seconds. The default value is 5. This value applies only when you specify a <code>command</code>. </p>"""
    retries: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The number of times to retry a failed health check before the container is considered unhealthy. You may specify between 1 and 10 retries. The default value is 3. This value applies only when you specify a <code>command</code>. </p>"""
    start_period: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The optional grace period to provide containers time to bootstrap before failed health checks count towards the maximum number of retries. You can specify between 0 and 300 seconds. By default, the <code>startPeriod</code> is off. This value applies only when you specify a <code>command</code>. </p> <note> <p>If a health check succeeds within the <code>startPeriod</code>, then the container is considered healthy and any subsequent failures count toward the maximum number of retries.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HealthCheck) -> dict:
    out: dict = {}
    import aws_sdk_ecs.types.string_list

    out["command"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
        value["command"]
    )
    if "interval" in value:
        out["interval"] = value["interval"]
    if "timeout" in value:
        out["timeout"] = value["timeout"]
    if "retries" in value:
        out["retries"] = value["retries"]
    if "start_period" in value:
        out["startPeriod"] = value["start_period"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HealthCheck:
    out: HealthCheck = {}  # type: ignore[typeddict-item]
    if "command" in data:
        import aws_sdk_ecs.types.string_list

        out["command"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["command"]
        )
    else:
        raise DeserializationError("HealthCheck.command required")
    if "interval" in data:
        out["interval"] = data["interval"]
    if "timeout" in data:
        out["timeout"] = data["timeout"]
    if "retries" in data:
        out["retries"] = data["retries"]
    if "startPeriod" in data:
        out["start_period"] = data["startPeriod"]
    return out
