"""Generated from Smithy shape ``com.amazonaws.apprunner#ObservabilityConfigurationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.integer
    import aws_sdk_apprunner.types.observability_configuration_name


class ObservabilityConfigurationSummary(TypedDict):
    observability_configuration_arn: NotRequired[
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of this observability configuration.</p>"""
    observability_configuration_name: NotRequired[
        "aws_sdk_apprunner.types.observability_configuration_name.ObservabilityConfigurationName"
    ]
    """<p>The customer-provided observability configuration name. It can be used in multiple revisions of a configuration.</p>"""
    observability_configuration_revision: "aws_sdk_apprunner.types.integer.Integer"
    """<p>The revision of this observability configuration. It's unique among all the active configurations (<code>\"Status\": \"ACTIVE\"</code>) that share the same <code>ObservabilityConfigurationName</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ObservabilityConfigurationSummary) -> dict:
    out: dict = {}
    if "observability_configuration_arn" in value:
        out["ObservabilityConfigurationArn"] = value["observability_configuration_arn"]
    if "observability_configuration_name" in value:
        out["ObservabilityConfigurationName"] = value[
            "observability_configuration_name"
        ]
    out["ObservabilityConfigurationRevision"] = value.get(
        "observability_configuration_revision", 0
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ObservabilityConfigurationSummary:
    out: ObservabilityConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "ObservabilityConfigurationArn" in data:
        out["observability_configuration_arn"] = data["ObservabilityConfigurationArn"]
    if "ObservabilityConfigurationName" in data:
        out["observability_configuration_name"] = data["ObservabilityConfigurationName"]
    if "ObservabilityConfigurationRevision" in data:
        out["observability_configuration_revision"] = data[
            "ObservabilityConfigurationRevision"
        ]
    else:
        out["observability_configuration_revision"] = 0
    return out
