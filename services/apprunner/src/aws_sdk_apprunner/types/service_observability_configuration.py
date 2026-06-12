"""Generated from Smithy shape ``com.amazonaws.apprunner#ServiceObservabilityConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.boolean


class ServiceObservabilityConfiguration(TypedDict):
    observability_enabled: "aws_sdk_apprunner.types.boolean.Boolean"
    """<p>When <code>true</code>, an observability configuration resource is associated with the service, and an <code>ObservabilityConfigurationArn</code> is specified.</p>"""
    observability_configuration_arn: NotRequired[
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the observability configuration that is associated with the service. Specified only when <code>ObservabilityEnabled</code> is <code>true</code>.</p> <p>Specify an ARN with a name and a revision number to associate that revision. For example: <code>arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing/3</code> </p> <p>Specify just the name to associate the latest revision. For example: <code>arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceObservabilityConfiguration) -> dict:
    out: dict = {}
    out["ObservabilityEnabled"] = value.get("observability_enabled", False)
    if "observability_configuration_arn" in value:
        out["ObservabilityConfigurationArn"] = value["observability_configuration_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceObservabilityConfiguration:
    out: ServiceObservabilityConfiguration = {}  # type: ignore[typeddict-item]
    if "ObservabilityEnabled" in data:
        out["observability_enabled"] = data["ObservabilityEnabled"]
    else:
        out["observability_enabled"] = False
    if "ObservabilityConfigurationArn" in data:
        out["observability_configuration_arn"] = data["ObservabilityConfigurationArn"]
    return out
