"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean


class AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails(TypedDict):
    enable: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether to enable the deployment circuit breaker logic for the service.</p>"""
    rollback: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether to roll back the service if a service deployment fails. If rollback is enabled, when a service deployment fails, the service is rolled back to the last deployment that completed successfully.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails,
) -> dict:
    out: dict = {}
    if "enable" in value:
        out["Enable"] = value["enable"]
    if "rollback" in value:
        out["Rollback"] = value["rollback"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails:
    out: AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails = {}  # type: ignore[typeddict-item]
    if "Enable" in data:
        out["enable"] = data["Enable"]
    if "Rollback" in data:
        out["rollback"] = data["Rollback"]
    return out
