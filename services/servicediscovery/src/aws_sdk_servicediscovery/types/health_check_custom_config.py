"""Generated from Smithy shape ``com.amazonaws.servicediscovery#HealthCheckCustomConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.failure_threshold


class HealthCheckCustomConfig(TypedDict):
    failure_threshold: NotRequired[
        "aws_sdk_servicediscovery.types.failure_threshold.FailureThreshold"
    ]
    """<important> <p>This parameter is no longer supported and is always set to 1. Cloud Map waits for approximately 30 seconds after receiving an <code>UpdateInstanceCustomHealthStatus</code> request before changing the status of the service instance.</p> </important> <p>The number of 30-second intervals that you want Cloud Map to wait after receiving an <code>UpdateInstanceCustomHealthStatus</code> request before it changes the health status of a service instance.</p> <p>Sending a second or subsequent <code>UpdateInstanceCustomHealthStatus</code> request with the same value before 30 seconds has passed doesn't accelerate the change. Cloud Map still waits <code>30</code> seconds after the first request to make the change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HealthCheckCustomConfig) -> dict:
    out: dict = {}
    if "failure_threshold" in value:
        out["FailureThreshold"] = value["failure_threshold"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HealthCheckCustomConfig:
    out: HealthCheckCustomConfig = {}  # type: ignore[typeddict-item]
    if "FailureThreshold" in data:
        out["failure_threshold"] = data["FailureThreshold"]
    return out
