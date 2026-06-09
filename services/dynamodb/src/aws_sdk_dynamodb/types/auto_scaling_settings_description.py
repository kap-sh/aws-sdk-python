"""Generated from Smithy shape ``com.amazonaws.dynamodb#AutoScalingSettingsDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_policy_description_list
    import aws_sdk_dynamodb.types.boolean_object
    import aws_sdk_dynamodb.types.positive_long_object
    import aws_sdk_dynamodb.types.string


class AutoScalingSettingsDescription(TypedDict):
    minimum_units: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The minimum capacity units that a global table or global secondary index should be scaled down to.</p>"""
    maximum_units: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The maximum capacity units that a global table or global secondary index should be scaled up to.</p>"""
    auto_scaling_disabled: NotRequired[
        "aws_sdk_dynamodb.types.boolean_object.BooleanObject"
    ]
    """<p>Disabled auto scaling for this global table or global secondary index.</p>"""
    auto_scaling_role_arn: NotRequired["aws_sdk_dynamodb.types.string.String"]
    """<p>Role ARN used for configuring the auto scaling policy.</p>"""
    scaling_policies: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_policy_description_list.AutoScalingPolicyDescriptionList"
    ]
    """<p>Information about the scaling policies.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingSettingsDescription) -> dict:
    out: dict = {}
    if "minimum_units" in value:
        out["MinimumUnits"] = value["minimum_units"]
    if "maximum_units" in value:
        out["MaximumUnits"] = value["maximum_units"]
    if "auto_scaling_disabled" in value:
        out["AutoScalingDisabled"] = value["auto_scaling_disabled"]
    if "auto_scaling_role_arn" in value:
        out["AutoScalingRoleArn"] = value["auto_scaling_role_arn"]
    if "scaling_policies" in value:
        import aws_sdk_dynamodb.types.auto_scaling_policy_description_list

        out["ScalingPolicies"] = (
            aws_sdk_dynamodb.types.auto_scaling_policy_description_list.serialize_aws_json_1_0(
                value["scaling_policies"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutoScalingSettingsDescription:
    out: AutoScalingSettingsDescription = {}  # type: ignore[typeddict-item]
    if "MinimumUnits" in data:
        out["minimum_units"] = data["MinimumUnits"]
    if "MaximumUnits" in data:
        out["maximum_units"] = data["MaximumUnits"]
    if "AutoScalingDisabled" in data:
        out["auto_scaling_disabled"] = data["AutoScalingDisabled"]
    if "AutoScalingRoleArn" in data:
        out["auto_scaling_role_arn"] = data["AutoScalingRoleArn"]
    if "ScalingPolicies" in data:
        import aws_sdk_dynamodb.types.auto_scaling_policy_description_list

        out["scaling_policies"] = (
            aws_sdk_dynamodb.types.auto_scaling_policy_description_list.deserialize_aws_json_1_0(
                data["ScalingPolicies"]
            )
        )
    return out
