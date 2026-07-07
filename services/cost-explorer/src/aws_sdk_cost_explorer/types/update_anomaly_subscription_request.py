"""Generated from Smithy shape ``com.amazonaws.costexplorer#UpdateAnomalySubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.anomaly_subscription_frequency
    import aws_sdk_cost_explorer.types.expression
    import aws_sdk_cost_explorer.types.generic_string
    import aws_sdk_cost_explorer.types.monitor_arn_list
    import aws_sdk_cost_explorer.types.nullable_non_negative_double
    import aws_sdk_cost_explorer.types.subscribers


class UpdateAnomalySubscriptionRequest(TypedDict, closed=True):
    subscription_arn: "aws_sdk_cost_explorer.types.generic_string.GenericString"
    """<p>A cost anomaly subscription Amazon Resource Name (ARN). </p>"""
    threshold: NotRequired[
        "aws_sdk_cost_explorer.types.nullable_non_negative_double.NullableNonNegativeDouble"
    ]
    """<p>(deprecated)</p> <p>The update to the threshold value for receiving notifications. </p> <p>This field has been deprecated. To update a threshold, use ThresholdExpression. Continued use of Threshold will be treated as shorthand syntax for a ThresholdExpression.</p> <p>You can specify either Threshold or ThresholdExpression, but not both.</p>"""
    frequency: NotRequired[
        "aws_sdk_cost_explorer.types.anomaly_subscription_frequency.AnomalySubscriptionFrequency"
    ]
    """<p>The update to the frequency value that subscribers receive notifications. </p>"""
    monitor_arn_list: NotRequired[
        "aws_sdk_cost_explorer.types.monitor_arn_list.MonitorArnList"
    ]
    """<p>A list of cost anomaly monitor ARNs. </p>"""
    subscribers: NotRequired["aws_sdk_cost_explorer.types.subscribers.Subscribers"]
    """<p>The update to the subscriber list. </p>"""
    subscription_name: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The new name of the subscription. </p>"""
    threshold_expression: NotRequired[
        "aws_sdk_cost_explorer.types.expression.Expression"
    ]
    r"""<p>The update to the <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html\">Expression</a> object used to specify the anomalies that you want to generate alerts for. This supports dimensions and nested expressions. The supported dimensions are <code>ANOMALY_TOTAL_IMPACT_ABSOLUTE</code> and <code>ANOMALY_TOTAL_IMPACT_PERCENTAGE</code>, corresponding to an anomaly’s TotalImpact and TotalImpactPercentage, respectively (see <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Impact.html\">Impact</a> for more details). The supported nested expression types are <code>AND</code> and <code>OR</code>. The match option <code>GREATER_THAN_OR_EQUAL</code> is required. Values must be numbers between 0 and 10,000,000,000 in string format.</p> <p>You can specify either Threshold or ThresholdExpression, but not both.</p> <p>The following are examples of valid ThresholdExpressions:</p> <ul> <li> <p>Absolute threshold: <code>{ \"Dimensions\": { \"Key\": \"ANOMALY_TOTAL_IMPACT_ABSOLUTE\", \"MatchOptions\": [ \"GREATER_THAN_OR_EQUAL\" ], \"Values\": [ \"100\" ] } }</code> </p> </li> <li> <p>Percentage threshold: <code>{ \"Dimensions\": { \"Key\": \"ANOMALY_TOTAL_IMPACT_PERCENTAGE\", \"MatchOptions\": [ \"GREATER_THAN_OR_EQUAL\" ], \"Values\": [ \"100\" ] } }</code> </p> </li> <li> <p> <code>AND</code> two thresholds together: <code>{ \"And\": [ { \"Dimensions\": { \"Key\": \"ANOMALY_TOTAL_IMPACT_ABSOLUTE\", \"MatchOptions\": [ \"GREATER_THAN_OR_EQUAL\" ], \"Values\": [ \"100\" ] } }, { \"Dimensions\": { \"Key\": \"ANOMALY_TOTAL_IMPACT_PERCENTAGE\", \"MatchOptions\": [ \"GREATER_THAN_OR_EQUAL\" ], \"Values\": [ \"100\" ] } } ] }</code> </p> </li> <li> <p> <code>OR</code> two thresholds together: <code>{ \"Or\": [ { \"Dimensions\": { \"Key\": \"ANOMALY_TOTAL_IMPACT_ABSOLUTE\", \"MatchOptions\": [ \"GREATER_THAN_OR_EQUAL\" ], \"Values\": [ \"100\" ] } }, { \"Dimensions\": { \"Key\": \"ANOMALY_TOTAL_IMPACT_PERCENTAGE\", \"MatchOptions\": [ \"GREATER_THAN_OR_EQUAL\" ], \"Values\": [ \"100\" ] } } ] }</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAnomalySubscriptionRequest) -> dict:
    out: dict = {}
    out["SubscriptionArn"] = value["subscription_arn"]
    if "threshold" in value:
        out["Threshold"] = value["threshold"]
    if "frequency" in value:
        import aws_sdk_cost_explorer.types.anomaly_subscription_frequency

        out["Frequency"] = (
            aws_sdk_cost_explorer.types.anomaly_subscription_frequency.serialize_aws_json_1_1(
                value["frequency"]
            )
        )
    if "monitor_arn_list" in value:
        import aws_sdk_cost_explorer.types.monitor_arn_list

        out["MonitorArnList"] = (
            aws_sdk_cost_explorer.types.monitor_arn_list.serialize_aws_json_1_1(
                value["monitor_arn_list"]
            )
        )
    if "subscribers" in value:
        import aws_sdk_cost_explorer.types.subscribers

        out["Subscribers"] = (
            aws_sdk_cost_explorer.types.subscribers.serialize_aws_json_1_1(
                value["subscribers"]
            )
        )
    if "subscription_name" in value:
        out["SubscriptionName"] = value["subscription_name"]
    if "threshold_expression" in value:
        import aws_sdk_cost_explorer.types.expression

        out["ThresholdExpression"] = (
            aws_sdk_cost_explorer.types.expression.serialize_aws_json_1_1(
                value["threshold_expression"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAnomalySubscriptionRequest:
    out: UpdateAnomalySubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "SubscriptionArn" in data:
        out["subscription_arn"] = data["SubscriptionArn"]
    else:
        raise DeserializationError(
            "UpdateAnomalySubscriptionRequest.subscription_arn required"
        )
    if "Threshold" in data:
        out["threshold"] = data["Threshold"]
    if "Frequency" in data:
        import aws_sdk_cost_explorer.types.anomaly_subscription_frequency

        out["frequency"] = (
            aws_sdk_cost_explorer.types.anomaly_subscription_frequency.deserialize_aws_json_1_1(
                data["Frequency"]
            )
        )
    if "MonitorArnList" in data:
        import aws_sdk_cost_explorer.types.monitor_arn_list

        out["monitor_arn_list"] = (
            aws_sdk_cost_explorer.types.monitor_arn_list.deserialize_aws_json_1_1(
                data["MonitorArnList"]
            )
        )
    if "Subscribers" in data:
        import aws_sdk_cost_explorer.types.subscribers

        out["subscribers"] = (
            aws_sdk_cost_explorer.types.subscribers.deserialize_aws_json_1_1(
                data["Subscribers"]
            )
        )
    if "SubscriptionName" in data:
        out["subscription_name"] = data["SubscriptionName"]
    if "ThresholdExpression" in data:
        import aws_sdk_cost_explorer.types.expression

        out["threshold_expression"] = (
            aws_sdk_cost_explorer.types.expression.deserialize_aws_json_1_1(
                data["ThresholdExpression"]
            )
        )
    return out
