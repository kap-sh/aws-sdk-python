"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetEC2RecommendationProjectedMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_compute_optimizer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.instance_arn
    import aws_sdk_compute_optimizer.types.metric_statistic
    import aws_sdk_compute_optimizer.types.period
    import aws_sdk_compute_optimizer.types.recommendation_preferences
    import aws_sdk_compute_optimizer.types.timestamp


class GetEC2RecommendationProjectedMetricsRequest(TypedDict, closed=True):
    instance_arn: "aws_sdk_compute_optimizer.types.instance_arn.InstanceArn"
    """<p>The Amazon Resource Name (ARN) of the instances for which to return recommendation projected metrics.</p>"""
    stat: "aws_sdk_compute_optimizer.types.metric_statistic.MetricStatistic"
    """<p>The statistic of the projected metrics.</p>"""
    period: "aws_sdk_compute_optimizer.types.period.Period"
    """<p>The granularity, in seconds, of the projected metrics data points.</p>"""
    start_time: "aws_sdk_compute_optimizer.types.timestamp.Timestamp"
    """<p>The timestamp of the first projected metrics data point to return.</p>"""
    end_time: "aws_sdk_compute_optimizer.types.timestamp.Timestamp"
    """<p>The timestamp of the last projected metrics data point to return.</p>"""
    recommendation_preferences: NotRequired[
        "aws_sdk_compute_optimizer.types.recommendation_preferences.RecommendationPreferences"
    ]
    """<p>An object to specify the preferences for the Amazon EC2 recommendation projected metrics to return in the response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEC2RecommendationProjectedMetricsRequest) -> dict:
    out: dict = {}
    out["instanceArn"] = value["instance_arn"]
    import aws_sdk_compute_optimizer.types.metric_statistic

    out["stat"] = (
        aws_sdk_compute_optimizer.types.metric_statistic.serialize_aws_json_1_0(
            value["stat"]
        )
    )
    out["period"] = value.get("period", 0)
    import aws_sdk_compute_optimizer.types.timestamp

    out["startTime"] = aws_sdk_compute_optimizer.types.timestamp.serialize_aws_json_1_0(
        value["start_time"]
    )
    import aws_sdk_compute_optimizer.types.timestamp

    out["endTime"] = aws_sdk_compute_optimizer.types.timestamp.serialize_aws_json_1_0(
        value["end_time"]
    )
    if "recommendation_preferences" in value:
        import aws_sdk_compute_optimizer.types.recommendation_preferences

        out["recommendationPreferences"] = (
            aws_sdk_compute_optimizer.types.recommendation_preferences.serialize_aws_json_1_0(
                value["recommendation_preferences"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEC2RecommendationProjectedMetricsRequest:
    out: GetEC2RecommendationProjectedMetricsRequest = {}  # type: ignore[typeddict-item]
    if "instanceArn" in data:
        out["instance_arn"] = data["instanceArn"]
    else:
        raise DeserializationError(
            "GetEC2RecommendationProjectedMetricsRequest.instance_arn required"
        )
    if "stat" in data:
        import aws_sdk_compute_optimizer.types.metric_statistic

        out["stat"] = (
            aws_sdk_compute_optimizer.types.metric_statistic.deserialize_aws_json_1_0(
                data["stat"]
            )
        )
    else:
        raise DeserializationError(
            "GetEC2RecommendationProjectedMetricsRequest.stat required"
        )
    if "period" in data:
        out["period"] = data["period"]
    else:
        out["period"] = 0
    if "startTime" in data:
        import aws_sdk_compute_optimizer.types.timestamp

        out["start_time"] = (
            aws_sdk_compute_optimizer.types.timestamp.deserialize_aws_json_1_0(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetEC2RecommendationProjectedMetricsRequest.start_time required"
        )
    if "endTime" in data:
        import aws_sdk_compute_optimizer.types.timestamp

        out["end_time"] = (
            aws_sdk_compute_optimizer.types.timestamp.deserialize_aws_json_1_0(
                data["endTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetEC2RecommendationProjectedMetricsRequest.end_time required"
        )
    if "recommendationPreferences" in data:
        import aws_sdk_compute_optimizer.types.recommendation_preferences

        out["recommendation_preferences"] = (
            aws_sdk_compute_optimizer.types.recommendation_preferences.deserialize_aws_json_1_0(
                data["recommendationPreferences"]
            )
        )
    return out
