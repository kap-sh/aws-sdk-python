"""Generated from Smithy shape ``com.amazonaws.apprunner#UpdateDefaultAutoScalingConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn


class UpdateDefaultAutoScalingConfigurationRequest(TypedDict):
    auto_scaling_configuration_arn: (
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the App Runner auto scaling configuration that you want to set as the default.</p> <p>The ARN can be a full auto scaling configuration ARN, or a partial ARN ending with either <code>.../<i>name</i> </code> or <code>.../<i>name</i>/<i>revision</i> </code>. If a revision isn't specified, the latest active revision is set as the default.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateDefaultAutoScalingConfigurationRequest) -> dict:
    out: dict = {}
    out["AutoScalingConfigurationArn"] = value["auto_scaling_configuration_arn"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> UpdateDefaultAutoScalingConfigurationRequest:
    out: UpdateDefaultAutoScalingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "AutoScalingConfigurationArn" in data:
        out["auto_scaling_configuration_arn"] = data["AutoScalingConfigurationArn"]
    else:
        raise DeserializationError(
            "UpdateDefaultAutoScalingConfigurationRequest.auto_scaling_configuration_arn required"
        )
    return out
