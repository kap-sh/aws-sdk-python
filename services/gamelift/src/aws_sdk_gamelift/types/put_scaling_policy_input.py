"""Generated from Smithy shape ``com.amazonaws.gamelift#PutScalingPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.comparison_operator_type
    import aws_sdk_gamelift.types.double
    import aws_sdk_gamelift.types.fleet_id_or_arn
    import aws_sdk_gamelift.types.integer
    import aws_sdk_gamelift.types.metric_name
    import aws_sdk_gamelift.types.non_zero_and_max_string
    import aws_sdk_gamelift.types.policy_type
    import aws_sdk_gamelift.types.positive_integer
    import aws_sdk_gamelift.types.scaling_adjustment_type
    import aws_sdk_gamelift.types.target_configuration


class PutScalingPolicyInput(TypedDict):
    name: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A descriptive label that is associated with a fleet's scaling policy. Policy names do not need to be unique. A fleet can have only one scaling policy with the same name.</p>"""
    fleet_id: NotRequired["aws_sdk_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to apply this policy to. You can use either the fleet ID or ARN value. The fleet cannot be in any of the following statuses: ERROR or DELETING.</p>"""
    scaling_adjustment: NotRequired["aws_sdk_gamelift.types.integer.Integer"]
    """<p>Amount of adjustment to make, based on the scaling adjustment type.</p>"""
    scaling_adjustment_type: NotRequired[
        "aws_sdk_gamelift.types.scaling_adjustment_type.ScalingAdjustmentType"
    ]
    r"""<p>The type of adjustment to make to a fleet's instance count:</p> <ul> <li> <p> <b>ChangeInCapacity</b> -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.</p> </li> <li> <p> <b>ExactCapacity</b> -- set the instance count to the scaling adjustment value.</p> </li> <li> <p> <b>PercentChangeInCapacity</b> -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down; for example, a value of \"-10\" scales the fleet down by 10%.</p> </li> </ul>"""
    threshold: NotRequired["aws_sdk_gamelift.types.double.Double"]
    """<p>Metric value used to trigger a scaling event.</p>"""
    comparison_operator: NotRequired[
        "aws_sdk_gamelift.types.comparison_operator_type.ComparisonOperatorType"
    ]
    """<p>Comparison operator to use when measuring the metric against the threshold value.</p>"""
    evaluation_periods: NotRequired[
        "aws_sdk_gamelift.types.positive_integer.PositiveInteger"
    ]
    """<p>Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.</p>"""
    metric_name: NotRequired["aws_sdk_gamelift.types.metric_name.MetricName"]
    r"""<p>Name of the Amazon GameLift Servers-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see <a href=\"https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html\">Monitor Amazon GameLift Servers with Amazon CloudWatch</a>. </p> <ul> <li> <p> <b>ActivatingGameSessions</b> -- Game sessions in the process of being created.</p> </li> <li> <p> <b>ActiveGameSessions</b> -- Game sessions that are currently running.</p> </li> <li> <p> <b>ActiveInstances</b> -- Fleet instances that are currently running at least one game session.</p> </li> <li> <p> <b>AvailableGameSessions</b> -- Additional game sessions that fleet could host simultaneously, given current capacity.</p> </li> <li> <p> <b>AvailablePlayerSessions</b> -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.</p> </li> <li> <p> <b>CurrentPlayerSessions</b> -- Player slots in active game sessions that are being used by a player or are reserved for a player. </p> </li> <li> <p> <b>IdleInstances</b> -- Active instances that are currently hosting zero game sessions. </p> </li> <li> <p> <b>PercentAvailableGameSessions</b> -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.</p> </li> <li> <p> <b>PercentIdleInstances</b> -- Percentage of the total number of active instances that are hosting zero game sessions.</p> </li> <li> <p> <b>QueueDepth</b> -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.</p> </li> <li> <p> <b>WaitTime</b> -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination. </p> </li> </ul>"""
    policy_type: NotRequired["aws_sdk_gamelift.types.policy_type.PolicyType"]
    """<p>The type of scaling policy to create. For a target-based policy, set the parameter <i>MetricName</i> to 'PercentAvailableGameSessions' and specify a <i>TargetConfiguration</i>. For a rule-based policy set the following parameters: <i>MetricName</i>, <i>ComparisonOperator</i>, <i>Threshold</i>, <i>EvaluationPeriods</i>, <i>ScalingAdjustmentType</i>, and <i>ScalingAdjustment</i>.</p>"""
    target_configuration: NotRequired[
        "aws_sdk_gamelift.types.target_configuration.TargetConfiguration"
    ]
    """<p>An object that contains settings for a target-based scaling policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutScalingPolicyInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "scaling_adjustment" in value:
        out["ScalingAdjustment"] = value["scaling_adjustment"]
    if "scaling_adjustment_type" in value:
        import aws_sdk_gamelift.types.scaling_adjustment_type

        out["ScalingAdjustmentType"] = (
            aws_sdk_gamelift.types.scaling_adjustment_type.serialize_aws_json_1_1(
                value["scaling_adjustment_type"]
            )
        )
    if "threshold" in value:
        out["Threshold"] = value["threshold"]
    if "comparison_operator" in value:
        import aws_sdk_gamelift.types.comparison_operator_type

        out["ComparisonOperator"] = (
            aws_sdk_gamelift.types.comparison_operator_type.serialize_aws_json_1_1(
                value["comparison_operator"]
            )
        )
    if "evaluation_periods" in value:
        out["EvaluationPeriods"] = value["evaluation_periods"]
    if "metric_name" in value:
        import aws_sdk_gamelift.types.metric_name

        out["MetricName"] = aws_sdk_gamelift.types.metric_name.serialize_aws_json_1_1(
            value["metric_name"]
        )
    if "policy_type" in value:
        import aws_sdk_gamelift.types.policy_type

        out["PolicyType"] = aws_sdk_gamelift.types.policy_type.serialize_aws_json_1_1(
            value["policy_type"]
        )
    if "target_configuration" in value:
        import aws_sdk_gamelift.types.target_configuration

        out["TargetConfiguration"] = (
            aws_sdk_gamelift.types.target_configuration.serialize_aws_json_1_1(
                value["target_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutScalingPolicyInput:
    out: PutScalingPolicyInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "ScalingAdjustment" in data:
        out["scaling_adjustment"] = data["ScalingAdjustment"]
    if "ScalingAdjustmentType" in data:
        import aws_sdk_gamelift.types.scaling_adjustment_type

        out["scaling_adjustment_type"] = (
            aws_sdk_gamelift.types.scaling_adjustment_type.deserialize_aws_json_1_1(
                data["ScalingAdjustmentType"]
            )
        )
    if "Threshold" in data:
        out["threshold"] = data["Threshold"]
    if "ComparisonOperator" in data:
        import aws_sdk_gamelift.types.comparison_operator_type

        out["comparison_operator"] = (
            aws_sdk_gamelift.types.comparison_operator_type.deserialize_aws_json_1_1(
                data["ComparisonOperator"]
            )
        )
    if "EvaluationPeriods" in data:
        out["evaluation_periods"] = data["EvaluationPeriods"]
    if "MetricName" in data:
        import aws_sdk_gamelift.types.metric_name

        out["metric_name"] = (
            aws_sdk_gamelift.types.metric_name.deserialize_aws_json_1_1(
                data["MetricName"]
            )
        )
    if "PolicyType" in data:
        import aws_sdk_gamelift.types.policy_type

        out["policy_type"] = (
            aws_sdk_gamelift.types.policy_type.deserialize_aws_json_1_1(
                data["PolicyType"]
            )
        )
    if "TargetConfiguration" in data:
        import aws_sdk_gamelift.types.target_configuration

        out["target_configuration"] = (
            aws_sdk_gamelift.types.target_configuration.deserialize_aws_json_1_1(
                data["TargetConfiguration"]
            )
        )
    return out
