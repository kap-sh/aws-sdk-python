"""Generated from Smithy shape ``com.amazonaws.dynamodb#AutoScalingSettingsUpdate``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_policy_update
    import aws_sdk_dynamodb.types.auto_scaling_role_arn
    import aws_sdk_dynamodb.types.boolean_object
    import aws_sdk_dynamodb.types.positive_long_object


class AutoScalingSettingsUpdate(TypedDict):
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
    auto_scaling_role_arn: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_role_arn.AutoScalingRoleArn"
    ]
    """<p>Role ARN used for configuring auto scaling policy.</p>"""
    scaling_policy_update: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_policy_update.AutoScalingPolicyUpdate"
    ]
    """<p>The scaling policy to apply for scaling target global table or global secondary index capacity units.</p>"""
