"""Generated from Smithy shape ``com.amazonaws.apprunner#UpdateDefaultAutoScalingConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.auto_scaling_configuration


class UpdateDefaultAutoScalingConfigurationResponse(TypedDict):
    auto_scaling_configuration: (
        "aws_sdk_apprunner.types.auto_scaling_configuration.AutoScalingConfiguration"
    )
    """<p>A description of the App Runner auto scaling configuration that was set as default.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: UpdateDefaultAutoScalingConfigurationResponse,
) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.auto_scaling_configuration

    out["AutoScalingConfiguration"] = (
        aws_sdk_apprunner.types.auto_scaling_configuration.serialize_aws_json_1_0(
            value["auto_scaling_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> UpdateDefaultAutoScalingConfigurationResponse:
    out: UpdateDefaultAutoScalingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "AutoScalingConfiguration" in data:
        import aws_sdk_apprunner.types.auto_scaling_configuration

        out["auto_scaling_configuration"] = (
            aws_sdk_apprunner.types.auto_scaling_configuration.deserialize_aws_json_1_0(
                data["AutoScalingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDefaultAutoScalingConfigurationResponse.auto_scaling_configuration required"
        )
    return out
