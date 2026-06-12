"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string_list


class AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails(TypedDict):
    command: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The command that the container runs to determine whether it is healthy.</p>"""
    interval: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The time period in seconds between each health check execution. The default value is 30 seconds.</p>"""
    retries: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of times to retry a failed health check before the container is considered unhealthy. The default value is 3.</p>"""
    start_period: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The optional grace period in seconds that allows containers time to bootstrap before failed health checks count towards the maximum number of retries.</p>"""
    timeout: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The time period in seconds to wait for a health check to succeed before it is considered a failure. The default value is 5.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails,
) -> dict:
    out: dict = {}
    if "command" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["Command"] = aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
            value["command"]
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


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails = {}  # type: ignore[typeddict-item]
    if "Command" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["command"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
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
