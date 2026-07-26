"""Generated from Smithy shape ``com.amazonaws.apprunner#DescribeAutoScalingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import capo_apprunner.types.auto_scaling_configuration


class DescribeAutoScalingConfigurationResponse(TypedDict, closed=True):
    auto_scaling_configuration: (
        "capo_apprunner.types.auto_scaling_configuration.AutoScalingConfiguration"
    )
    """<p>A full description of the App Runner auto scaling configuration that you specified in this request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAutoScalingConfigurationResponse) -> dict:
    out: dict = {}
    import capo_apprunner.types.auto_scaling_configuration

    out["AutoScalingConfiguration"] = (
        capo_apprunner.types.auto_scaling_configuration.serialize_aws_json_1_0(
            value["auto_scaling_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAutoScalingConfigurationResponse:
    out: DescribeAutoScalingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "AutoScalingConfiguration" in data:
        import capo_apprunner.types.auto_scaling_configuration

        out["auto_scaling_configuration"] = (
            capo_apprunner.types.auto_scaling_configuration.deserialize_aws_json_1_0(
                data["AutoScalingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAutoScalingConfigurationResponse.auto_scaling_configuration required"
        )
    return out
