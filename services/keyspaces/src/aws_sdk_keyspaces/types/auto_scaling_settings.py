"""Generated from Smithy shape ``com.amazonaws.keyspaces#AutoScalingSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.auto_scaling_policy
    import aws_sdk_keyspaces.types.boolean_object
    import aws_sdk_keyspaces.types.capacity_units


class AutoScalingSettings(TypedDict):
    auto_scaling_disabled: "aws_sdk_keyspaces.types.boolean_object.BooleanObject"
    """<p>This optional parameter enables auto scaling for the table if set to <code>false</code>.</p>"""
    minimum_units: NotRequired["aws_sdk_keyspaces.types.capacity_units.CapacityUnits"]
    """<p>The minimum level of throughput the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).</p>"""
    maximum_units: NotRequired["aws_sdk_keyspaces.types.capacity_units.CapacityUnits"]
    """<p>Manage costs by specifying the maximum amount of throughput to provision. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).</p>"""
    scaling_policy: NotRequired[
        "aws_sdk_keyspaces.types.auto_scaling_policy.AutoScalingPolicy"
    ]
    """<p>Amazon Keyspaces supports the <code>target tracking</code> auto scaling policy. With this policy, Amazon Keyspaces auto scaling ensures that the table's ratio of consumed to provisioned capacity stays at or near the target value that you specify. You define the target value as a percentage between 20 and 90.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingSettings) -> dict:
    out: dict = {}
    out["autoScalingDisabled"] = value.get("auto_scaling_disabled", False)
    if "minimum_units" in value:
        out["minimumUnits"] = value["minimum_units"]
    if "maximum_units" in value:
        out["maximumUnits"] = value["maximum_units"]
    if "scaling_policy" in value:
        import aws_sdk_keyspaces.types.auto_scaling_policy

        out["scalingPolicy"] = (
            aws_sdk_keyspaces.types.auto_scaling_policy.serialize_aws_json_1_0(
                value["scaling_policy"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutoScalingSettings:
    out: AutoScalingSettings = {}  # type: ignore[typeddict-item]
    if "autoScalingDisabled" in data:
        out["auto_scaling_disabled"] = data["autoScalingDisabled"]
    else:
        out["auto_scaling_disabled"] = False
    if "minimumUnits" in data:
        out["minimum_units"] = data["minimumUnits"]
    if "maximumUnits" in data:
        out["maximum_units"] = data["maximumUnits"]
    if "scalingPolicy" in data:
        import aws_sdk_keyspaces.types.auto_scaling_policy

        out["scaling_policy"] = (
            aws_sdk_keyspaces.types.auto_scaling_policy.deserialize_aws_json_1_0(
                data["scalingPolicy"]
            )
        )
    return out
