"""Generated from Smithy shape ``com.amazonaws.apprunner#HealthCheckConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.health_check_healthy_threshold
    import aws_sdk_apprunner.types.health_check_interval
    import aws_sdk_apprunner.types.health_check_path
    import aws_sdk_apprunner.types.health_check_protocol
    import aws_sdk_apprunner.types.health_check_timeout
    import aws_sdk_apprunner.types.health_check_unhealthy_threshold


class HealthCheckConfiguration(TypedDict, closed=True):
    protocol: NotRequired[
        "aws_sdk_apprunner.types.health_check_protocol.HealthCheckProtocol"
    ]
    """<p>The IP protocol that App Runner uses to perform health checks for your service.</p> <p>If you set <code>Protocol</code> to <code>HTTP</code>, App Runner sends health check requests to the HTTP path specified by <code>Path</code>.</p> <p>Default: <code>TCP</code> </p>"""
    path: NotRequired["aws_sdk_apprunner.types.health_check_path.HealthCheckPath"]
    r"""<p>The URL that health check requests are sent to.</p> <p> <code>Path</code> is only applicable when you set <code>Protocol</code> to <code>HTTP</code>.</p> <p>Default: <code>\"/\"</code> </p>"""
    interval: NotRequired[
        "aws_sdk_apprunner.types.health_check_interval.HealthCheckInterval"
    ]
    """<p>The time interval, in seconds, between health checks.</p> <p>Default: <code>5</code> </p>"""
    timeout: NotRequired[
        "aws_sdk_apprunner.types.health_check_timeout.HealthCheckTimeout"
    ]
    """<p>The time, in seconds, to wait for a health check response before deciding it failed.</p> <p>Default: <code>2</code> </p>"""
    healthy_threshold: NotRequired[
        "aws_sdk_apprunner.types.health_check_healthy_threshold.HealthCheckHealthyThreshold"
    ]
    """<p>The number of consecutive checks that must succeed before App Runner decides that the service is healthy.</p> <p>Default: <code>1</code> </p>"""
    unhealthy_threshold: NotRequired[
        "aws_sdk_apprunner.types.health_check_unhealthy_threshold.HealthCheckUnhealthyThreshold"
    ]
    """<p>The number of consecutive checks that must fail before App Runner decides that the service is unhealthy.</p> <p>Default: <code>5</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HealthCheckConfiguration) -> dict:
    out: dict = {}
    if "protocol" in value:
        import aws_sdk_apprunner.types.health_check_protocol

        out["Protocol"] = (
            aws_sdk_apprunner.types.health_check_protocol.serialize_aws_json_1_0(
                value["protocol"]
            )
        )
    if "path" in value:
        out["Path"] = value["path"]
    if "interval" in value:
        out["Interval"] = value["interval"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "healthy_threshold" in value:
        out["HealthyThreshold"] = value["healthy_threshold"]
    if "unhealthy_threshold" in value:
        out["UnhealthyThreshold"] = value["unhealthy_threshold"]
    return out


def deserialize_aws_json_1_0(data: dict) -> HealthCheckConfiguration:
    out: HealthCheckConfiguration = {}  # type: ignore[typeddict-item]
    if "Protocol" in data:
        import aws_sdk_apprunner.types.health_check_protocol

        out["protocol"] = (
            aws_sdk_apprunner.types.health_check_protocol.deserialize_aws_json_1_0(
                data["Protocol"]
            )
        )
    if "Path" in data:
        out["path"] = data["Path"]
    if "Interval" in data:
        out["interval"] = data["Interval"]
    if "Timeout" in data:
        out["timeout"] = data["Timeout"]
    if "HealthyThreshold" in data:
        out["healthy_threshold"] = data["HealthyThreshold"]
    if "UnhealthyThreshold" in data:
        out["unhealthy_threshold"] = data["UnhealthyThreshold"]
    return out
