"""Generated from Smithy shape ``com.amazonaws.apprunner#DeleteAutoScalingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import capo_apprunner.types.auto_scaling_configuration


class DeleteAutoScalingConfigurationResponse(TypedDict, closed=True):
    auto_scaling_configuration: (
        "capo_apprunner.types.auto_scaling_configuration.AutoScalingConfiguration"
    )
    """<p>A description of the App Runner auto scaling configuration that this request just deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAutoScalingConfigurationResponse) -> dict:
    out: dict = {}
    import capo_apprunner.types.auto_scaling_configuration

    out["AutoScalingConfiguration"] = (
        capo_apprunner.types.auto_scaling_configuration.serialize_aws_json_1_0(
            value["auto_scaling_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAutoScalingConfigurationResponse:
    out: DeleteAutoScalingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "AutoScalingConfiguration" in data:
        import capo_apprunner.types.auto_scaling_configuration

        out["auto_scaling_configuration"] = (
            capo_apprunner.types.auto_scaling_configuration.deserialize_aws_json_1_0(
                data["AutoScalingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteAutoScalingConfigurationResponse.auto_scaling_configuration required"
        )
    return out
