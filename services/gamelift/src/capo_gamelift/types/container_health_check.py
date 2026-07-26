"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerHealthCheck``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.container_command_string_list
    import capo_gamelift.types.container_health_check_interval
    import capo_gamelift.types.container_health_check_retries
    import capo_gamelift.types.container_health_check_start_period
    import capo_gamelift.types.container_health_check_timeout


class ContainerHealthCheck(TypedDict, closed=True):
    command: NotRequired[
        "capo_gamelift.types.container_command_string_list.ContainerCommandStringList"
    ]
    """<p>A string array that specifies the command that the container runs to determine if it's healthy.</p>"""
    interval: NotRequired[
        "capo_gamelift.types.container_health_check_interval.ContainerHealthCheckInterval"
    ]
    """<p>The time period (in seconds) between each health check.</p>"""
    retries: NotRequired[
        "capo_gamelift.types.container_health_check_retries.ContainerHealthCheckRetries"
    ]
    """<p>The number of times to retry a failed health check before flagging the container unhealthy. The first run of the command does not count as a retry.</p>"""
    start_period: NotRequired[
        "capo_gamelift.types.container_health_check_start_period.ContainerHealthCheckStartPeriod"
    ]
    """<p>The optional grace period (in seconds) to give a container time to bootstrap before the first failed health check counts toward the number of retries.</p>"""
    timeout: NotRequired[
        "capo_gamelift.types.container_health_check_timeout.ContainerHealthCheckTimeout"
    ]
    """<p>The time period (in seconds) to wait for a health check to succeed before counting a failed health check. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerHealthCheck) -> dict:
    out: dict = {}
    if "command" in value:
        import capo_gamelift.types.container_command_string_list

        out["Command"] = (
            capo_gamelift.types.container_command_string_list.serialize_aws_json_1_1(
                value["command"]
            )
        )
    if "interval" in value:
        out["Interval"] = value["interval"]
    if "retries" in value:
        out["Retries"] = value["retries"]
    if "start_period" in value:
        out["StartPeriod"] = value["start_period"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerHealthCheck:
    out: ContainerHealthCheck = {}  # type: ignore[typeddict-item]
    if "Command" in data:
        import capo_gamelift.types.container_command_string_list

        out["command"] = (
            capo_gamelift.types.container_command_string_list.deserialize_aws_json_1_1(
                data["Command"]
            )
        )
    if "Interval" in data:
        out["interval"] = data["Interval"]
    if "Retries" in data:
        out["retries"] = data["Retries"]
    if "StartPeriod" in data:
        out["start_period"] = data["StartPeriod"]
    if "Timeout" in data:
        out["timeout"] = data["Timeout"]
    return out
