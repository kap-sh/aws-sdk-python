"""Generated from Smithy shape ``com.amazonaws.dynamodb#AutoScalingSettingsUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.auto_scaling_policy_update
    import capo_dynamodb.types.auto_scaling_role_arn
    import capo_dynamodb.types.boolean_object
    import capo_dynamodb.types.positive_long_object


class AutoScalingSettingsUpdate(TypedDict, closed=True):
    minimum_units: NotRequired[
        "capo_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The minimum capacity units that a global table or global secondary index should be scaled down to.</p>"""
    maximum_units: NotRequired[
        "capo_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The maximum capacity units that a global table or global secondary index should be scaled up to.</p>"""
    auto_scaling_disabled: NotRequired[
        "capo_dynamodb.types.boolean_object.BooleanObject"
    ]
    """<p>Disabled auto scaling for this global table or global secondary index.</p>"""
    auto_scaling_role_arn: NotRequired[
        "capo_dynamodb.types.auto_scaling_role_arn.AutoScalingRoleArn"
    ]
    """<p>Role ARN used for configuring auto scaling policy.</p>"""
    scaling_policy_update: NotRequired[
        "capo_dynamodb.types.auto_scaling_policy_update.AutoScalingPolicyUpdate"
    ]
    """<p>The scaling policy to apply for scaling target global table or global secondary index capacity units.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingSettingsUpdate) -> dict:
    out: dict = {}
    if "minimum_units" in value:
        out["MinimumUnits"] = value["minimum_units"]
    if "maximum_units" in value:
        out["MaximumUnits"] = value["maximum_units"]
    if "auto_scaling_disabled" in value:
        out["AutoScalingDisabled"] = value["auto_scaling_disabled"]
    if "auto_scaling_role_arn" in value:
        out["AutoScalingRoleArn"] = value["auto_scaling_role_arn"]
    if "scaling_policy_update" in value:
        import capo_dynamodb.types.auto_scaling_policy_update

        out["ScalingPolicyUpdate"] = (
            capo_dynamodb.types.auto_scaling_policy_update.serialize_aws_json_1_0(
                value["scaling_policy_update"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutoScalingSettingsUpdate:
    out: AutoScalingSettingsUpdate = {}  # type: ignore[typeddict-item]
    if data.get("MinimumUnits") is not None:
        out["minimum_units"] = data["MinimumUnits"]
    if data.get("MaximumUnits") is not None:
        out["maximum_units"] = data["MaximumUnits"]
    if data.get("AutoScalingDisabled") is not None:
        out["auto_scaling_disabled"] = data["AutoScalingDisabled"]
    if data.get("AutoScalingRoleArn") is not None:
        out["auto_scaling_role_arn"] = data["AutoScalingRoleArn"]
    if data.get("ScalingPolicyUpdate") is not None:
        import capo_dynamodb.types.auto_scaling_policy_update

        out["scaling_policy_update"] = (
            capo_dynamodb.types.auto_scaling_policy_update.deserialize_aws_json_1_0(
                data["ScalingPolicyUpdate"]
            )
        )
    return out
