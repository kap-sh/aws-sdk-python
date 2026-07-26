"""Generated from Smithy shape ``com.amazonaws.rtbfabric#AutoScalingGroupsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.auto_scaling_group_name_list
    import capo_rtbfabric.types.health_check_config


class AutoScalingGroupsConfiguration(TypedDict, closed=True):
    auto_scaling_group_names: (
        "capo_rtbfabric.types.auto_scaling_group_name_list.AutoScalingGroupNameList"
    )
    """<p>The names of the auto scaling group.</p>"""
    role_arn: "str"
    """<p>The role ARN of the auto scaling group.</p>"""
    health_check_config: NotRequired[
        "capo_rtbfabric.types.health_check_config.HealthCheckConfig"
    ]
    """<p>The health check configuration for the Auto Scaling group managed endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoScalingGroupsConfiguration) -> dict:
    out: dict = {}
    import capo_rtbfabric.types.auto_scaling_group_name_list

    out["autoScalingGroupNames"] = (
        capo_rtbfabric.types.auto_scaling_group_name_list.serialize_json(
            value["auto_scaling_group_names"]
        )
    )
    out["roleArn"] = value["role_arn"]
    if "health_check_config" in value:
        import capo_rtbfabric.types.health_check_config

        out["healthCheckConfig"] = (
            capo_rtbfabric.types.health_check_config.serialize_json(
                value["health_check_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutoScalingGroupsConfiguration:
    out: AutoScalingGroupsConfiguration = {}  # type: ignore[typeddict-item]
    if "autoScalingGroupNames" in data:
        import capo_rtbfabric.types.auto_scaling_group_name_list

        out["auto_scaling_group_names"] = (
            capo_rtbfabric.types.auto_scaling_group_name_list.deserialize_json(
                data["autoScalingGroupNames"]
            )
        )
    else:
        raise DeserializationError(
            "AutoScalingGroupsConfiguration.auto_scaling_group_names required"
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("AutoScalingGroupsConfiguration.role_arn required")
    if "healthCheckConfig" in data:
        import capo_rtbfabric.types.health_check_config

        out["health_check_config"] = (
            capo_rtbfabric.types.health_check_config.deserialize_json(
                data["healthCheckConfig"]
            )
        )
    return out
