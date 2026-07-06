"""Generated from Smithy shape ``com.amazonaws.apprunner#CreateAutoScalingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.auto_scaling_configuration


class CreateAutoScalingConfigurationResponse(TypedDict, closed=True):
    auto_scaling_configuration: (
        "aws_sdk_apprunner.types.auto_scaling_configuration.AutoScalingConfiguration"
    )
    """<p>A description of the App Runner auto scaling configuration that's created by this request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAutoScalingConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.auto_scaling_configuration

    out["AutoScalingConfiguration"] = (
        aws_sdk_apprunner.types.auto_scaling_configuration.serialize_aws_json_1_0(
            value["auto_scaling_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAutoScalingConfigurationResponse:
    out: CreateAutoScalingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "AutoScalingConfiguration" in data:
        import aws_sdk_apprunner.types.auto_scaling_configuration

        out["auto_scaling_configuration"] = (
            aws_sdk_apprunner.types.auto_scaling_configuration.deserialize_aws_json_1_0(
                data["AutoScalingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAutoScalingConfigurationResponse.auto_scaling_configuration required"
        )
    return out
